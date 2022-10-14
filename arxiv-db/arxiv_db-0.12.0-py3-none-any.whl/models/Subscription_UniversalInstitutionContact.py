
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# Subscription_UniversalInstitutionContact


class SubscriptionUniversalInstitutionContact(Base):
    __tablename__ = 'Subscription_UniversalInstitutionContact'
    __table_args__ = (
        ForeignKeyConstraint(['sid'], ['Subscription_UniversalInstitution.id'], ondelete='CASCADE', name='Subscription_Institution_Contact_Universal'),
        Index('sid', 'sid')
    )

    sid = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    active = Column(TINYINT, server_default=text("'0'"))
    contact_name = Column(String(255))
    phone = Column(String(255))
    note = Column(String(2048))

    Subscription_UniversalInstitution = relationship('SubscriptionUniversalInstitution', back_populates='Subscription_UniversalInstitutionContact')
