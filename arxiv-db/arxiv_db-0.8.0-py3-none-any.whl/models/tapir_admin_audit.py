from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_admin_audit


class TapirAdminAudit(Base):
    __tablename__ = 'tapir_admin_audit'
    __table_args__ = (
        ForeignKeyConstraint(['admin_user'], ['tapir_users.user_id'], name='0_554'),
        ForeignKeyConstraint(['affected_user'], ['tapir_users.user_id'], name='0_555'),
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_553'),
        Index('admin_user', 'admin_user'),
        Index('affected_user', 'affected_user'),
        Index('data', 'data'),
        Index('data_2', 'data'),
        Index('data_3', 'data'),
        Index('ip_addr', 'ip_addr'),
        Index('log_date', 'log_date'),
        Index('session_id', 'session_id')
    )

    log_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    ip_addr = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    affected_user = Column(INTEGER, nullable=False, server_default=text("'0'"))
    tracking_cookie = Column(String(255), nullable=False, server_default=text("''"))
    action = Column(String(32), nullable=False, server_default=text("''"))
    data = Column(Text, nullable=False)
    comment = Column(Text, nullable=False)
    entry_id = Column(INTEGER, primary_key=True)
    session_id = Column(INTEGER)
    admin_user = Column(INTEGER)

    tapir_users = relationship('TapirUsers', foreign_keys=[admin_user], back_populates='tapir_admin_audit')
    tapir_users_ = relationship('TapirUsers', foreign_keys=[affected_user], back_populates='tapir_admin_audit_')
    session = relationship('TapirSessions', back_populates='tapir_admin_audit')
