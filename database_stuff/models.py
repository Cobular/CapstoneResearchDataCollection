from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import sessionmaker, Session

postgres_db = {
    "drivername": "postgres",
    "username": "postgres",
    "password": "rceF^rx71WHq",
    "host": "localhost",
    "port": 5432,
}
engine = create_engine(URL(**postgres_db))
metadata = MetaData()

Base = declarative_base(bind=engine, metadata=metadata)


class Games(Base):
    __tablename__ = "games"

    game_id = Column(BIGINT, primary_key=True)

    def __repr__(self):
        return f"{self.game_id}"


class GamePlayerMetadata(Base):
    __tablename__ = "game_player_metadata"

    id = Column(Integer)
    game_id = Column(
        BIGINT, ForeignKey("games.game_id"), primary_key=True, nullable=False
    )
    match_id = Column(BIGINT, nullable=False)
    blue_team = Column(Boolean, nullable=False)
    esports_team_id = Column(BIGINT, nullable=False)
    esports_player_id = Column(BIGINT, nullable=False)
    participant_id = Column(Integer, nullable=False, primary_key=True)
    summoner_name = Column(String(50), nullable=False)
    champion_id = Column(String(15), nullable=False)
    role = Column(String(7), nullable=False)

    def __repr__(self):
        return f"{self.summoner_name} playing {self.champion_id}"


class GameFrames(Base):
    __tablename__ = "game_frames"

    id = Column(Integer, primary_key=True)
    game_id = Column(BIGINT, nullable=False)
    participant_id = Column(Integer, nullable=False)
    timestamp = Column(Time, nullable=False)
    level = Column(Integer, nullable=False)
    kills = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    assists = Column(Integer, nullable=False)
    totalGoldEarned = Column(Integer, nullable=False)
    creepScore = Column(Integer, nullable=False)
    killParticipation = Column(Integer, nullable=False)
    championDamageShare = Column(Integer, nullable=False)
    wardsPlaced = Column(Integer, nullable=False)
    wardsDestroyed = Column(Integer, nullable=False)
    attackDamage = Column(Integer, nullable=False)
    abilityPower = Column(Integer, nullable=False)
    criticalChance = Column(Integer, nullable=False)
    attackSpeed = Column(Integer, nullable=False)
    lifeSteal = Column(Integer, nullable=False)
    armor = Column(Integer, nullable=False)
    magicResistance = Column(Integer, nullable=False)
    tenacity = Column(Integer, nullable=False)
    items = Column(ARRAY(Integer), nullable=False)
    main_rune = Column(Integer, nullable=False)
    second_rune = Column(Integer, nullable=False)
    rune_choices = Column(ARRAY(Integer), nullable=False)
    abilities = Column(ARRAY(VARCHAR(1)))

    ForeignKeyConstraint(
        ["game_id", "participant_id"],
        ["game_player_metadata.game_id", "game_player_metadata.participant_id"],
    )

    def __repr__(self):
        return f"{self.participant_id} in {self.game_id}"


def session_creator() -> Session:
    session = sessionmaker(bind=engine)
    return session()

