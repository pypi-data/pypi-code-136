
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_qa_reports


class SubmissionQaReports(Base):
    __tablename__ = 'arXiv_submission_qa_reports'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_submission_qa_reports_ibfk_1'),
        Index('report_key_name', 'report_key_name'),
        Index('submission_id', 'submission_id')
    )

    id = Column(Integer, primary_key=True)
    submission_id = Column(Integer, nullable=False)
    report_key_name = Column(String(64), nullable=False)
    num_flags = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    report = Column(JSON, nullable=False)
    created = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    report_uri = Column(String(256))

    submission = relationship('Submissions', back_populates='arXiv_submission_qa_reports')
