
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_moderator_api_key


class ModeratorApiKey(Base):
    __tablename__ = 'arXiv_moderator_api_key'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_moderator_api_key_ibfk_1'),
    )

    user_id = Column(INTEGER, primary_key=True, nullable=False, server_default=text("'0'"))
    secret = Column(String(32), primary_key=True, nullable=False, server_default=text("''"))
    valid = Column(Integer, nullable=False, server_default=text("'1'"))
    issued_when = Column(INTEGER, nullable=False, server_default=text("'0'"))
    issued_to = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))

    user = relationship('TapirUsers', back_populates='arXiv_moderator_api_key')
