from cassiopeia import set_riot_api_key
from cassiopeia import Match
import json

set_riot_api_key("LOLOL")

with open("../data/match_ids.json", "r") as file:
    match_ids = json.load(file)

    for match_id in match_ids:
        current_match = Match(id=match_id, region="INTL")
        print(current_match.blue_team)
        print(match_id)
