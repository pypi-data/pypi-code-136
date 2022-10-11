
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_address


class TapirAddress(Base):
    __tablename__ = 'tapir_address'
    __table_args__ = (
        ForeignKeyConstraint(['country'], ['tapir_countries.digraph'], name='0_523'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_522'),
        Index('address_type', 'address_type'),
        Index('city', 'city'),
        Index('country', 'country'),
        Index('postal_code', 'postal_code')
    )

    user_id = Column(INTEGER, primary_key=True, nullable=False, server_default=text("'0'"))
    address_type = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    company = Column(String(80), nullable=False, server_default=text("''"))
    line1 = Column(String(80), nullable=False, server_default=text("''"))
    line2 = Column(String(80), nullable=False, server_default=text("''"))
    city = Column(String(50), nullable=False, server_default=text("''"))
    state = Column(String(50), nullable=False, server_default=text("''"))
    postal_code = Column(String(16), nullable=False, server_default=text("''"))
    country = Column(CHAR(2), nullable=False, server_default=text("''"))
    share_addr = Column(INTEGER, nullable=False, server_default=text("'0'"))

    tapir_countries = relationship('TapirCountries', back_populates='tapir_address')
    user = relationship('TapirUsers', back_populates='tapir_address')
