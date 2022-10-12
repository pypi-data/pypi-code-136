
from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata

# arXiv_submission_category_proposal


class SubmissionCategoryProposal(Base):
    __tablename__ = 'arXiv_submission_category_proposal'
    __table_args__ = (
        ForeignKeyConstraint(['category'], ['arXiv_category_def.category'], name='arXiv_submission_category_proposal_fk_category'),
        ForeignKeyConstraint(['proposal_comment_id'], ['arXiv_admin_log.id'], name='arXiv_submission_category_proposal_fk_prop_comment_id'),
        ForeignKeyConstraint(['response_comment_id'], ['arXiv_admin_log.id'], name='arXiv_submission_category_proposal_fk_resp_comment_id'),
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submission_category_proposal_fk_submission_id'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_submission_category_proposal_fk_user_id'),
        Index('arXiv_submission_category_proposal_fk_prop_comment_id', 'proposal_comment_id'),
        Index('arXiv_submission_category_proposal_fk_resp_comment_id', 'response_comment_id'),
        Index('arXiv_submission_category_proposal_fk_user_id', 'user_id'),
        Index('arXiv_submission_category_proposal_idx_category', 'category'),
        Index('arXiv_submission_category_proposal_idx_is_primary', 'is_primary'),
        Index('arXiv_submission_category_proposal_idx_key', 'proposal_id'),
        Index('arXiv_submission_category_proposal_idx_submission_id', 'submission_id')
    )

    proposal_id = Column(Integer, primary_key=True, nullable=False)
    submission_id = Column(Integer, primary_key=True, nullable=False)
    category = Column(VARCHAR(32), primary_key=True, nullable=False)
    is_primary = Column(TINYINT(1), primary_key=True, nullable=False, server_default=text("'0'"))
    user_id = Column(INTEGER, nullable=False)
    proposal_status = Column(Integer, server_default=text("'0'"))
    updated = Column(DateTime)
    proposal_comment_id = Column(Integer)
    response_comment_id = Column(Integer)

    arXiv_category_def = relationship('CategoryDef', back_populates='arXiv_submission_category_proposal')
    proposal_comment = relationship('AdminLog', foreign_keys=[proposal_comment_id], back_populates='arXiv_submission_category_proposal')
    response_comment = relationship('AdminLog', foreign_keys=[response_comment_id], back_populates='arXiv_submission_category_proposal_')
    submission = relationship('Submissions', back_populates='arXiv_submission_category_proposal')
    user = relationship('TapirUsers', back_populates='arXiv_submission_category_proposal')
