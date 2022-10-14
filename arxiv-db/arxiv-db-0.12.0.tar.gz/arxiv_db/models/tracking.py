
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_tracking


class Tracking(Base):
    __tablename__ = 'arXiv_tracking'
    __table_args__ = (
        Index('sword_id', 'sword_id', unique=True),
    )

    tracking_id = Column(Integer, primary_key=True)
    sword_id = Column(INTEGER(8), nullable=False, server_default=text("'00000000'"))
    paper_id = Column(String(32), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    submission_errors = Column(Text)

    arXiv_submissions = relationship('Submissions', back_populates='sword')
