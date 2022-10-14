
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# Subscription_UniversalInstitutionIP


class SubscriptionUniversalInstitutionIP(Base):
    __tablename__ = 'Subscription_UniversalInstitutionIP'
    __table_args__ = (
        ForeignKeyConstraint(['sid'], ['Subscription_UniversalInstitution.id'], ondelete='CASCADE', name='Subscription_Institution_IP_Universal'),
        Index('end', 'end'),
        Index('ip', 'start', 'end'),
        Index('sid', 'sid'),
        Index('start', 'start')
    )

    sid = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    end = Column(BigInteger, nullable=False)
    start = Column(BigInteger, nullable=False)
    exclude = Column(TINYINT, server_default=text("'0'"))

    Subscription_UniversalInstitution = relationship('SubscriptionUniversalInstitution', back_populates='Subscription_UniversalInstitutionIP')
