from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from database import Base


class EdgeTeam(Base):

    __tablename__ = "edge_teams"

    id = Column(
        Integer,
        primary_key=True
    )

    tournament_id = Column(Integer)

    team_number = Column(Integer)

    player1_id = Column(Integer)

    player2_id = Column(Integer)

    status = Column(
        Text,
        default="active"
    )
