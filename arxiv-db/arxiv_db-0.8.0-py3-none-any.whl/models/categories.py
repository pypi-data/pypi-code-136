from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_categories

from .archives import Archives
from .endorsement_domains import EndorsementDomains
from .cross_control import CrossControl
from .demographics import Demographics
from .endorsement_requests import EndorsementRequests
from .endorsements import Endorsements

class Categories(Base):
    __tablename__ = 'arXiv_categories'
    __table_args__ = (
        ForeignKeyConstraint(['archive'], ['arXiv_archives.archive_id'], name='0_578'),
        ForeignKeyConstraint(['endorsement_domain'], ['arXiv_endorsement_domains.endorsement_domain'], name='0_753'),
        Index('endorsement_domain', 'endorsement_domain')
    )

    archive = Column(String(16), primary_key=True, nullable=False, server_default=text("''"))
    subject_class = Column(String(16), primary_key=True, nullable=False, server_default=text("''"))
    definitive = Column(Integer, nullable=False, server_default=text("'0'"))
    active = Column(Integer, nullable=False, server_default=text("'0'"))
    endorse_all = Column(Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'"))
    endorse_email = Column(Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'"))
    papers_to_endorse = Column(SMALLINT, nullable=False, server_default=text("'0'"))
    category_name = Column(String(255))
    endorsement_domain = Column(String(32))

    arXiv_archives = relationship('Archives', back_populates='arXiv_categories')
    arXiv_endorsement_domains = relationship('EndorsementDomains', back_populates='arXiv_categories')
    arXiv_cross_control = relationship('CrossControl', back_populates='arXiv_categories')
    arXiv_demographics = relationship('Demographics', back_populates='arXiv_categories')
    arXiv_endorsement_requests = relationship('EndorsementRequests', back_populates='arXiv_categories')
    arXiv_endorsements = relationship('Endorsements', back_populates='arXiv_categories')
