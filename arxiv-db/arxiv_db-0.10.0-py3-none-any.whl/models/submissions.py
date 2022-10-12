from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submissions

class Submissions(Base):
    __tablename__ = 'arXiv_submissions'
    __table_args__ = (
        ForeignKeyConstraint(['agreement_id'], ['arXiv_submission_agreements.agreement_id'], name='agreement_fk'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submissions_fk_document_id'),
        ForeignKeyConstraint(['license'], ['arXiv_licenses.name'], onupdate='CASCADE', name='arXiv_submissions_fk_license'),
        ForeignKeyConstraint(['submitter_id'], ['tapir_users.user_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submissions_fk_submitter_id'),
        ForeignKeyConstraint(['sword_id'], ['arXiv_tracking.sword_id'], name='arXiv_submissions_fk_sword_id'),
        Index('agreement_fk', 'agreement_id'),
        Index('arXiv_submissions_idx_doc_paper_id', 'doc_paper_id'),
        Index('arXiv_submissions_idx_document_id', 'document_id'),
        Index('arXiv_submissions_idx_is_locked', 'is_locked'),
        Index('arXiv_submissions_idx_is_ok', 'is_ok'),
        Index('arXiv_submissions_idx_license', 'license'),
        Index('arXiv_submissions_idx_rt_ticket_id', 'rt_ticket_id'),
        Index('arXiv_submissions_idx_status', 'status'),
        Index('arXiv_submissions_idx_submitter_id', 'submitter_id'),
        Index('arXiv_submissions_idx_sword_id', 'sword_id'),
        Index('arXiv_submissions_idx_type', 'type')
    )

    submission_id = Column(Integer, primary_key=True)
    is_author = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    is_withdrawn = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    version = Column(Integer, nullable=False, server_default=text("'1'"))
    remote_addr = Column(VARCHAR(16), nullable=False, server_default=text("''"))
    remote_host = Column(VARCHAR(255), nullable=False, server_default=text("''"))
    package = Column(VARCHAR(255), nullable=False, server_default=text("''"))
    is_locked = Column(INTEGER, nullable=False, server_default=text("'0'"))
    document_id = Column(MEDIUMINT)
    doc_paper_id = Column(VARCHAR(20))
    sword_id = Column(INTEGER)
    userinfo = Column(TINYINT, server_default=text("'0'"))
    agree_policy = Column(TINYINT(1), server_default=text("'0'"))
    viewed = Column(TINYINT(1), server_default=text("'0'"))
    stage = Column(Integer, server_default=text("'0'"))
    submitter_id = Column(INTEGER)
    submitter_name = Column(String(64))
    submitter_email = Column(String(64))
    created = Column(DateTime)
    updated = Column(DateTime)
    sticky_status = Column(Integer)
    must_process = Column(TINYINT(1), server_default=text("'1'"))
    submit_time = Column(DateTime)
    release_time = Column(DateTime)
    source_size = Column(Integer, server_default=text("'0'"))
    source_format = Column(VARCHAR(12))
    source_flags = Column(VARCHAR(12))
    has_pilot_data = Column(TINYINT(1))
    title = Column(Text)
    authors = Column(Text)
    comments = Column(Text)
    proxy = Column(VARCHAR(255))
    report_num = Column(Text)
    msc_class = Column(String(255))
    acm_class = Column(String(255))
    journal_ref = Column(Text)
    doi = Column(String(255))
    abstract = Column(Text)
    license = Column(VARCHAR(255))
    type = Column(CHAR(8))
    is_ok = Column(TINYINT(1))
    admin_ok = Column(TINYINT(1))
    allow_tex_produced = Column(TINYINT(1), server_default=text("'0'"))
    is_oversize = Column(TINYINT(1), server_default=text("'0'"))
    rt_ticket_id = Column(INTEGER)
    auto_hold = Column(TINYINT(1), server_default=text("'0'"))
    agreement_id = Column(SMALLINT)

    agreement = relationship('SubmissionAgreements', back_populates='arXiv_submissions')
    document = relationship('Documents', back_populates='arXiv_submissions')
    arXiv_licenses = relationship('Licenses', back_populates='arXiv_submissions')
    submitter = relationship('TapirUsers', back_populates='arXiv_submissions')
    sword = relationship('Tracking', back_populates='arXiv_submissions')
    arXiv_pilot_files = relationship('PilotFiles', back_populates='submission')
    arXiv_submission_category = relationship('SubmissionCategory', back_populates='submission')
    arXiv_submission_category_proposal = relationship('SubmissionCategoryProposal', back_populates='submission')
    arXiv_submission_flag = relationship('SubmissionFlag', back_populates='submission')
    arXiv_submission_hold_reason = relationship('SubmissionHoldReason', back_populates='submission')
    arXiv_submission_near_duplicates = relationship('SubmissionNearDuplicates', back_populates='submission')
    arXiv_submission_qa_reports = relationship('SubmissionQaReports', back_populates='submission')
    arXiv_submission_view_flag = relationship('SubmissionViewFlag', back_populates='submission')
