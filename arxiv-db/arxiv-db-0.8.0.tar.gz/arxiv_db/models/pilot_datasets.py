from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_pilot_datasets

class PilotDatasets(Base):
    __tablename__ = 'arXiv_pilot_datasets'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_pilot_datasets_cdfk3'),
    )

    submission_id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    last_checked = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    numfiles = Column(SMALLINT, server_default=text("'0'"))
    feed_url = Column(String(256))
    manifestation = Column(String(256))
    published = Column(TINYINT(1), server_default=text("'0'"))
