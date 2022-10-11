from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from ...database import Base


class MeetingModel(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True)
    meeting_name = Column(String(191), nullable=False, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    updated_at = Column(
        DateTime,
        nullable=False,
        # https://stackoverflow.com/questions/58776476/why-doesnt-freezegun-work-with-sqlalchemy-default-values
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
    )
