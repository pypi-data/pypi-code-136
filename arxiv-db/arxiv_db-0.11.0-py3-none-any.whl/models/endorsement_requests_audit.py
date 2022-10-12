from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_endorsement_requests_audit

from .endorsement_requests import EndorsementRequests

class EndorsementRequestsAudit(EndorsementRequests):
    __tablename__ = 'arXiv_endorsement_requests_audit'
    __table_args__ = (
        ForeignKeyConstraint(['request_id'], ['arXiv_endorsement_requests.request_id'], name='0_725'),
    )

    request_id = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    session_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    remote_addr = Column(String(16))
    remote_host = Column(String(255))
    tracking_cookie = Column(String(255))
