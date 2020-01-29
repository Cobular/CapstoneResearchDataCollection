from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.dialects.postgresql import ARRAY

postgres_db = {
    "drivername": "postgres",
    "username": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432,
}
engine = create_engine(URL(**postgres_db))
metadata = MetaData()

Base = declarative_base(bind=engine, metadata=metadata)


class Games(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=true)

    def __repr__(self):
        return f"{self.game_id}"


class GameMetadata(Base):
    __tablename__ = "game_metadata_player"

    id = Column(Integer)
    game_id = Column(
        Integer, ForeignKey("games.game_id"), primary_key=true, nullable=false
    )
    match_id = Column(Integer, nullable=false)
    blue_team = Column(Boolean, nullable=false)
    esports_player_id = Column(Integer, nullable=false)
    participant_id = Column(Integer, nullable=false, primary_key=true)
    summoner_name = Column(String(50), nullable=false)
    champion_id = Column(String(15), nullable=false)
    role = Column(String(7), nullable=false)

    def __repr__(self):
        return f"{self.summoner_name} playing {self.champion_id}"


class GameFrames(Base):
    __tablename__ = "game_frames"
    id = (Column(Integer, primary_key=true),)
    game_id = (Column(Integer, nullable=false),)
    participant_id = (Column(Integer, nullable=false),)
    timestamp = Column(Time, nullable=false)
    level = Column(int, nullable=false)
    kills = Column(int, nullable=false)
    deaths = Column(int, nullable=false)
    assists = Column(int, nullable=false)
    totalGoldEarned = Column(int, nullable=false)
    creepScore = Column(int, nullable=false)
    killParticipation = Column(int, nullable=false)
    championDamageShare = Column(int, nullable=false)
    wardsPlaced = Column(int, nullable=false)
    wardsDestroyed = Column(int, nullable=false)
    attackDamage = Column(int, nullable=false)
    abilityPower = Column(int, nullable=false)
    criticalChance = Column(int, nullable=false)
    attackSpeed = Column(int, nullable=false)
    lifeSteal = Column(int, nullable=false)
    armor = Column(int, nullable=false)
    magicResistance = Column(int, nullable=false)
    tenacity = Column(int, nullable=false)
    items = Column(ARRAY(Integer), nullable=false)
    main_rune = Column(int, nullable=false)
    second_rune = Column(int, nullable=false)
    rune_choices = Column(ARRAY(int), nullable=false)
    abilities = Column(ARRAY(VARCHAR(1)))

    ForeignKeyConstraint(
        ["game_id", "participant_id"],
        ["game_metadata_player.game_id", "game_metadata_player.participant_id"],
    )

    def __repr__(self):
        return f"{self.participant_id} in {self.game_id}"

