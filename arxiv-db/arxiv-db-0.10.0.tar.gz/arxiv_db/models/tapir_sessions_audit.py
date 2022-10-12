from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_sessions_audit

from .tapir_sessions import TapirSessions

class TapirSessionsAudit(TapirSessions):
    __tablename__ = 'tapir_sessions_audit'
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_527'),
        Index('ip_addr', 'ip_addr'),
        Index('tracking_cookie', 'tracking_cookie')
    )

    session_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    ip_addr = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    tracking_cookie = Column(String(255), nullable=False, server_default=text("''"))
