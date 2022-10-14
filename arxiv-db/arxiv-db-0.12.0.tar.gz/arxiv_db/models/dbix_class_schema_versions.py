
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# dbix_class_schema_versions


class DbixClassSchemaVersions(Base):
    __tablename__ = 'dbix_class_schema_versions'

    version = Column(String(10), primary_key=True)
    installed = Column(String(20), nullable=False)
