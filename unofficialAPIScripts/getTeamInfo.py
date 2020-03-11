import json

import requests


def get_completed_events():
    """Didn't help, the team codes are their 2-3 character short codes. Should probably use it still, for later"""
    header = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    getTeamsPayload = {"hl": "en-US", "tournamentId": ["102804906674705057"]}

    r = requests.get(
        "https://esports-api.lolesports.com/persisted/gw/getCompletedEvents",
        headers=header,
        params=getTeamsPayload,
    )


def get_teams():
    """Totally works, just don't give it a slug in id and it will work"""
    header = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    getTeamsPayload = {
        "hl": "en-US",
        # "id": ["funplus-phoenix"]
    }

    r = requests.get(
        "https://esports-api.lolesports.com/persisted/gw/getTeams",
        headers=header,
        params=getTeamsPayload,
    )

    print(r)


get_teams()
