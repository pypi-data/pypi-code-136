
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submitter_flags


class SubmitterFlags(Base):
    __tablename__ = 'arXiv_submitter_flags'

    flag_id = Column(Integer, primary_key=True)
    comment = Column(String(255))
    pattern = Column(String(255))
