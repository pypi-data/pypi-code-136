
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_pilot_files


class PilotFiles(Base):
    __tablename__ = 'arXiv_pilot_files'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_pilot_files_cdfk3'),
        Index('arXiv_pilot_files_cdfk3', 'submission_id')
    )

    file_id = Column(INTEGER, primary_key=True)
    submission_id = Column(Integer, nullable=False)
    filename = Column(String(256), server_default=text("''"))
    entity_url = Column(String(256))
    description = Column(String(80))
    byRef = Column(TINYINT(1), server_default=text("'1'"))

    submission = relationship('Submissions', back_populates='arXiv_pilot_files')
