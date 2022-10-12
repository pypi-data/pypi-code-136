from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

from .sqa_types import EpochIntArxivTz
metadata = Base.metadata

# arXiv_endorsement_requests


class EndorsementRequests(Base):
    __tablename__ = 'arXiv_endorsement_requests'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_723'),
        ForeignKeyConstraint(['endorsee_id'], ['tapir_users.user_id'], name='0_722'),
        Index('archive', 'archive', 'subject_class'),
        Index('endorsee_id', 'endorsee_id'),
        Index('endorsee_id_2', 'endorsee_id', 'archive', 'subject_class', unique=True),
        Index('secret', 'secret', unique=True)
    )

    request_id = Column(INTEGER, primary_key=True)
    endorsee_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    archive = Column(String(16), nullable=False, server_default=text("''"))
    subject_class = Column(String(16), nullable=False, server_default=text("''"))
    secret = Column(String(16), nullable=False, server_default=text("''"))
    flag_valid = Column(INTEGER, nullable=False, server_default=text("'0'"))
    issued_when = Column(EpochIntArxivTz, nullable=False, server_default=text("'0'"))
    point_value = Column(INTEGER, nullable=False, server_default=text("'0'"))

    arXiv_categories = relationship('Categories', back_populates='arXiv_endorsement_requests')
    endorsee = relationship('TapirUsers', back_populates='arXiv_endorsement_requests', uselist=False)
    endorsement = relationship('Endorsements', back_populates='request', uselist=False)
    ownership_requests = relationship('OwnershipRequests', back_populates='endorsement_request')
    audit = relationship('EndorsementRequestsAudit', uselist=False)
