
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_log_positions


class LogPositions(Base):
    __tablename__ = 'arXiv_log_positions'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    position = Column(INTEGER)
    date = Column(INTEGER)
