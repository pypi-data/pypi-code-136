
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_email_mailings


class TapirEmailMailings(Base):
    __tablename__ = 'tapir_email_mailings'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['tapir_users.user_id'], name='0_565'),
        ForeignKeyConstraint(['sent_by'], ['tapir_users.user_id'], name='0_566'),
        ForeignKeyConstraint(['template_id'], ['tapir_email_templates.template_id'], name='0_567'),
        Index('created_by', 'created_by'),
        Index('sent_by', 'sent_by'),
        Index('template_id', 'template_id')
    )

    mailing_id = Column(INTEGER, primary_key=True)
    template_id = Column(INTEGER)
    created_by = Column(INTEGER)
    sent_by = Column(INTEGER)
    created_date = Column(INTEGER)
    sent_date = Column(INTEGER)
    complete_date = Column(INTEGER)
    mailing_name = Column(String(255))
    comment = Column(Text)

    tapir_users = relationship('TapirUsers', foreign_keys=[created_by], back_populates='tapir_email_mailings')
    tapir_users_ = relationship('TapirUsers', foreign_keys=[sent_by], back_populates='tapir_email_mailings_')
    template = relationship('TapirEmailTemplates', back_populates='tapir_email_mailings')
