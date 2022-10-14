
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_hold_reason


class SubmissionHoldReason(Base):
    __tablename__ = 'arXiv_submission_hold_reason'
    __table_args__ = (
        ForeignKeyConstraint(['comment_id'], ['arXiv_admin_log.id'], name='arXiv_submission_hold_reason_ibfk_3'),
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_hold_reason_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_hold_reason_ibfk_2'),
        Index('comment_id', 'comment_id'),
        Index('submission_id', 'submission_id'),
        Index('user_id', 'user_id')
    )

    reason_id = Column(Integer, primary_key=True, nullable=False)
    submission_id = Column(Integer, nullable=False)
    user_id = Column(INTEGER, primary_key=True, nullable=False)
    reason = Column(String(30))
    type = Column(String(30))
    comment_id = Column(Integer)

    comment = relationship('AdminLog', back_populates='arXiv_submission_hold_reason')
    submission = relationship('Submissions', back_populates='arXiv_submission_hold_reason')
    user = relationship('TapirUsers', back_populates='arXiv_submission_hold_reason')
