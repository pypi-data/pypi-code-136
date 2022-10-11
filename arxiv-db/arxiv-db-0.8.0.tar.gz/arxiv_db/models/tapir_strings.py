
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_strings


class TapirStrings(Base):
    __tablename__ = 'tapir_strings'

    name = Column(String(32), primary_key=True, nullable=False, server_default=text("''"))
    module = Column(String(32), primary_key=True, nullable=False, server_default=text("''"))
    language = Column(String(32), primary_key=True, nullable=False, server_default=text("'en'"))
    string = Column(Text, nullable=False)
