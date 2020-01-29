import json
from database_stuff.models import session_creator, Games, GamePlayerMetadata


def load_games():
    with open("../data/game_ids.json") as game_ids:
        ids = json.load(game_ids)

        session = session_creator()
        for i in ids:
            int_id = int(i)
            session.add(Games(game_id=int_id))
        session.commit()
        session.close()


def load_metadata():
    with open("../data/game_metadata.json") as metadata_json_file:
        metadata_json = json.load(metadata_json_file)

        session = session_creator()
        for game in metadata_json:
            game_id = game["gameID"]
            match_id = game["matchID"]
            esports_team_id = game["gameMetadata"]["blueTeamMetadata"]["esportsTeamId"]

            for blue_team_member in game["gameMetadata"]["blueTeamMetadata"][
                "participantMetadata"
            ]:
                session.add(
                    GamePlayerMetadata(
                        game_id=game_id,
                        match_id=match_id,
                        blue_team=True,
                        esports_team_id=esports_team_id,
                        esports_player_id=blue_team_member["esportsPlayerId"],
                        participant_id=blue_team_member["participantId"],
                        summoner_name=blue_team_member["summonerName"],
                        champion_id=blue_team_member["championId"],
                        role=blue_team_member["role"],
                    )
                )

            for red_team_member in game["gameMetadata"]["redTeamMetadata"][
                "participantMetadata"
            ]:
                session.add(
                    GamePlayerMetadata(
                        game_id=game_id,
                        match_id=match_id,
                        blue_team=False,
                        esports_team_id=esports_team_id,
                        esports_player_id=red_team_member["esportsPlayerId"],
                        participant_id=red_team_member["participantId"],
                        summoner_name=red_team_member["summonerName"],
                        champion_id=red_team_member["championId"],
                        role=red_team_member["role"],
                    )
                )

        session.commit()
        session.close()
