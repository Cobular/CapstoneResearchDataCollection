import json

import requests

header = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
getStandingsPayload = {"hl": "en-US", "tournamentId": ["102804906674705057"]}
Match_IDs = []

r = requests.get(
    "https://prod-relapi.ewp.gg/persisted/gw/getStandings",
    headers=header,
    params=getStandingsPayload,
)

for stage in r.json()["data"]["standings"][0]["stages"]:
    if stage["slug"] == "play_in_groups":
        print("Play In Groups -------------------------------------")
        for section in stage["sections"]:
            for match in section["matches"]:
                Match_IDs.append(match["id"])
                print(match["id"])

    if stage["slug"] == "play_in_elim":
        print("Play In Elim -------------------------------------")
        for section in stage["sections"]:
            for match in section["matches"]:
                Match_IDs.append(match["id"])
                print(match["id"])

    if stage["slug"] == "groups":
        print("Groups -------------------------------------")
        for section in stage["sections"]:
            for match in section["matches"]:
                Match_IDs.append(match["id"])
                print(match["id"])

    if stage["slug"] == "elim":
        print("Elim -------------------------------------")
        for section in stage["sections"]:
            for match in section["matches"]:
                Match_IDs.append(match["id"])
                print(match["id"])

print(json.dumps(Match_IDs))
