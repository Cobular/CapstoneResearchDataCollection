import json

import requests

header = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
GameIds = []

with open("../data/match_ids.json") as match_ids_file:
    match_ids = json.load(match_ids_file)

    for match in match_ids:
        r = requests.get(
            "https://prod-relapi.ewp.gg/persisted/gw/getEventDetails",
            headers=header,
            params={"hl": "en-US", "id": match},
        )
        print(len(r.json()["data"]["event"]["match"]["games"]))
        for game in r.json()["data"]["event"]["match"]["games"]:
            # print(game["id"])
            GameIds.append(game["id"])

print(GameIds, len(GameIds))
