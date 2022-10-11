
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_near_duplicates


class SubmissionNearDuplicates(Base):
    __tablename__ = 'arXiv_submission_near_duplicates'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_near_duplicates_ibfk_1'),
        Index('match', 'submission_id', 'matching_id', unique=True)
    )

    submission_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    matching_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    similarity = Column(DECIMAL(2, 1), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    submission = relationship('Submissions', back_populates='arXiv_submission_near_duplicates')
