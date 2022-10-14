from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

from .tapir_users import TapirUsers
metadata = Base.metadata

# tapir_users_hot


class TapirUsersHot(TapirUsers):
    __tablename__ = 'tapir_users_hot'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_514'),
        Index('last_login', 'last_login'),
        Index('number_sessions', 'number_sessions'),
        Index('second_last_login', 'second_last_login')
    )

    user_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    last_login = Column(INTEGER, nullable=False, server_default=text("'0'"))
    second_last_login = Column(INTEGER, nullable=False, server_default=text("'0'"))
    number_sessions = Column(Integer, nullable=False, server_default=text("'0'"))
