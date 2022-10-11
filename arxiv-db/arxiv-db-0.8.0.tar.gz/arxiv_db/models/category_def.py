from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_category_def


class CategoryDef(Base):
    __tablename__ = 'arXiv_category_def'

    category = Column(String(32), primary_key=True)
    name = Column(String(255))
    active = Column(TINYINT(1), server_default=text("'1'"))

    arXiv_document_category = relationship('DocumentCategory', back_populates='arXiv_category_def')
    arXiv_submission_category = relationship('SubmissionCategory', back_populates='arXiv_category_def')
    arXiv_submission_category_proposal = relationship('SubmissionCategoryProposal', back_populates='arXiv_category_def')
