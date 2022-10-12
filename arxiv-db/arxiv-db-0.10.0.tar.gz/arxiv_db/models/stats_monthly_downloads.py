
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_stats_monthly_downloads


class StatsMonthlyDownloads(Base):
    __tablename__ = 'arXiv_stats_monthly_downloads'

    ym = Column(Date, primary_key=True)
    downloads = Column(INTEGER, nullable=False)
