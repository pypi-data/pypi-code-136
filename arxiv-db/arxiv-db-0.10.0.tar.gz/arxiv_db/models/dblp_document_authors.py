
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_dblp_document_authors


class DblpDocumentAuthors(Base):
    __tablename__ = 'arXiv_dblp_document_authors'
    __table_args__ = (
        ForeignKeyConstraint(['author_id'], ['arXiv_dblp_authors.author_id'], name='arXiv_DBLP_ibfk2'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_DBLP_abfk1'),
        Index('author_id', 'author_id'),
        Index('document_id', 'document_id')
    )

    document_id = Column(MEDIUMINT, primary_key=True, nullable=False)
    author_id = Column(MEDIUMINT, primary_key=True, nullable=False, server_default=text("'0'"))
    position = Column(TINYINT, nullable=False, server_default=text("'0'"))

    author = relationship('DblpAuthors', back_populates='arXiv_dblp_document_authors')
    document = relationship('Documents', back_populates='arXiv_dblp_document_authors')
