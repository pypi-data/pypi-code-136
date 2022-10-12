
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata


class ArchiveCategory(Base):
    __tablename__ = 'arXiv_archive_category'

    archive_id = Column(String(16), primary_key=True, nullable=False, server_default=text("''"))
    category_id = Column(String(32), primary_key=True, nullable=False)
