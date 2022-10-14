from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from arxiv_db.models.tapir_users import TapirUsers

from .. import Base

metadata = Base.metadata

# arXiv_orcid_ids


class OrcidIds(TapirUsers):
    __tablename__ = 'arXiv_orcid_ids'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_orcid_ids_ibfk_1'),
        Index('orcid', 'orcid')
    )

    user_id = Column(INTEGER, primary_key=True)
    orcid = Column(String(19), nullable=False)
    authenticated = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    updated = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
