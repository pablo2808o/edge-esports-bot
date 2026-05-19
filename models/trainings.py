from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from database import Base


class Training(Base):

    __tablename__ = "trainings"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(Text)

    description = Column(Text)

    photo = Column(Text)


class TrainingRegistration(Base):

    __tablename__ = "training_regs"

    id = Column(
        Integer,
        primary_key=True
    )

    training_id = Column(Integer)

    user_id = Column(Integer)

    training_date = Column(Text)

    training_time = Column(Text)

    room_id = Column(Text)

    room_password = Column(Text)
