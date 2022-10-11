
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_sessions


class TapirSessions(Base):
    __tablename__ = 'tapir_sessions'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_525'),
        Index('end_time', 'end_time'),
        Index('start_time', 'start_time'),
        Index('user_id', 'user_id')
    )

    session_id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    last_reissue = Column(Integer, nullable=False, server_default=text("'0'"))
    start_time = Column(Integer, nullable=False, server_default=text("'0'"))
    end_time = Column(Integer, nullable=False, server_default=text("'0'"))

    user = relationship('TapirUsers', back_populates='tapir_sessions')
    tapir_admin_audit = relationship('TapirAdminAudit', back_populates='session')
    tapir_permanent_tokens = relationship('TapirPermanentTokens', back_populates='session')
    tapir_recovery_tokens_used = relationship('TapirRecoveryTokensUsed', back_populates='session')
