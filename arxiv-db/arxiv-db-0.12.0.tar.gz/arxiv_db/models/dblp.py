from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship


from .. import Base

metadata = Base.metadata

# arXiv_dblp

from .documents import Documents

class Dblp(Documents):
    __tablename__ = 'arXiv_dblp'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_DBLP_cdfk1'),
    )

    document_id = Column(MEDIUMINT, primary_key=True, server_default=text("'0'"))
    url = Column(String(80))
