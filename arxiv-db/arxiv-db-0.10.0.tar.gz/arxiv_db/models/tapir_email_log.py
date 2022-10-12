
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_email_log


class TapirEmailLog(Base):
    __tablename__ = 'tapir_email_log'
    __table_args__ = (
        Index('mailing_id', 'mailing_id'),
    )

    mail_id = Column(INTEGER, primary_key=True)
    sent_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    template_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    reference_type = Column(CHAR(1))
    reference_id = Column(INTEGER)
    email = Column(String(255))
    flag_bounced = Column(INTEGER)
    mailing_id = Column(INTEGER)
