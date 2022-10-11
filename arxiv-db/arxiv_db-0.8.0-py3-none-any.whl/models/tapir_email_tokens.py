
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# tapir_email_tokens


class TapirEmailTokens(Base):
    __tablename__ = 'tapir_email_tokens'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_530'),
        Index('secret', 'secret')
    )

    user_id = Column(INTEGER, primary_key=True, nullable=False, server_default=text("'0'"))
    secret = Column(String(32), primary_key=True, nullable=False, server_default=text("''"))
    tapir_dest = Column(String(255), nullable=False, server_default=text("''"))
    issued_when = Column(INTEGER, nullable=False, server_default=text("'0'"))
    issued_to = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    tracking_cookie = Column(String(255), nullable=False, server_default=text("''"))
    wants_perm_token = Column(Integer, nullable=False, server_default=text("'0'"))

    user = relationship('TapirUsers', back_populates='tapir_email_tokens')
