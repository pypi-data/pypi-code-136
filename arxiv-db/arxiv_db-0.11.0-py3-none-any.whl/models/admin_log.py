from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata


class AdminLog(Base):
    __tablename__ = 'arXiv_admin_log'
    __table_args__ = (
        Index('arXiv_admin_log_idx_command', 'command'),
        Index('arXiv_admin_log_idx_paper_id', 'paper_id'),
        Index('arXiv_admin_log_idx_submission_id', 'submission_id'),
        Index('arXiv_admin_log_idx_username', 'username')
    )

    id = Column(Integer, primary_key=True)
    created = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    logtime = Column(String(24))
    paper_id = Column(String(20))
    username = Column(String(20))
    host = Column(String(64))
    program = Column(String(20))
    command = Column(String(20))
    logtext = Column(Text)
    document_id = Column(MEDIUMINT)
    submission_id = Column(Integer)
    notify = Column(TINYINT(1), server_default=text("'0'"))

    arXiv_submission_category_proposal = relationship('SubmissionCategoryProposal', foreign_keys='[SubmissionCategoryProposal.proposal_comment_id]', back_populates='proposal_comment')
    arXiv_submission_category_proposal_ = relationship('SubmissionCategoryProposal', foreign_keys='[SubmissionCategoryProposal.response_comment_id]', back_populates='response_comment')
    arXiv_submission_hold_reason = relationship('SubmissionHoldReason', back_populates='comment')

#  LocalWords:  AdminLog
