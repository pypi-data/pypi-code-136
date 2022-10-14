from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_admin_metadata

class AdminMetadata(Base):
    __tablename__ = 'arXiv_admin_metadata'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', name='meta_doc_fk'),
        Index('document_id', 'document_id'),
        Index('id', 'metadata_id'),
        Index('pidv', 'paper_id', 'version', unique=True)
    )

    metadata_id = Column(Integer, primary_key=True)
    version = Column(Integer, nullable=False, server_default=text("'1'"))
    document_id = Column(MEDIUMINT)
    paper_id = Column(String(64))
    created = Column(DateTime)
    updated = Column(DateTime)
    submitter_name = Column(String(64))
    submitter_email = Column(String(64))
    history = Column(Text)
    source_size = Column(Integer)
    source_type = Column(String(12))
    title = Column(Text)
    authors = Column(Text)
    category_string = Column(String(255))
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
    is_current = Column(TINYINT(1), server_default=text("'0'"))

    document = relationship('Documents', back_populates='arXiv_admin_metadata')
