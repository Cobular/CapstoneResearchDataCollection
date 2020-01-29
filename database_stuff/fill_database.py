import json
from database_stuff.models import session_creator, Games, GamePlayerMetadata, GameFrames
import os
import re
from dateutil import parser


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


def load_frames():
    file_count = 1
    for file in os.listdir("../data/frames"):
        if file.endswith("json"):
            with open(f"../data/frames/{str(file)}") as frames_file:
                frames = json.load(frames_file)
                game_id = re.findall(r"\d+", frames_file.name)

                session = session_creator()

                frame_count = 1
                total_frames = len(frames)
                for frame in frames:
                    timestamp = parser.isoparse(frame["rfc460Timestamp"])
                    player_count = 0
                    for player in frame["participants"]:
                        session.add(
                            GameFrames(
                                game_id=game_id[0],
                                participant_id=player["participantId"],
                                timestamp=timestamp,
                                level=player["level"],
                                kills=player["kills"],
                                deaths=player["deaths"],
                                assists=player["assists"],
                                totalGoldEarned=player["totalGoldEarned"],
                                creepScore=player["creepScore"],
                                killParticipation=player["killParticipation"],
                                championDamageShare=player["championDamageShare"],
                                wardsPlaced=player["wardsPlaced"],
                                wardsDestroyed=player["wardsDestroyed"],
                                attackDamage=player["attackDamage"],
                                abilityPower=player["abilityPower"],
                                criticalChance=player["criticalChance"],
                                attackSpeed=player["attackSpeed"],
                                lifeSteal=player["lifeSteal"],
                                armor=player["armor"],
                                magicResistance=player["magicResistance"],
                                tenacity=player["tenacity"],
                                items=player["items"],
                                main_rune=player["perkMetadata"]["styleId"],
                                second_rune=player["perkMetadata"]["subStyleId"],
                                rune_choices=player["perkMetadata"]["perks"],
                                abilities=player["abilities"],
                            )
                        )
                        print(f"File: {file_count} | Frame: {frame_count}/{total_frames} | Player: {player_count}")
                        player_count += 1
                    frame_count += 1
                session.commit()
                session.close()
        file_count += 1

load_frames()
