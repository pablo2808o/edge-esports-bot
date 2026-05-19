from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from database import Base


class TDMQueue(Base):

    __tablename__ = "tdm_queue"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(Integer)

    rank_selected = Column(Text)

    selected_date = Column(Text)

    selected_time = Column(Text)


class TDMMatch(Base):

    __tablename__ = "tdm_matches"

    id = Column(
        Integer,
        primary_key=True
    )

    player1_id = Column(Integer)

    player2_id = Column(Integer)

    league = Column(Text)

    room_id = Column(Text)

    room_password = Column(Text)

    status = Column(
        Text,
        default="waiting"
    )


class TDMResult(Base):

    __tablename__ = "tdm_results"

    id = Column(
        Integer,
        primary_key=True
    )

    match_id = Column(Integer)

    player_id = Column(Integer)

    screenshot = Column(Text)

    points = Column(
        Integer,
        default=0
    )
