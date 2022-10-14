
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_agreements


class SubmissionAgreements(Base):
    __tablename__ = 'arXiv_submission_agreements'

    agreement_id = Column(SMALLINT, primary_key=True)
    commit_ref = Column(String(255), nullable=False)
    effective_date = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    content = Column(Text)

    arXiv_submissions = relationship('Submissions', back_populates='agreement')
