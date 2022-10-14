from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_author_ids

from .tapir_users import TapirUsers

class AuthorIds(TapirUsers):
    __tablename__ = 'arXiv_author_ids'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_author_ids_ibfk_1'),
        Index('author_id', 'author_id')
    )

    user_id = Column(INTEGER, primary_key=True)
    author_id = Column(String(50), nullable=False)
    updated = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
