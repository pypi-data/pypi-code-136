
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_monitor_mailsent


class MonitorMailsent(Base):
    __tablename__ = 'arXiv_monitor_mailsent'

    t = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    sent = Column(INTEGER)
