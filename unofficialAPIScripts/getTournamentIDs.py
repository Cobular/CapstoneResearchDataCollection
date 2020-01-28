import requests

header = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}

getLeaguesPayload = {"hl": "en-US"}
getLeagues = requests.get(
    "https://prod-relapi.ewp.gg/persisted/gw/getLeagues",
    headers=header,
    params=getLeaguesPayload,
)
print(getLeagues.json()["data"]["leagues"])
# Worlds league ID 98767975604431411

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

getTournamentsForLeaguesPayload = {"hl": "en-US", "leagueId": "98767975604431411"}
getTournamentsForLeagues = requests.get(
    "https://prod-relapi.ewp.gg/persisted/gw/getTournamentsForLeague",
    headers=header,
    params=getLeaguesPayload,
)
print(getTournamentsForLeagues.json())
# 2019 Worlds ID: 102804906674705057, 2018 Worlds ID: 100783238182986407, 2017 Worlds ID: 98767991971246908

getStandingsPayload = {"hl": "en-US", "tournamentId": ["102804906674705057"]}
getStandings = requests.get(
    "https://prod-relapi.ewp.gg/persisted/gw/getStandings",
    headers=header,
    params=getStandingsPayload,
)
print(getStandings.json()["data"]["standings"][0]["stages"])
