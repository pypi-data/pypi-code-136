
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_nicknames_audit


class TapirNicknamesAudit(Base):
    __tablename__ = 'tapir_nicknames_audit'
    __table_args__ = (
        Index('creation_date', 'creation_date'),
        Index('creation_ip_num', 'creation_ip_num'),
        Index('tracking_cookie', 'tracking_cookie')
    )

    nick_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    creation_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    creation_ip_num = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    tracking_cookie = Column(String(255), nullable=False, server_default=text("''"))
