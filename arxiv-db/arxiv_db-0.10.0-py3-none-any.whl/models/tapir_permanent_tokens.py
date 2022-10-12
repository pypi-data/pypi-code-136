
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_permanent_tokens


class TapirPermanentTokens(Base):
    __tablename__ = 'tapir_permanent_tokens'
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_541'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_540'),
        Index('session_id', 'session_id')
    )

    user_id = Column(INTEGER, primary_key=True, nullable=False, server_default=text("'0'"))
    secret = Column(String(32), primary_key=True, nullable=False, server_default=text("''"))
    valid = Column(Integer, nullable=False, server_default=text("'1'"))
    issued_when = Column(INTEGER, nullable=False, server_default=text("'0'"))
    issued_to = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    session_id = Column(INTEGER, nullable=False, server_default=text("'0'"))

    session = relationship('TapirSessions', back_populates='tapir_permanent_tokens')
    user = relationship('TapirUsers', back_populates='tapir_permanent_tokens')
