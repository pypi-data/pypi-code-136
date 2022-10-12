from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_endorsements


class Endorsements(Base):
    """Represents a user endorsing another user."""

    __tablename__ = 'arXiv_endorsements'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_729'),
        ForeignKeyConstraint(['endorsee_id'], ['tapir_users.user_id'], name='0_728'),
        ForeignKeyConstraint(['endorser_id'], ['tapir_users.user_id'], name='0_727'),
        ForeignKeyConstraint(['request_id'], ['arXiv_endorsement_requests.request_id'], name='0_730'),
        Index('archive', 'archive', 'subject_class'),
        Index('endorsee_id', 'endorsee_id'),
        Index('endorser_id', 'endorser_id'),
        Index('endorser_id_2', 'endorser_id', 'endorsee_id', 'archive', 'subject_class', unique=True),
        Index('request_id', 'request_id')
    )

    endorsement_id = Column(INTEGER, primary_key=True)
    endorsee_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    archive = Column(String(16), nullable=False, server_default=text("''"))
    subject_class = Column(String(16), nullable=False, server_default=text("''"))
    flag_valid = Column(INTEGER, nullable=False, server_default=text("'0'"))
    point_value = Column(INTEGER, nullable=False, server_default=text("'0'"))
    issued_when = Column(INTEGER, nullable=False, server_default=text("'0'"))
    endorser_id = Column(INTEGER)
    type = Column(Enum('user', 'admin', 'auto'))
    request_id = Column(INTEGER)

    arXiv_categories = relationship('Categories', back_populates='arXiv_endorsements')
    endorsee = relationship('TapirUsers', foreign_keys=[endorsee_id], back_populates='endorsee_of', uselist=False)
    endorser = relationship('TapirUsers', foreign_keys=[endorser_id], back_populates='endorses', uselist=False)

    request = relationship('EndorsementRequests', back_populates='endorsement', uselist=False)
    """Request for the endorsement by the endorsee."""

    audit = relationship('EndorsementsAudit', uselist=False)
    """Record of response the endorser."""
