
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_titles


class Titles(Base):
    __tablename__ = 'arXiv_titles'
    __table_args__ = (
        Index('arXiv_repno_idx', 'report_num'),
        Index('arXiv_titles_idx', 'title')
    )

    paper_id = Column(String(64), primary_key=True)
    title = Column(String(255))
    report_num = Column(String(255))
    date = Column(Date)
