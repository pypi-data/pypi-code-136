
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_phone


class TapirPhone(Base):
    __tablename__ = 'tapir_phone'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_520'),
        Index('phone_number', 'phone_number'),
        Index('phone_type', 'phone_type')
    )

    user_id = Column(INTEGER, primary_key=True, nullable=False, server_default=text("'0'"))
    phone_type = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    share_phone = Column(INTEGER, nullable=False, server_default=text("'16'"))
    phone_number = Column(String(32))

    user = relationship('TapirUsers', back_populates='tapir_phone')
