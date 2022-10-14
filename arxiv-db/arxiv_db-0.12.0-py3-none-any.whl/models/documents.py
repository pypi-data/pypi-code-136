from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_documents


class Documents(Base):
    __tablename__ = 'arXiv_documents'
    __table_args__ = (
        ForeignKeyConstraint(['submitter_id'], ['tapir_users.user_id'], name='0_580'),
        Index('dated', 'dated'),
        Index('paper_id', 'paper_id', unique=True),
        Index('submitter_email', 'submitter_email'),
        Index('submitter_id', 'submitter_id'),
        Index('title', 'title')
    )

    document_id = Column(MEDIUMINT, primary_key=True)
    paper_id = Column(String(20), nullable=False, server_default=text("''"))
    title = Column(String(255), nullable=False, server_default=text("''"))
    submitter_email = Column(String(64), nullable=False, server_default=text("''"))
    dated = Column(INTEGER, nullable=False, server_default=text("'0'"))
    authors = Column(Text)
    submitter_id = Column(INTEGER)
    primary_subject_class = Column(String(16))
    created = Column(DateTime)

    submitter = relationship('TapirUsers', back_populates='arXiv_documents')
    arXiv_admin_metadata = relationship('AdminMetadata', back_populates='document')
    arXiv_cross_control = relationship('CrossControl', back_populates='document')
    arXiv_dblp_document_authors = relationship('DblpDocumentAuthors', back_populates='document')
    arXiv_document_category = relationship('DocumentCategory', back_populates='document')
    arXiv_jref_control = relationship('JrefControl', back_populates='document')
    arXiv_metadata = relationship('Metadata', back_populates='document')
    arXiv_mirror_list = relationship('MirrorList', back_populates='document')
    arXiv_show_email_requests = relationship('ShowEmailRequests', back_populates='document')
    arXiv_submission_control = relationship('SubmissionControl', back_populates='document')
    arXiv_submissions = relationship('Submissions', back_populates='document')
    arXiv_top_papers = relationship('TopPapers', back_populates='document')
    arXiv_versions = relationship('Versions', back_populates='document')
    owners = relationship('PaperOwners', back_populates='document')
    password = relationship('PaperPw', uselist=False)
    """Paper ownership claim password.

    Warning: there should be only one password but it is not
    constrained in the DB schema.
    """
