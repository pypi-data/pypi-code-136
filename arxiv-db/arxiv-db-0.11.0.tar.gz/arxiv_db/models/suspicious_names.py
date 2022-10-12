from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_suspicious_names

from .tapir_users  import TapirUsers
class SuspiciousNames(TapirUsers):
    __tablename__ = 'arXiv_suspicious_names'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_606'),
    )

    user_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    full_name = Column(String(255), nullable=False, server_default=text("''"))
