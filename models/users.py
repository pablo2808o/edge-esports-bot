from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import Text

from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    telegram_id = Column(
        BigInteger,
        unique=True
    )

    username = Column(Text)

    uid = Column(Text)

    league = Column(
        Text,
        default="EDGE base"
    )

    points = Column(
        Integer,
        default=0
    )

    wins = Column(
        Integer,
        default=0
    )

    losses = Column(
        Integer,
        default=0
    )

    is_approved = Column(
        Integer,
        default=0
    )
