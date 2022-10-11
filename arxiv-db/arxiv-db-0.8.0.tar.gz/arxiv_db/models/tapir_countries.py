
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_countries


class TapirCountries(Base):
    __tablename__ = 'tapir_countries'

    digraph = Column(CHAR(2), primary_key=True, server_default=text("''"))
    country_name = Column(String(255), nullable=False, server_default=text("''"))
    rank = Column(INTEGER, nullable=False, server_default=text("'255'"))

    tapir_address = relationship('TapirAddress', back_populates='tapir_countries')
    tapir_demographics = relationship('TapirDemographics', back_populates='tapir_countries')
