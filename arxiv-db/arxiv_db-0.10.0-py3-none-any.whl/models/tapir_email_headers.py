
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_email_headers


class TapirEmailHeaders(Base):
    __tablename__ = 'tapir_email_headers'
    __table_args__ = (
        ForeignKeyConstraint(['template_id'], ['tapir_email_templates.template_id'], name='0_563'),
    )

    template_id = Column(INTEGER, primary_key=True, nullable=False, server_default=text("'0'"))
    header_name = Column(String(32), primary_key=True, nullable=False, server_default=text("''"))
    header_content = Column(String(255), nullable=False, server_default=text("''"))

    template = relationship('TapirEmailTemplates', back_populates='tapir_email_headers')
