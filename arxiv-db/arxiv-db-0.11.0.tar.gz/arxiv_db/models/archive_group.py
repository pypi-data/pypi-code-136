
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_archive_group


class ArchiveGroup(Base):
    __tablename__ = 'arXiv_archive_group'

    archive_id = Column(String(16), primary_key=True, nullable=False, server_default=text("''"))
    group_id = Column(String(16), primary_key=True, nullable=False, server_default=text("''"))
