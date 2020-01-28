import datetime
import json

import requests
from dateutil import parser

header = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
error_list = []
success_list = []
data_list = []


def round_time(dt=None, round_to=60):
    """https://kite.com/python/examples/4653/datetime-round-datetime-to-any-time-interval-in-seconds"""
    if dt == None:
        dt = datetime.datetime.now()
    seconds = (dt.replace(tzinfo=None) - dt.min.replace(tzinfo=None)).seconds
    rounding = (seconds + round_to / 2) // round_to * round_to
    return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)


def get_frames_until_fin(game_id):
    frames_list = []
    re = requests.get(
        f"https://feed.lolesports.com/livestats/v1/details/{game_id}", headers=header,
    )

    if re.status_code == 200:
        frames_list.extend(re.json()["frames"])

    end_frame_time = round_time(
        parser.isoparse(re.json()["frames"][-1]["rfc460Timestamp"]), round_to=10
    )
    past_end_frame_time = datetime.datetime.utcfromtimestamp(0)
    game_start_time = parser.isoparse(re.json()["frames"][-1]["rfc460Timestamp"])
    real_start_time = datetime.datetime.now()

    loop_count = 0

    try:
        while True:
            re = requests.get(
                f"https://feed.lolesports.com/livestats/v1/details/{game_id}?startingTime={end_frame_time.isoformat().replace('+00:00', 'Z')}",
                headers=header,
            )
            frames_list.extend(re.json()["frames"])
            end_frame_time = round_time(
                parser.isoparse(re.json()["frames"][-1]["rfc460Timestamp"]), round_to=10
            )
            loop_count += 1
            print(f"Frames: {len(frames_list)} | dFrames: {len(re.json()['frames'])} | Loops: {loop_count} | Game Time: {end_frame_time - game_start_time} | Run Duration: {datetime.datetime.now() - real_start_time}")

            if end_frame_time == past_end_frame_time:
                break
            past_end_frame_time = end_frame_time
    except Exception as exc:
        print(exc)
        return frames_list

    print("fin")
    return frames_list


# def get_frames_until_fin_recursive(game_id, frames_list, old_req):
#     frames_list.append(old_req.json()["frames"])
#     if len(old_req.json()["frames"]) == 10:
#         req = requests.get(
#             f"https://feed.lolesports.com/livestats/v1/details/{game_id}?startingTime={old_req.json()['frames'][-1]['rfc460Timestamp']}",
#             headers=header,
#         )
#         r
#     else:
#         return old_req


with open("../data/valid_game_ids.json") as game_ids_file:
    game_ids = json.load(game_ids_file)

    for game in game_ids:
        with open(f'output_{game}.json', 'w') as outfile:
            json_data = get_frames_until_fin(game)
            json.dump(json_data, outfile)

        print(f"done with {game}")

        # r = requests.get(
        #     f"https://feed.lolesports.com/livestats/v1/details/{game}", headers=header,
        # )

        # if r.status_code == 200:
        #     data_list.append(
        #         {
        #             "gameID": r.json()["esportsGameId"],
        #             "matchID": r.json()["esportsMatchId"],
        #             "gameMetadata": r.json()["gameMetadata"],
        #         }
        #     )
        #     # print(r.json())
        # else:
        #     error_list.append(game)
        #     print(f"HTTP Error Alert! Game ID: {game} | Status Code: {r.status_code}")

print(data_list)
print(error_list)
