from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_sword_licenses
from .tapir_users import TapirUsers

class SwordLicenses(TapirUsers):
    __tablename__ = 'arXiv_sword_licenses'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='user_id_fk'),
    )

    user_id = Column(INTEGER, primary_key=True)
    updated = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    license = Column(String(127))
