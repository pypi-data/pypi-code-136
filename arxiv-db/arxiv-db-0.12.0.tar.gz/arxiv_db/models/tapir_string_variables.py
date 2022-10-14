
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_string_variables


class TapirStringVariables(Base):
    __tablename__ = 'tapir_string_variables'

    variable_id = Column(String(32), primary_key=True, server_default=text("''"))
    value = Column(Text, nullable=False)
