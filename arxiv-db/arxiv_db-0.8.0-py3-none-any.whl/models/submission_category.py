
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_category


class SubmissionCategory(Base):
    __tablename__ = 'arXiv_submission_category'
    __table_args__ = (
        ForeignKeyConstraint(['category'], ['arXiv_category_def.category'], name='arXiv_submission_category_fk_category'),
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submission_category_fk_submission_id'),
        Index('arXiv_submission_category_idx_category', 'category'),
        Index('arXiv_submission_category_idx_is_primary', 'is_primary'),
        Index('arXiv_submission_category_idx_is_published', 'is_published'),
        Index('arXiv_submission_category_idx_submission_id', 'submission_id')
    )

    submission_id = Column(Integer, primary_key=True, nullable=False)
    category = Column(String(32), primary_key=True, nullable=False, server_default=text("''"))
    is_primary = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_published = Column(TINYINT(1), server_default=text("'0'"))

    arXiv_category_def = relationship('CategoryDef', back_populates='arXiv_submission_category')
    submission = relationship('Submissions', back_populates='arXiv_submission_category')
