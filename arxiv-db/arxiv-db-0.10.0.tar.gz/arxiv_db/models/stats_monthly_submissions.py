
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_stats_monthly_submissions


class StatsMonthlySubmissions(Base):
    __tablename__ = 'arXiv_stats_monthly_submissions'

    ym = Column(Date, primary_key=True, server_default=text("'0000-00-00'"))
    num_submissions = Column(SMALLINT, nullable=False)
    historical_delta = Column(TINYINT, nullable=False, server_default=text("'0'"))
