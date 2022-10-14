from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_paper_pw

class PaperPw(Base):
    __tablename__ = 'arXiv_paper_pw'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_585'),
    )

    document_id = Column(MEDIUMINT, primary_key=True, server_default=text("'0'"))
    password_storage = Column(INTEGER)
    password_enc = Column(String(50))
