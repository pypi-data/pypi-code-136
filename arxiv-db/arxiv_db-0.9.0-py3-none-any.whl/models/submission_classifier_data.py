from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_classifier_data
from .submissions import Submissions

class SubmissionClassifierData(Base):
    __tablename__ = 'arXiv_submission_classifier_data'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_classifier_data_ibfk_1'),
    )

    submission_id = Column(Integer, primary_key=True, server_default=text("'0'"))
    last_update = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    json = Column(Text)
    status = Column(Enum('processing', 'success', 'failed', 'no connection'))
    message = Column(Text)
    is_oversize = Column(TINYINT(1), server_default=text("'0'"))
