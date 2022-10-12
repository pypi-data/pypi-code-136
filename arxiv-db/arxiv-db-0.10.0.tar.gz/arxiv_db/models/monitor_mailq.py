
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_monitor_mailq


class MonitorMailq(Base):
    __tablename__ = 'arXiv_monitor_mailq'

    t = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    main_q = Column(INTEGER, nullable=False, server_default=text("'0'"))
    local_q = Column(INTEGER, nullable=False, server_default=text("'0'"))
    local_host_map = Column(INTEGER, nullable=False, server_default=text("'0'"))
    local_timeout = Column(INTEGER, nullable=False, server_default=text("'0'"))
    local_refused = Column(INTEGER, nullable=False, server_default=text("'0'"))
    local_in_flight = Column(INTEGER, nullable=False, server_default=text("'0'"))
