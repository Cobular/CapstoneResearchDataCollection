# https://esports-api.lolesports.com/persisted/gw/getStandings

import json

import requests

header = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
getStandingsPayload = {"hl": "en-US", "tournamentId": ["102804906674705057"]}
game_results = []

r = requests.get(
    "https://esports-api.lolesports.com/persisted/gw/getStandings",
    headers=header,
    params=getStandingsPayload,
)

for stages in r.json()["data"]["standings"][0]["stages"]:
    if stages["slug"] == "play_in_groups":
        for sections in stages["sections"]:
            for match in sections["matches"]:
                for team in match["teams"]:
                    if team["result"]["outcome"] == "loss":
                        win = False
                    else:
                        win = True
                    game_results.append({"match_id": match["id"], "team_id": team["id"], "win": win})

    if stages["slug"] == "play_in_elim":
        for sections in stages["sections"]:
            for match in sections["matches"]:
                for team in match["teams"]:
                    if team["result"]["outcome"] == "loss":
                        win = False
                    else:
                        win = True
                    game_results.append({"match_id": match["id"], "team_id": team["id"], "win": win})

    if stages["slug"] == "groups":
        for sections in stages["sections"]:
            for match in sections["matches"]:
                for team in match["teams"]:
                    if team["result"]["outcome"] == "loss":
                        win = False
                    else:
                        win = True
                    game_results.append({"match_id": match["id"], "team_id": team["id"], "win": win})

    if stages["slug"] == "elim":
        for sections in stages["sections"]:
            for match in sections["matches"]:
                for team in match["teams"]:
                    if team["result"]["outcome"] == "loss":
                        win = False
                    else:
                        win = True
                    game_results.append({"match_id": match["id"], "team_id": team["id"], "win": win})

print(game_results)