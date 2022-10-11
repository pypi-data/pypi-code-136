
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_top_papers


class TopPapers(Base):
    __tablename__ = 'arXiv_top_papers'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_top_papers_ibfk_1'),
        Index('document_id', 'document_id')
    )

    from_week = Column(Date, primary_key=True, nullable=False, server_default=text("'0000-00-00'"))
    class_ = Column('class', CHAR(1), primary_key=True, nullable=False, server_default=text("''"))
    rank = Column(SMALLINT, primary_key=True, nullable=False, server_default=text("'0'"))
    document_id = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    viewers = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))

    document = relationship('Documents', back_populates='arXiv_top_papers')
