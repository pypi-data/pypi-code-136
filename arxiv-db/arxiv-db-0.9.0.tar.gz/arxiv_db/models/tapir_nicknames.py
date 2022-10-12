from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_nicknames


class TapirNicknames(Base):
    __tablename__ = 'tapir_nicknames'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_570'),
        Index('flag_valid', 'flag_valid'),
        Index('nickname', 'nickname', unique=True),
        Index('policy', 'policy'),
        Index('role', 'role'),
        Index('user_id', 'user_id', 'user_seq', unique=True)
    )

    nick_id = Column(INTEGER, primary_key=True)
    nickname = Column(String(20), nullable=False, server_default=text("''"))
    user_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    user_seq = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_valid = Column(INTEGER, nullable=False, server_default=text("'0'"))
    role = Column(INTEGER, nullable=False, server_default=text("'0'"))
    policy = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_primary = Column(INTEGER, nullable=False, server_default=text("'0'"))

    user = relationship('TapirUsers', back_populates='tapir_nicknames')
