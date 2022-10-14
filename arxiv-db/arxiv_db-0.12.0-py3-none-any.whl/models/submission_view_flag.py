
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_view_flag


class SubmissionViewFlag(Base):
    __tablename__ = 'arXiv_submission_view_flag'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_view_flag_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_view_flag_ibfk_2'),
        Index('user_id', 'user_id')
    )

    submission_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(INTEGER, primary_key=True, nullable=False)
    flag = Column(TINYINT(1), server_default=text("'0'"))
    updated = Column(DateTime)

    submission = relationship('Submissions', back_populates='arXiv_submission_view_flag')
    user = relationship('TapirUsers', back_populates='arXiv_submission_view_flag')
