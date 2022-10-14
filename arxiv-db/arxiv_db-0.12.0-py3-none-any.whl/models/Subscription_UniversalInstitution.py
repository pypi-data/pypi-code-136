
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata


class SubscriptionUniversalInstitution(Base):
    __tablename__ = 'Subscription_UniversalInstitution'
    __table_args__ = (
        Index('name', 'name'),
    )

    name = Column(String(255), nullable=False)
    id = Column(Integer, primary_key=True)
    resolver_URL = Column(String(255))
    label = Column(String(255))
    alt_text = Column(String(255))
    link_icon = Column(String(255))
    note = Column(String(255))

    Subscription_UniversalInstitutionContact = relationship('SubscriptionUniversalInstitutionContact', back_populates='Subscription_UniversalInstitution')
    Subscription_UniversalInstitutionIP = relationship('SubscriptionUniversalInstitutionIP', back_populates='Subscription_UniversalInstitution')
