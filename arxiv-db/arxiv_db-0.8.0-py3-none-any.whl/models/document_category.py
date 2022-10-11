
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_document_category


class DocumentCategory(Base):
    __tablename__ = 'arXiv_document_category'
    __table_args__ = (
        ForeignKeyConstraint(['category'], ['arXiv_category_def.category'], name='doc_cat_cat'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', name='doc_cat_doc'),
        Index('category', 'category'),
        Index('document_id', 'document_id')
    )

    document_id = Column(MEDIUMINT, primary_key=True, nullable=False, server_default=text("'0'"))
    category = Column(String(32), primary_key=True, nullable=False)
    is_primary = Column(TINYINT(1), nullable=False, server_default=text("'0'"))

    arXiv_category_def = relationship('CategoryDef', back_populates='arXiv_document_category')
    document = relationship('Documents', back_populates='arXiv_document_category')
