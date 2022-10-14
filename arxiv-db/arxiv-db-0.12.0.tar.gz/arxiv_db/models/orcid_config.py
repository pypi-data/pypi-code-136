
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_orcid_config


class OrcidConfig(Base):
    __tablename__ = 'arXiv_orcid_config'

    domain = Column(String(75), primary_key=True, nullable=False)
    keyname = Column(String(60), primary_key=True, nullable=False)
    value = Column(String(150))
