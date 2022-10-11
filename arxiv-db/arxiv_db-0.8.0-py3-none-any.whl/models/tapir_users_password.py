from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_users_password
from .tapir_users import TapirUsers

class TapirUsersPassword(TapirUsers):
    __tablename__ = 'tapir_users_password'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_512'),
    )

    user_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    password_storage = Column(INTEGER, nullable=False, server_default=text("'0'"))
    password_enc = Column(String(50), nullable=False, server_default=text("''"))
