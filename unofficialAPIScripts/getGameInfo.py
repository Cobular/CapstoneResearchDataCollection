import json

import requests

header = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
error_list = []
success_list = []
data_list = []

with open("../data/valid_game_ids.json") as game_ids_file:
    game_ids = json.load(game_ids_file)

    for game in game_ids:
        r = requests.get(
            f"https://feed.lolesports.com/livestats/v1/window/{game}", headers=header,
        )

        if r.status_code == 200:
            data_list.append({
                "gameID": r.json()['esportsGameId'],
                "matchID": r.json()['esportsMatchId'],
                "gameMetadata": r.json()['gameMetadata'],
            })
            # print(r.json())
        else:
            error_list.append(game)
            print(f"HTTP Error Alert! Game ID: {game} | Status Code: {r.status_code}")

print(data_list)
print(error_list)
