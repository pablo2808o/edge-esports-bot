from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import Text

from database import Base


class ClanApplication(Base):

    __tablename__ = "clan_applications"

    id = Column(
        Integer,
        primary_key=True
    )

    telegram_id = Column(BigInteger)

    username = Column(Text)

    uid = Column(Text)

    screenshot = Column(Text)

    exp_type = Column(Text)

    exp_text = Column(Text)

    status = Column(
        Text,
        default="pending"
    )
