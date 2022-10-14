
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_recovery_tokens_used


class TapirRecoveryTokensUsed(Base):
    __tablename__ = 'tapir_recovery_tokens_used'
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_549'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_548'),
        Index('session_id', 'session_id')
    )

    user_id = Column(INTEGER, primary_key=True, nullable=False, server_default=text("'0'"))
    secret = Column(String(32), primary_key=True, nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    used_when = Column(INTEGER)
    used_from = Column(String(16))
    session_id = Column(INTEGER)

    session = relationship('TapirSessions', back_populates='tapir_recovery_tokens_used')
    user = relationship('TapirUsers', back_populates='tapir_recovery_tokens_used')
