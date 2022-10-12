from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .associative_tables import t_arXiv_ownership_requests_papers
from .. import Base

metadata = Base.metadata

# arXiv_ownership_requests


class OwnershipRequests(Base):
    __tablename__ = 'arXiv_ownership_requests'
    __table_args__ = (
        ForeignKeyConstraint(['endorsement_request_id'], ['arXiv_endorsement_requests.request_id'], name='0_735'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_734'),
        Index('endorsement_request_id', 'endorsement_request_id'),
        Index('user_id', 'user_id')
    )

    request_id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    workflow_status = Column(Enum('pending', 'accepted', 'rejected'), nullable=False, server_default=text("'pending'"))
    endorsement_request_id = Column(INTEGER)

    request_audit = relationship('OwnershipRequestsAudit')
    endorsement_request = relationship('EndorsementRequests', back_populates='ownership_requests')
    user = relationship('TapirUsers', back_populates='arXiv_ownership_requests')
    documents = relationship("Documents", secondary=t_arXiv_ownership_requests_papers)
