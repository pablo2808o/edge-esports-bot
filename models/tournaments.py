from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from database import Base


class BigPlayTournament(Base):

    __tablename__ = "bigplay_tournaments"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(Text)

    description = Column(Text)

    photo = Column(Text)

    tournament_date = Column(Text)


class EdgeTournament(Base):

    __tablename__ = "edge_tournaments"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(Text)

    description = Column(Text)

    photo = Column(Text)

    tournament_date = Column(Text)
