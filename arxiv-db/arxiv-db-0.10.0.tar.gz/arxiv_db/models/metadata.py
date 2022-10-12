from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_metadata

class Metadata(Base):
    __tablename__ = 'arXiv_metadata'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_metadata_fk_document_id'),
        ForeignKeyConstraint(['license'], ['arXiv_licenses.name'], name='arXiv_metadata_fk_license'),
        ForeignKeyConstraint(['submitter_id'], ['tapir_users.user_id'], name='arXiv_metadata_fk_submitter_id'),
        Index('arXiv_metadata_idx_document_id', 'document_id'),
        Index('arXiv_metadata_idx_license', 'license'),
        Index('arXiv_metadata_idx_submitter_id', 'submitter_id'),
        Index('pidv', 'paper_id', 'version', unique=True)
    )

    metadata_id = Column(Integer, primary_key=True)
    document_id = Column(MEDIUMINT, nullable=False, server_default=text("'0'"))
    paper_id = Column(String(64), nullable=False)
    submitter_name = Column(String(64), nullable=False)
    submitter_email = Column(String(64), nullable=False)
    version = Column(Integer, nullable=False, server_default=text("'1'"))
    is_withdrawn = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    created = Column(DateTime)
    updated = Column(DateTime)
    submitter_id = Column(INTEGER)
    source_size = Column(Integer)
    source_format = Column(String(12))
    source_flags = Column(String(12))
    title = Column(Text)
    authors = Column(Text)
    abs_categories = Column(String(255))
    comments = Column(Text)
    proxy = Column(String(255))
    report_num = Column(Text)
    msc_class = Column(String(255))
    acm_class = Column(String(255))
    journal_ref = Column(Text)
    doi = Column(String(255))
    abstract = Column(Text)
    license = Column(String(255))
    modtime = Column(Integer)
    is_current = Column(TINYINT(1), server_default=text("'1'"))

    document = relationship('Documents', back_populates='arXiv_metadata')
    arXiv_licenses = relationship('Licenses', back_populates='arXiv_metadata')
    submitter = relationship('TapirUsers', back_populates='arXiv_metadata')
    arXiv_datacite_dois = relationship('DataciteDois', back_populates='metadata_')
