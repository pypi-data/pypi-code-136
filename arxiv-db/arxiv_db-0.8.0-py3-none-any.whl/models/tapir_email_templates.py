
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_email_templates


class TapirEmailTemplates(Base):
    __tablename__ = 'tapir_email_templates'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['tapir_users.user_id'], name='0_560'),
        ForeignKeyConstraint(['updated_by'], ['tapir_users.user_id'], name='0_561'),
        Index('created_by', 'created_by'),
        Index('short_name', 'short_name', 'lang', unique=True),
        Index('update_date', 'update_date'),
        Index('updated_by', 'updated_by')
    )

    template_id = Column(INTEGER, primary_key=True)
    short_name = Column(String(32), nullable=False, server_default=text("''"))
    lang = Column(CHAR(2), nullable=False, server_default=text("'en'"))
    long_name = Column(String(255), nullable=False, server_default=text("''"))
    data = Column(Text, nullable=False)
    sql_statement = Column(Text, nullable=False)
    update_date = Column(INTEGER, nullable=False, server_default=text("'0'"))
    created_by = Column(INTEGER, nullable=False, server_default=text("'0'"))
    updated_by = Column(INTEGER, nullable=False, server_default=text("'0'"))
    workflow_status = Column(INTEGER, nullable=False, server_default=text("'0'"))
    flag_system = Column(INTEGER, nullable=False, server_default=text("'0'"))

    tapir_users = relationship('TapirUsers', foreign_keys=[created_by], back_populates='tapir_email_templates')
    tapir_users_ = relationship('TapirUsers', foreign_keys=[updated_by], back_populates='tapir_email_templates_')
    tapir_email_headers = relationship('TapirEmailHeaders', back_populates='template')
    tapir_email_mailings = relationship('TapirEmailMailings', back_populates='template')
