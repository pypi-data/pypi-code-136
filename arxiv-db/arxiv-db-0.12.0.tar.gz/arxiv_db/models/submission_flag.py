
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_flag


class SubmissionFlag(Base):
    __tablename__ = 'arXiv_submission_flag'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_flag_ibfk_2'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_flag_ibfk_1'),
        Index('uniq_one_flag_per_mod', 'submission_id', 'user_id', unique=True),
        Index('user_id', 'user_id')
    )

    flag_id = Column(Integer, primary_key=True)
    user_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    submission_id = Column(Integer, nullable=False)
    flag = Column(TINYINT, nullable=False, server_default=text("'0'"))
    updated = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    submission = relationship('Submissions', back_populates='arXiv_submission_flag')
    user = relationship('TapirUsers', back_populates='arXiv_submission_flag')
