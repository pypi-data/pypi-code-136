from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_ownership_requests_audit
from .sqa_types import EpochIntArxivTz

from .ownership_requests import OwnershipRequests

class OwnershipRequestsAudit(Base):
    __tablename__ = 'arXiv_ownership_requests_audit'
    __table_args__ = (
        ForeignKeyConstraint(['request_id'], ['arXiv_ownership_requests.request_id'], name='0_737'),
    )

    request_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    session_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    remote_addr = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    tracking_cookie = Column(String(255), nullable=False, server_default=text("''"))
    date = Column(EpochIntArxivTz, nullable=False, server_default=text("'0'"))
