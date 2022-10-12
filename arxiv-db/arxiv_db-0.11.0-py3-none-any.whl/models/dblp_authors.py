
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_dblp_authors


class DblpAuthors(Base):
    __tablename__ = 'arXiv_dblp_authors'
    __table_args__ = (
        Index('author_id', 'author_id', unique=True),
        Index('name', 'name', unique=True)
    )

    author_id = Column(MEDIUMINT, primary_key=True)
    name = Column(String(40))

    arXiv_dblp_document_authors = relationship('DblpDocumentAuthors', back_populates='author')
