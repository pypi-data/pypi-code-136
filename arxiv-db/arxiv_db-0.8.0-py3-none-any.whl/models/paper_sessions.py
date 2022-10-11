
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_paper_sessions


class PaperSessions(Base):
    __tablename__ = 'arXiv_paper_sessions'

    paper_session_id = Column(INTEGER, primary_key=True)
    paper_id = Column(String(16), nullable=False, server_default=text("''"))
    start_time = Column(INTEGER, nullable=False, server_default=text("'0'"))
    end_time = Column(INTEGER, nullable=False, server_default=text("'0'"))
    ip_name = Column(String(16), nullable=False, server_default=text("''"))
