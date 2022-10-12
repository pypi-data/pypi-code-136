"""arXiv SQLAlchemy models as dataclasses.

Generated from the production DB 2022-09-23 using sqlacodegen 3.0.0rc1 with the nojoined option.

2022-09-23 Convert the mysql specific types to generic types

CHAR -> generic CHAR
DECIMAL -> Numeric()
INTEGER, MEDIUMINT -> Integer
SMALLINT -> SmallInteger
VARCHAR -> String()
MEDIUMTEXT -> Text
TINYINT -> Some to SmallInteger and any with "is_something" to Boolean

Added a prefix to many index names to avoid duplicates.

"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text, Boolean
from sqlalchemy.types import SmallInteger, Numeric
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()
metadata = mapper_registry.metadata

# CURRENT_TIMESTAMP_SD=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))})
CURRENT_TIMESTAMP_SD=None

@mapper_registry.mapped
@dataclass
class SubscriptionUniversalInstitution:
    __tablename__ = 'Subscription_UniversalInstitution'
    __table_args__ = (
        Index('idx_0_name', 'name'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    name: str = field(metadata={'sa': Column(String(255), nullable=False)})
    id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    resolver_URL: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    label: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    alt_text: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    link_icon: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    note: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})

    Subscription_UniversalInstitutionContact: List[SubscriptionUniversalInstitutionContact] = field(default_factory=list, metadata={'sa': relationship('SubscriptionUniversalInstitutionContact', back_populates='Subscription_UniversalInstitution')})
    Subscription_UniversalInstitutionIP: List[SubscriptionUniversalInstitutionIP] = field(default_factory=list, metadata={'sa': relationship('SubscriptionUniversalInstitutionIP', back_populates='Subscription_UniversalInstitution')})


@mapper_registry.mapped
@dataclass
class ArXivAdminLog:
    __tablename__ = 'arXiv_admin_log'
    __table_args__ = (
        Index('arXiv_admin_log_idx_command', 'command'),
        Index('arXiv_admin_log_idx_paper_id', 'paper_id'),
        Index('arXiv_admin_log_idx_submission_id', 'submission_id'),
        Index('arXiv_admin_log_idx_username', 'username')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    created: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD)})
    logtime: Optional[str] = field(default=None, metadata={'sa': Column(String(24))})
    paper_id: Optional[str] = field(default=None, metadata={'sa': Column(String(20))})
    username: Optional[str] = field(default=None, metadata={'sa': Column(String(20))})
    host: Optional[str] = field(default=None, metadata={'sa': Column(String(64))})
    program: Optional[str] = field(default=None, metadata={'sa': Column(String(20))})
    command: Optional[str] = field(default=None, metadata={'sa': Column(String(20))})
    logtext: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    document_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    submission_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    notify: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})

    arXiv_submission_category_proposal: List[ArXivSubmissionCategoryProposal] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionCategoryProposal', foreign_keys='[ArXivSubmissionCategoryProposal.proposal_comment_id]', back_populates='proposal_comment')})
    arXiv_submission_category_proposal_: List[ArXivSubmissionCategoryProposal] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionCategoryProposal', foreign_keys='[ArXivSubmissionCategoryProposal.response_comment_id]', back_populates='response_comment')})
    arXiv_submission_hold_reason: List[ArXivSubmissionHoldReason] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionHoldReason', back_populates='comment')})


t_arXiv_admin_state = Table(
    'arXiv_admin_state', metadata,
    Column('document_id', Integer),
    Column('timestamp', TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD),
    Column('abs_timestamp', Integer),
    Column('src_timestamp', Integer),
    Column('state', Enum('pending', 'ok', 'bad'), nullable=False, server_default=text("'pending'")),
    Column('admin', String(32)),
    Column('comment', String(255)),
    Index('idx_1_document_id', 'document_id', unique=True)
)


@mapper_registry.mapped
@dataclass
class ArXivArchiveCategory:
    __tablename__ = 'arXiv_archive_category'
    __sa_dataclass_metadata_key__ = 'sa'

    archive_id: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, nullable=False, server_default=text("''"))})
    category_id: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False)})


@mapper_registry.mapped
@dataclass
class ArXivArchiveDef:
    __tablename__ = 'arXiv_archive_def'
    __sa_dataclass_metadata_key__ = 'sa'

    archive: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, server_default=text("''"))})
    name: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})


@mapper_registry.mapped
@dataclass
class ArXivArchiveGroup:
    __tablename__ = 'arXiv_archive_group'
    __sa_dataclass_metadata_key__ = 'sa'

    archive_id: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, nullable=False, server_default=text("''"))})
    group_id: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, nullable=False, server_default=text("''"))})


@mapper_registry.mapped
@dataclass
class ArXivAwsConfig:
    __tablename__ = 'arXiv_aws_config'
    __sa_dataclass_metadata_key__ = 'sa'

    domain: str = field(init=False, metadata={'sa': Column(String(75), primary_key=True, nullable=False)})
    keyname: str = field(init=False, metadata={'sa': Column(String(60), primary_key=True, nullable=False)})
    value: Optional[str] = field(default=None, metadata={'sa': Column(String(150))})


@mapper_registry.mapped
@dataclass
class ArXivAwsFiles:
    __tablename__ = 'arXiv_aws_files'
    __table_args__ = (
        Index('idx_2_type', 'type'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    type: str = field(metadata={'sa': Column(String(10), nullable=False, server_default=text("''"))})
    filename: str = field(init=False, metadata={'sa': Column(String(100), primary_key=True, server_default=text("''"))})
    md5sum: Optional[str] = field(default=None, metadata={'sa': Column(String(50))})
    content_md5sum: Optional[str] = field(default=None, metadata={'sa': Column(String(50))})
    size: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    timestamp: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    yymm: Optional[str] = field(default=None, metadata={'sa': Column(String(4))})
    seq_num: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    first_item: Optional[str] = field(default=None, metadata={'sa': Column(String(20))})
    last_item: Optional[str] = field(default=None, metadata={'sa': Column(String(20))})
    num_items: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})


@mapper_registry.mapped
@dataclass
class ArXivBibFeeds:
    __tablename__ = 'arXiv_bib_feeds'
    __sa_dataclass_metadata_key__ = 'sa'

    bib_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    name: str = field(metadata={'sa': Column(String(64), nullable=False, server_default=text("''"))})
    priority: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    strip_journal_ref: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    uri: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    identifier: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    version: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    concatenate_dupes: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    max_updates: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    email_errors: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    prune_ids: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    prune_regex: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    enabled: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})


@mapper_registry.mapped
@dataclass
class ArXivBibUpdates:
    __tablename__ = 'arXiv_bib_updates'
    __sa_dataclass_metadata_key__ = 'sa'

    update_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    bib_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    updated: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))})
    journal_ref: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    doi: Optional[str] = field(default=None, metadata={'sa': Column(Text)})


t_arXiv_black_email = Table(
    'arXiv_black_email', metadata,
    Column('pattern', String(64))
)


t_arXiv_block_email = Table(
    'arXiv_block_email', metadata,
    Column('pattern', String(64))
)


@mapper_registry.mapped
@dataclass
class ArXivBogusCountries:
    __tablename__ = 'arXiv_bogus_countries'
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    country_name: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})


@mapper_registry.mapped
@dataclass
class ArXivCategoryDef:
    __tablename__ = 'arXiv_category_def'
    __sa_dataclass_metadata_key__ = 'sa'

    category: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True)})
    name: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    active: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'1'"))})

    arXiv_document_category: List[ArXivDocumentCategory] = field(default_factory=list, metadata={'sa': relationship('ArXivDocumentCategory', back_populates='arXiv_category_def')})
    arXiv_submission_category: List[ArXivSubmissionCategory] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionCategory', back_populates='arXiv_category_def')})
    arXiv_submission_category_proposal: List[ArXivSubmissionCategoryProposal] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionCategoryProposal', back_populates='arXiv_category_def')})


@mapper_registry.mapped
@dataclass
class ArXivDblpAuthors:
    __tablename__ = 'arXiv_dblp_authors'
    __table_args__ = (
        Index('idx_3_author_id', 'author_id', unique=True),
        Index('idx_4_name', 'name', unique=True)
    )
    __sa_dataclass_metadata_key__ = 'sa'

    author_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    name: Optional[str] = field(default=None, metadata={'sa': Column(String(40))})

    arXiv_dblp_document_authors: List[ArXivDblpDocumentAuthors] = field(default_factory=list, metadata={'sa': relationship('ArXivDblpDocumentAuthors', back_populates='author')})


@mapper_registry.mapped
@dataclass
class ArXivEndorsementDomains:
    __tablename__ = 'arXiv_endorsement_domains'
    __sa_dataclass_metadata_key__ = 'sa'

    endorsement_domain: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, server_default=text("''"))})
    endorse_all: str = field(metadata={'sa': Column(Enum('y', 'n'), nullable=False, server_default=text("'n'"))})
    mods_endorse_all: str = field(metadata={'sa': Column(Enum('y', 'n'), nullable=False, server_default=text("'n'"))})
    endorse_email: str = field(metadata={'sa': Column(Enum('y', 'n'), nullable=False, server_default=text("'y'"))})
    papers_to_endorse: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'4'"))})

    arXiv_categories: List[ArXivCategories] = field(default_factory=list, metadata={'sa': relationship('ArXivCategories', back_populates='arXiv_endorsement_domains')})


@mapper_registry.mapped
@dataclass
class ArXivFreezeLog:
    __tablename__ = 'arXiv_freeze_log'
    __sa_dataclass_metadata_key__ = 'sa'

    date_: int = field(metadata={'sa': Column('date', Integer, primary_key=True, server_default=text("'0'"))})


@mapper_registry.mapped
@dataclass
class ArXivGroupDef:
    __tablename__ = 'arXiv_group_def'
    __sa_dataclass_metadata_key__ = 'sa'

    archive_group: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, server_default=text("''"))})
    name: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})


@mapper_registry.mapped
@dataclass
class ArXivGroups:
    __tablename__ = 'arXiv_groups'
    __sa_dataclass_metadata_key__ = 'sa'

    group_id: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, server_default=text("''"))})
    group_name: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    start_year: str = field(metadata={'sa': Column(String(4), nullable=False, server_default=text("''"))})

    arXiv_archives: List[ArXivArchives] = field(default_factory=list, metadata={'sa': relationship('ArXivArchives', back_populates='arXiv_groups')})


@mapper_registry.mapped
@dataclass
class ArXivLicenses:
    __tablename__ = 'arXiv_licenses'
    __sa_dataclass_metadata_key__ = 'sa'

    name: str = field(init=False, metadata={'sa': Column(String(255), primary_key=True)})
    label: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    active: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'1'"))})
    note: Optional[str] = field(default=None, metadata={'sa': Column(String(400))})
    sequence: Optional[int] = field(default=None, metadata={'sa': Column(SmallInteger)})

    arXiv_metadata: List[ArXivMetadata] = field(default_factory=list, metadata={'sa': relationship('ArXivMetadata', back_populates='arXiv_licenses')})
    arXiv_submissions: List[ArXivSubmissions] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_licenses')})


@mapper_registry.mapped
@dataclass
class ArXivLogPositions:
    __tablename__ = 'arXiv_log_positions'
    __sa_dataclass_metadata_key__ = 'sa'

    id: str = field(init=False, metadata={'sa': Column(String(255), primary_key=True, server_default=text("''"))})
    position: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    date_: Optional[int] = field(default=None, metadata={'sa': Column('date', Integer)})


@mapper_registry.mapped
@dataclass
class ArXivMonitorKlog:
    __tablename__ = 'arXiv_monitor_klog'
    __sa_dataclass_metadata_key__ = 'sa'

    t: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    sent: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})


@mapper_registry.mapped
@dataclass
class ArXivMonitorMailq:
    __tablename__ = 'arXiv_monitor_mailq'
    __sa_dataclass_metadata_key__ = 'sa'

    t: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    main_q: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    local_q: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    local_host_map: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    local_timeout: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    local_refused: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    local_in_flight: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})


@mapper_registry.mapped
@dataclass
class ArXivMonitorMailsent:
    __tablename__ = 'arXiv_monitor_mailsent'
    __sa_dataclass_metadata_key__ = 'sa'

    t: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    sent: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})


@mapper_registry.mapped
@dataclass
class ArXivNextMail:
    __tablename__ = 'arXiv_next_mail'
    __table_args__ = (
        Index('arXiv_next_mail_idx_document_id', 'document_id'),
        Index('arXiv_next_mail_idx_document_id_version', 'document_id', 'version')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    next_mail_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    submission_id: int = field(metadata={'sa': Column(Integer, nullable=False)})
    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    version: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    type: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("'new'"))})
    is_written: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    paper_id: Optional[str] = field(default=None, metadata={'sa': Column(String(20))})
    extra: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    mail_id: Optional[str] = field(default=None, metadata={'sa': Column(CHAR(6))})


@mapper_registry.mapped
@dataclass
class ArXivOrcidConfig:
    __tablename__ = 'arXiv_orcid_config'
    __sa_dataclass_metadata_key__ = 'sa'

    domain: str = field(init=False, metadata={'sa': Column(String(75), primary_key=True, nullable=False)})
    keyname: str = field(init=False, metadata={'sa': Column(String(60), primary_key=True, nullable=False)})
    value: Optional[str] = field(default=None, metadata={'sa': Column(String(150))})


t_arXiv_ownership_requests_papers = Table(
    'arXiv_ownership_requests_papers', metadata,
    Column('request_id', Integer, nullable=False, server_default=text("'0'")),
    Column('document_id', Integer, nullable=False, server_default=text("'0'")),
    Index('idx_5_document_id', 'document_id'),
    Index('idx_6_request_id', 'request_id', 'document_id', unique=True)
)


@mapper_registry.mapped
@dataclass
class ArXivPaperSessions:
    __tablename__ = 'arXiv_paper_sessions'
    __sa_dataclass_metadata_key__ = 'sa'

    paper_session_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    paper_id: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    start_time: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    end_time: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    ip_name: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})


@mapper_registry.mapped
@dataclass
class ArXivPublishLog:
    __tablename__ = 'arXiv_publish_log'
    __sa_dataclass_metadata_key__ = 'sa'

    date_: int = field(metadata={'sa': Column('date', Integer, primary_key=True, server_default=text("'0'"))})


t_arXiv_refresh_list = Table(
    'arXiv_refresh_list', metadata,
    Column('filename', String(255)),
    Column('mtime', Integer),
    Index('arXiv_refresh_list_mtime', 'mtime')
)


@mapper_registry.mapped
@dataclass
class ArXivRejectSessionUsernames:
    __tablename__ = 'arXiv_reject_session_usernames'
    __sa_dataclass_metadata_key__ = 'sa'

    username: str = field(init=False, metadata={'sa': Column(String(64), primary_key=True, server_default=text("''"))})


@mapper_registry.mapped
@dataclass
class ArXivSciencewisePings:
    __tablename__ = 'arXiv_sciencewise_pings'
    __sa_dataclass_metadata_key__ = 'sa'

    paper_id_v: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True)})
    updated: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})


@mapper_registry.mapped
@dataclass
class ArXivState:
    __tablename__ = 'arXiv_state'
    __sa_dataclass_metadata_key__ = 'sa'

    id: int = field(metadata={'sa': Column(Integer, primary_key=True)})
    name: Optional[str] = field(default=None, metadata={'sa': Column(String(24))})
    value: Optional[str] = field(default=None, metadata={'sa': Column(String(24))})


t_arXiv_stats_hourly = Table(
    'arXiv_stats_hourly', metadata,
    Column('ymd', Date, nullable=False),
    Column('hour', SmallInteger, nullable=False),
    Column('node_num', SmallInteger, nullable=False),
    Column('access_type', CHAR(1), nullable=False),
    Column('connections', Integer, nullable=False),
    Index('arXiv_stats_hourly_idx_access_type', 'access_type'),
    Index('arXiv_stats_hourly_idx_hour', 'hour'),
    Index('arXiv_stats_hourly_idx_node_num', 'node_num'),
    Index('arXiv_stats_hourly_idx_ymd', 'ymd')
)


@mapper_registry.mapped
@dataclass
class ArXivStatsMonthlyDownloads:
    __tablename__ = 'arXiv_stats_monthly_downloads'
    __sa_dataclass_metadata_key__ = 'sa'

    ym: date = field(init=False, metadata={'sa': Column(Date, primary_key=True)})
    downloads: int = field(metadata={'sa': Column(Integer, nullable=False)})


@mapper_registry.mapped
@dataclass
class ArXivStatsMonthlySubmissions:
    __tablename__ = 'arXiv_stats_monthly_submissions'
    __sa_dataclass_metadata_key__ = 'sa'

    ym: date = field(init=False, metadata={'sa': Column(Date, primary_key=True, server_default=text("'0000-00-00'"))})
    num_submissions: int = field(metadata={'sa': Column(SmallInteger, nullable=False)})
    historical_delta: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionAgreements:
    __tablename__ = 'arXiv_submission_agreements'
    __sa_dataclass_metadata_key__ = 'sa'

    agreement_id: int = field(init=False, metadata={'sa': Column(SmallInteger, primary_key=True)})
    commit_ref: str = field(metadata={'sa': Column(String(255), nullable=False)})
    effective_date: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))})
    content: Optional[str] = field(default=None, metadata={'sa': Column(Text)})

    arXiv_submissions: List[ArXivSubmissions] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissions', back_populates='agreement')})


@mapper_registry.mapped
@dataclass
class ArXivSubmitterFlags:
    __tablename__ = 'arXiv_submitter_flags'
    __sa_dataclass_metadata_key__ = 'sa'

    flag_id: int = field(metadata={'sa': Column(Integer, primary_key=True)})
    comment: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    pattern: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})


@mapper_registry.mapped
@dataclass
class ArXivSuspectEmails:
    __tablename__ = 'arXiv_suspect_emails'
    __sa_dataclass_metadata_key__ = 'sa'

    id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    type: str = field(metadata={'sa': Column(String(10), nullable=False)})
    pattern: str = field(metadata={'sa': Column(Text, nullable=False)})
    comment: str = field(metadata={'sa': Column(Text, nullable=False)})
    updated: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD)})


@mapper_registry.mapped
@dataclass
class ArXivTitles:
    __tablename__ = 'arXiv_titles'
    __table_args__ = (
        Index('arXiv_repno_idx', 'report_num'),
        Index('arXiv_titles_idx', 'title')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    paper_id: str = field(init=False, metadata={'sa': Column(String(64), primary_key=True)})
    title: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    report_num: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    date_: Optional[date] = field(default=None, metadata={'sa': Column('date', Date)})


@mapper_registry.mapped
@dataclass
class ArXivTrackbackPings:
    __tablename__ = 'arXiv_trackback_pings'
    __table_args__ = (
        Index('arXiv_trackback_pings__document_id', 'document_id'),
        Index('arXiv_trackback_pings__posted_date', 'posted_date'),
        Index('arXiv_trackback_pings__status', 'status'),
        Index('arXiv_trackback_pings__url', 'url')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    trackback_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    title: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    excerpt: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    url: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    blog_name: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    remote_addr: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    posted_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    is_stale: int = field(metadata={'sa': Column(Boolean, nullable=False, server_default=text("'0'"))})
    approved_by_user: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    approved_time: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    status: str = field(metadata={'sa': Column(Enum('pending', 'pending2', 'accepted', 'rejected', 'spam'), nullable=False, server_default=text("'pending'"))})
    document_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    site_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})


@mapper_registry.mapped
@dataclass
class ArXivTrackbackSites:
    __tablename__ = 'arXiv_trackback_sites'
    __table_args__ = (
        Index('arXiv_trackback_sites__pattern', 'pattern'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    pattern: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    site_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    action: str = field(metadata={'sa': Column(Enum('neutral', 'accept', 'reject', 'spam'), nullable=False, server_default=text("'neutral'"))})


@mapper_registry.mapped
@dataclass
class ArXivTracking:
    __tablename__ = 'arXiv_tracking'
    __table_args__ = (
        Index('idx_7_sword_id', 'sword_id', unique=True),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    tracking_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    sword_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'00000000'"))})
    paper_id: str = field(metadata={'sa': Column(String(32), nullable=False)})
    timestamp: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))})
    submission_errors: Optional[str] = field(default=None, metadata={'sa': Column(Text)})

    arXiv_submissions: List[ArXivSubmissions] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissions', back_populates='sword')})


t_arXiv_updates = Table(
    'arXiv_updates', metadata,
    Column('document_id', Integer),
    Column('version', Integer, nullable=False, server_default=text("'1'")),
    Column('date', Date),
    Column('action', Enum('new', 'replace', 'absonly', 'cross', 'repcro')),
    Column('archive', String(20)),
    Column('category', String(20)),
    Index('idx_8_archive_index', 'archive'),
    Index('idx_9_category_index', 'category'),
    Index('idx_10_date_index', 'date'),
    Index('idx_11_document_id', 'document_id', 'date', 'action', 'category', unique=True),
    Index('document_id_index', 'document_id')
)


t_arXiv_updates_tmp = Table(
    'arXiv_updates_tmp', metadata,
    Column('document_id', Integer),
    Column('date', Date),
    Column('action', Enum('new', 'replace', 'absonly', 'cross', 'repcro')),
    Column('category', String(20)),
    Index('idx_12_document_id', 'document_id', 'date', 'action', 'category', unique=True)
)


t_arXiv_white_email = Table(
    'arXiv_white_email', metadata,
    Column('pattern', String(64)),
    Index('uc_pattern', 'pattern', unique=True)
)


t_arXiv_xml_notifications = Table(
    'arXiv_xml_notifications', metadata,
    Column('control_id', Integer),
    Column('type', Enum('submission', 'cross', 'jref')),
    Column('queued_date', Integer, nullable=False, server_default=text("'0'")),
    Column('sent_date', Integer, nullable=False, server_default=text("'0'")),
    Column('status', Enum('unsent', 'sent', 'failed')),
    Index('idx_13_control_id', 'control_id'),
    Index('idx_14_status', 'status')
)


@mapper_registry.mapped
@dataclass
class DbixClassSchemaVersions:
    __tablename__ = 'dbix_class_schema_versions'
    __sa_dataclass_metadata_key__ = 'sa'

    version: str = field(init=False, metadata={'sa': Column(String(10), primary_key=True)})
    installed: str = field(metadata={'sa': Column(String(20), nullable=False)})


t_demographics_backup = Table(
    'demographics_backup', metadata,
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    Column('country', CHAR(2), nullable=False, server_default=text("''")),
    Column('affiliation', String(255), nullable=False, server_default=text("''")),
    Column('url', String(255), nullable=False, server_default=text("''")),
    Column('type', SmallInteger),
    Column('os', SmallInteger),
    Column('archive', String(16)),
    Column('subject_class', String(16)),
    Column('original_subject_classes', String(255), nullable=False, server_default=text("''")),
    Column('flag_group_physics', Integer),
    Column('flag_group_math', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_group_cs', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_group_nlin', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_proxy', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_journal', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_xml', Integer, nullable=False, server_default=text("'0'")),
    Column('dirty', Integer, nullable=False, server_default=text("'2'")),
    Column('flag_group_test', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_suspect', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_group_q_bio', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_no_upload', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_no_endorse', Integer, nullable=False, server_default=text("'0'")),
    Column('veto_status', Enum('ok', 'no-endorse', 'no-upload'), server_default=text("'ok'"))
)


@mapper_registry.mapped
@dataclass
class Sessions:
    __tablename__ = 'sessions'
    __sa_dataclass_metadata_key__ = 'sa'

    id: str = field(init=False, metadata={'sa': Column(CHAR(72), primary_key=True)})
    session_data: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    expires: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})


@mapper_registry.mapped
@dataclass
class TapirCountries:
    __tablename__ = 'tapir_countries'
    __sa_dataclass_metadata_key__ = 'sa'

    digraph: str = field(init=False, metadata={'sa': Column(CHAR(2), primary_key=True, server_default=text("''"))})
    country_name: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    rank: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'255'"))})

    tapir_address: List[TapirAddress] = field(default_factory=list, metadata={'sa': relationship('TapirAddress', back_populates='tapir_countries')})
    tapir_demographics: List[TapirDemographics] = field(default_factory=list, metadata={'sa': relationship('TapirDemographics', back_populates='tapir_countries')})


@mapper_registry.mapped
@dataclass
class TapirEmailLog:
    __tablename__ = 'tapir_email_log'
    __table_args__ = (
        Index('idx_15_mailing_id', 'mailing_id'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    mail_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    sent_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    template_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    reference_type: Optional[str] = field(default=None, metadata={'sa': Column(CHAR(1))})
    reference_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    email: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    flag_bounced: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    mailing_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})


t_tapir_error_log = Table(
    'tapir_error_log', metadata,
    Column('error_date', Integer, nullable=False, server_default=text("'0'")),
    Column('user_id', Integer),
    Column('session_id', Integer),
    Column('ip_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(32), nullable=False, server_default=text("''")),
    Column('message', String(32), nullable=False, server_default=text("''")),
    Column('url', String(255), nullable=False, server_default=text("''")),
    Column('error_url', String(255), nullable=False, server_default=text("''")),
    Index('idx_16_error_date', 'error_date'),
    Index('idx_17_ip_addr', 'ip_addr'),
    Index('idx_18_message', 'message'),
    Index('idx_19_session_id', 'session_id'),
    Index('idx_20_tracking_cookie', 'tracking_cookie'),
    Index('idx_21_user_id', 'user_id')
)


@mapper_registry.mapped
@dataclass
class TapirIntegerVariables:
    __tablename__ = 'tapir_integer_variables'
    __sa_dataclass_metadata_key__ = 'sa'

    variable_id: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, server_default=text("''"))})
    value: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})


@mapper_registry.mapped
@dataclass
class TapirNicknamesAudit:
    __tablename__ = 'tapir_nicknames_audit'
    __table_args__ = (
        Index('idx_22_creation_date', 'creation_date'),
        Index('idx_23_creation_ip_num', 'creation_ip_num'),
        Index('idx_24_tracking_cookie', 'tracking_cookie')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    nick_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    creation_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    creation_ip_num: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})


t_tapir_no_cookies = Table(
    'tapir_no_cookies', metadata,
    Column('log_date', Integer, nullable=False, server_default=text("'0'")),
    Column('ip_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('session_data', String(255), nullable=False, server_default=text("''")),
    Column('user_agent', String(255), nullable=False, server_default=text("''"))
)


t_tapir_periodic_tasks_log = Table(
    'tapir_periodic_tasks_log', metadata,
    Column('t', Integer, nullable=False, server_default=text("'0'")),
    Column('entry', Text),
    Index('tapir_periodic_tasks_log_1', 't')
)


@mapper_registry.mapped
@dataclass
class TapirPolicyClasses:
    __tablename__ = 'tapir_policy_classes'
    __sa_dataclass_metadata_key__ = 'sa'

    class_id: int = field(init=False, metadata={'sa': Column(SmallInteger, primary_key=True)})
    name: str = field(metadata={'sa': Column(String(64), nullable=False, server_default=text("''"))})
    description: str = field(metadata={'sa': Column(Text, nullable=False)})
    password_storage: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    recovery_policy: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    permanent_login: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    tapir_users: List[TapirUsers] = field(default_factory=list, metadata={'sa': relationship('TapirUsers', back_populates='tapir_policy_classes')})


@mapper_registry.mapped
@dataclass
class TapirPresessions:
    __tablename__ = 'tapir_presessions'
    __sa_dataclass_metadata_key__ = 'sa'

    presession_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    ip_num: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    created_at: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})


@mapper_registry.mapped
@dataclass
class TapirStringVariables:
    __tablename__ = 'tapir_string_variables'
    __sa_dataclass_metadata_key__ = 'sa'

    variable_id: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, server_default=text("''"))})
    value: str = field(metadata={'sa': Column(Text, nullable=False)})


@mapper_registry.mapped
@dataclass
class TapirStrings:
    __tablename__ = 'tapir_strings'
    __sa_dataclass_metadata_key__ = 'sa'

    name: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    module: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    language: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("'en'"))})
    string: str = field(metadata={'sa': Column(Text, nullable=False)})


@mapper_registry.mapped
@dataclass
class SubscriptionUniversalInstitutionContact:
    __tablename__ = 'Subscription_UniversalInstitutionContact'
    __table_args__ = (
        ForeignKeyConstraint(['sid'], ['Subscription_UniversalInstitution.id'], ondelete='CASCADE', name='Subscription_Institution_Contact_Universal'),
        Index('idx_25_sid', 'sid')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    sid: int = field(metadata={'sa': Column(Integer, nullable=False)})
    id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    email: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    active: Optional[int] = field(default=None, metadata={'sa': Column(Boolean, server_default=text("'0'"))})
    contact_name: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    phone: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    note: Optional[str] = field(default=None, metadata={'sa': Column(String(2048))})

    Subscription_UniversalInstitution: Optional[SubscriptionUniversalInstitution] = field(default=None, metadata={'sa': relationship('SubscriptionUniversalInstitution', back_populates='Subscription_UniversalInstitutionContact')})


@mapper_registry.mapped
@dataclass
class SubscriptionUniversalInstitutionIP:
    __tablename__ = 'Subscription_UniversalInstitutionIP'
    __table_args__ = (
        ForeignKeyConstraint(['sid'], ['Subscription_UniversalInstitution.id'], ondelete='CASCADE', name='Subscription_Institution_IP_Universal'),
        Index('idx_26_end', 'end'),
        Index('idx_27_ip', 'start', 'end'),
        Index('idx_28_sid', 'sid'),
        Index('idx_29_start', 'start')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    sid: int = field(metadata={'sa': Column(Integer, nullable=False)})
    id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    end: int = field(metadata={'sa': Column(BigInteger, nullable=False)})
    start: int = field(metadata={'sa': Column(BigInteger, nullable=False)})
    exclude: Optional[int] = field(default=None, metadata={'sa': Column(Boolean, server_default=text("'0'"))})

    Subscription_UniversalInstitution: Optional[SubscriptionUniversalInstitution] = field(default=None, metadata={'sa': relationship('SubscriptionUniversalInstitution', back_populates='Subscription_UniversalInstitutionIP')})


@mapper_registry.mapped
@dataclass
class ArXivArchives:
    __tablename__ = 'arXiv_archives'
    __table_args__ = (
        ForeignKeyConstraint(['in_group'], ['arXiv_groups.group_id'], name='0_576'),
        Index('idx_30_in_group', 'in_group')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    archive_id: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, server_default=text("''"))})
    in_group: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    archive_name: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    start_date: str = field(metadata={'sa': Column(String(4), nullable=False, server_default=text("''"))})
    end_date: str = field(metadata={'sa': Column(String(4), nullable=False, server_default=text("''"))})
    subdivided: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    arXiv_groups: Optional[ArXivGroups] = field(default=None, metadata={'sa': relationship('ArXivGroups', back_populates='arXiv_archives')})
    arXiv_categories: List[ArXivCategories] = field(default_factory=list, metadata={'sa': relationship('ArXivCategories', back_populates='arXiv_archives')})


t_tapir_save_post_variables = Table(
    'tapir_save_post_variables', metadata,
    Column('presession_id', Integer, nullable=False, server_default=text("'0'")),
    Column('name', String(255)),
    Column('value', Text, nullable=False),
    Column('seq', Integer, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['presession_id'], ['tapir_presessions.presession_id'], name='0_558'),
    Index('idx_31_presession_id', 'presession_id')
)


@mapper_registry.mapped
@dataclass
class TapirUsers:
    __tablename__ = 'tapir_users'
    __table_args__ = (
        ForeignKeyConstraint(['policy_class'], ['tapir_policy_classes.class_id'], name='0_510'),
        Index('idx_32_email', 'email', unique=True),
        Index('idx_33_first_name', 'first_name'),
        Index('idx_34_flag_approved', 'flag_approved'),
        Index('idx_35_flag_banned', 'flag_banned'),
        Index('idx_36_flag_can_lock', 'flag_can_lock'),
        Index('idx_37_flag_deleted', 'flag_deleted'),
        Index('idx_38_flag_edit_users', 'flag_edit_users'),
        Index('idx_39_flag_internal', 'flag_internal'),
        Index('idx_40_joined_date', 'joined_date'),
        Index('idx_41_joined_ip_num', 'joined_ip_num'),
        Index('idx_42_last_name', 'last_name'),
        Index('idx_43_policy_class', 'policy_class'),
        Index('idx_44_tracking_cookie', 'tracking_cookie')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    share_first_name: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    share_last_name: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    email: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    share_email: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'8'"))})
    email_bouncing: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    policy_class: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    joined_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    joined_remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    flag_internal: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_edit_users: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_edit_system: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_email_verified: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_approved: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    flag_deleted: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_banned: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_wants_email: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_html_email: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    flag_allow_tex_produced: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_can_lock: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    first_name: Optional[str] = field(default=None, metadata={'sa': Column(String(50))})
    last_name: Optional[str] = field(default=None, metadata={'sa': Column(String(50))})
    suffix_name: Optional[str] = field(default=None, metadata={'sa': Column(String(50))})
    joined_ip_num: Optional[str] = field(default=None, metadata={'sa': Column(String(16))})

    tapir_policy_classes: Optional[TapirPolicyClasses] = field(default=None, metadata={'sa': relationship('TapirPolicyClasses', back_populates='tapir_users')})
    arXiv_author_ids: Optional[ArXivAuthorIds] = field(default=None, metadata={'sa': relationship('ArXivAuthorIds', uselist=False, back_populates='user')})
    arXiv_control_holds: List[ArXivControlHolds] = field(default_factory=list, metadata={'sa': relationship('ArXivControlHolds', foreign_keys='[ArXivControlHolds.last_changed_by]', back_populates='tapir_users')})
    arXiv_control_holds_: List[ArXivControlHolds] = field(default_factory=list, metadata={'sa': relationship('ArXivControlHolds', foreign_keys='[ArXivControlHolds.placed_by]', back_populates='tapir_users_')})
    arXiv_documents: List[ArXivDocuments] = field(default_factory=list, metadata={'sa': relationship('ArXivDocuments', back_populates='submitter')})
    arXiv_moderator_api_key: List[ArXivModeratorApiKey] = field(default_factory=list, metadata={'sa': relationship('ArXivModeratorApiKey', back_populates='user')})
    arXiv_orcid_ids: Optional[ArXivOrcidIds] = field(default=None, metadata={'sa': relationship('ArXivOrcidIds', uselist=False, back_populates='user')})
    arXiv_queue_view: Optional[ArXivQueueView] = field(default=None, metadata={'sa': relationship('ArXivQueueView', uselist=False, back_populates='user')})
    arXiv_suspicious_names: Optional[ArXivSuspiciousNames] = field(default=None, metadata={'sa': relationship('ArXivSuspiciousNames', uselist=False, back_populates='user')})
    arXiv_sword_licenses: Optional[ArXivSwordLicenses] = field(default=None, metadata={'sa': relationship('ArXivSwordLicenses', uselist=False, back_populates='user')})
    tapir_address: List[TapirAddress] = field(default_factory=list, metadata={'sa': relationship('TapirAddress', back_populates='user')})
    tapir_demographics: Optional[TapirDemographics] = field(default=None, metadata={'sa': relationship('TapirDemographics', uselist=False, back_populates='user')})
    tapir_email_change_tokens: List[TapirEmailChangeTokens] = field(default_factory=list, metadata={'sa': relationship('TapirEmailChangeTokens', back_populates='user')})
    tapir_email_templates: List[TapirEmailTemplates] = field(default_factory=list, metadata={'sa': relationship('TapirEmailTemplates', foreign_keys='[TapirEmailTemplates.created_by]', back_populates='tapir_users')})
    tapir_email_templates_: List[TapirEmailTemplates] = field(default_factory=list, metadata={'sa': relationship('TapirEmailTemplates', foreign_keys='[TapirEmailTemplates.updated_by]', back_populates='tapir_users_')})
    tapir_email_tokens: List[TapirEmailTokens] = field(default_factory=list, metadata={'sa': relationship('TapirEmailTokens', back_populates='user')})
    tapir_nicknames: List[TapirNicknames] = field(default_factory=list, metadata={'sa': relationship('TapirNicknames', back_populates='user')})
    tapir_phone: List[TapirPhone] = field(default_factory=list, metadata={'sa': relationship('TapirPhone', back_populates='user')})
    tapir_recovery_tokens: List[TapirRecoveryTokens] = field(default_factory=list, metadata={'sa': relationship('TapirRecoveryTokens', back_populates='user')})
    tapir_sessions: List[TapirSessions] = field(default_factory=list, metadata={'sa': relationship('TapirSessions', back_populates='user')})
    tapir_users_hot: Optional[TapirUsersHot] = field(default=None, metadata={'sa': relationship('TapirUsersHot', uselist=False, back_populates='user')})
    tapir_users_password: Optional[TapirUsersPassword] = field(default=None, metadata={'sa': relationship('TapirUsersPassword', uselist=False, back_populates='user')})
    arXiv_cross_control: List[ArXivCrossControl] = field(default_factory=list, metadata={'sa': relationship('ArXivCrossControl', back_populates='user')})
    arXiv_demographics: Optional[ArXivDemographics] = field(default=None, metadata={'sa': relationship('ArXivDemographics', uselist=False, back_populates='user')})
    arXiv_endorsement_requests: List[ArXivEndorsementRequests] = field(default_factory=list, metadata={'sa': relationship('ArXivEndorsementRequests', back_populates='endorsee')})
    arXiv_jref_control: List[ArXivJrefControl] = field(default_factory=list, metadata={'sa': relationship('ArXivJrefControl', back_populates='user')})
    arXiv_metadata: List[ArXivMetadata] = field(default_factory=list, metadata={'sa': relationship('ArXivMetadata', back_populates='submitter')})
    arXiv_show_email_requests: List[ArXivShowEmailRequests] = field(default_factory=list, metadata={'sa': relationship('ArXivShowEmailRequests', back_populates='user')})
    arXiv_submission_control: List[ArXivSubmissionControl] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionControl', back_populates='user')})
    arXiv_submissions: List[ArXivSubmissions] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissions', back_populates='submitter')})
    tapir_admin_audit: List[TapirAdminAudit] = field(default_factory=list, metadata={'sa': relationship('TapirAdminAudit', foreign_keys='[TapirAdminAudit.admin_user]', back_populates='tapir_users')})
    tapir_admin_audit_: List[TapirAdminAudit] = field(default_factory=list, metadata={'sa': relationship('TapirAdminAudit', foreign_keys='[TapirAdminAudit.affected_user]', back_populates='tapir_users_')})
    tapir_email_mailings: List[TapirEmailMailings] = field(default_factory=list, metadata={'sa': relationship('TapirEmailMailings', foreign_keys='[TapirEmailMailings.created_by]', back_populates='tapir_users')})
    tapir_email_mailings_: List[TapirEmailMailings] = field(default_factory=list, metadata={'sa': relationship('TapirEmailMailings', foreign_keys='[TapirEmailMailings.sent_by]', back_populates='tapir_users_')})
    tapir_permanent_tokens: List[TapirPermanentTokens] = field(default_factory=list, metadata={'sa': relationship('TapirPermanentTokens', back_populates='user')})
    tapir_recovery_tokens_used: List[TapirRecoveryTokensUsed] = field(default_factory=list, metadata={'sa': relationship('TapirRecoveryTokensUsed', back_populates='user')})
    arXiv_endorsements: List[ArXivEndorsements] = field(default_factory=list, metadata={'sa': relationship('ArXivEndorsements', foreign_keys='[ArXivEndorsements.endorsee_id]', back_populates='endorsee')})
    arXiv_endorsements_: List[ArXivEndorsements] = field(default_factory=list, metadata={'sa': relationship('ArXivEndorsements', foreign_keys='[ArXivEndorsements.endorser_id]', back_populates='endorser')})
    arXiv_ownership_requests: List[ArXivOwnershipRequests] = field(default_factory=list, metadata={'sa': relationship('ArXivOwnershipRequests', back_populates='user')})
    arXiv_submission_category_proposal: List[ArXivSubmissionCategoryProposal] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionCategoryProposal', back_populates='user')})
    arXiv_submission_flag: List[ArXivSubmissionFlag] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionFlag', back_populates='user')})
    arXiv_submission_hold_reason: List[ArXivSubmissionHoldReason] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionHoldReason', back_populates='user')})
    arXiv_submission_view_flag: List[ArXivSubmissionViewFlag] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionViewFlag', back_populates='user')})


@mapper_registry.mapped
@dataclass
class ArXivAuthorIds:
    __tablename__ = 'arXiv_author_ids'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_author_ids_ibfk_1'),
        Index('idx_45_author_id', 'author_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True)})
    author_id: str = field(metadata={'sa': Column(String(50), nullable=False)})
    updated: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_author_ids')})


t_arXiv_bad_pw = Table(
    'arXiv_bad_pw', metadata,
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_601'),
    Index('idx_46_user_id', 'user_id')
)


@mapper_registry.mapped
@dataclass
class ArXivCategories:
    __tablename__ = 'arXiv_categories'
    __table_args__ = (
        ForeignKeyConstraint(['archive'], ['arXiv_archives.archive_id'], name='0_578'),
        ForeignKeyConstraint(['endorsement_domain'], ['arXiv_endorsement_domains.endorsement_domain'], name='0_753'),
        Index('idx_47_endorsement_domain', 'endorsement_domain')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    archive: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, nullable=False, server_default=text("''"))})
    subject_class: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, nullable=False, server_default=text("''"))})
    definitive: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    active: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    endorse_all: str = field(metadata={'sa': Column(Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'"))})
    endorse_email: str = field(metadata={'sa': Column(Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'"))})
    papers_to_endorse: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    category_name: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    endorsement_domain: Optional[str] = field(default=None, metadata={'sa': Column(String(32))})

    arXiv_archives: Optional[ArXivArchives] = field(default=None, metadata={'sa': relationship('ArXivArchives', back_populates='arXiv_categories')})
    arXiv_endorsement_domains: Optional[ArXivEndorsementDomains] = field(default=None, metadata={'sa': relationship('ArXivEndorsementDomains', back_populates='arXiv_categories')})
    arXiv_cross_control: List[ArXivCrossControl] = field(default_factory=list, metadata={'sa': relationship('ArXivCrossControl', back_populates='arXiv_categories')})
    arXiv_demographics: List[ArXivDemographics] = field(default_factory=list, metadata={'sa': relationship('ArXivDemographics', back_populates='arXiv_categories')})
    arXiv_endorsement_requests: List[ArXivEndorsementRequests] = field(default_factory=list, metadata={'sa': relationship('ArXivEndorsementRequests', back_populates='arXiv_categories')})
    arXiv_questionable_categories: Optional[ArXivQuestionableCategories] = field(default=None, metadata={'sa': relationship('ArXivQuestionableCategories', uselist=False, back_populates='arXiv_categories')})
    arXiv_endorsements: List[ArXivEndorsements] = field(default_factory=list, metadata={'sa': relationship('ArXivEndorsements', back_populates='arXiv_categories')})


@mapper_registry.mapped
@dataclass
class ArXivControlHolds:
    __tablename__ = 'arXiv_control_holds'
    __table_args__ = (
        ForeignKeyConstraint(['last_changed_by'], ['tapir_users.user_id'], name='arXiv_control_holds_ibfk_2'),
        ForeignKeyConstraint(['placed_by'], ['tapir_users.user_id'], name='arXiv_control_holds_ibfk_1'),
        Index('idx_48_control_id', 'control_id', 'hold_type', unique=True),
        Index('idx_49_hold_reason', 'hold_reason'),
        Index('idx_50_hold_status', 'hold_status'),
        Index('idx_51_hold_type', 'hold_type'),
        Index('idx_52_last_changed_by', 'last_changed_by'),
        Index('idx_53_origin', 'origin'),
        Index('idx_54_placed_by', 'placed_by')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    hold_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    control_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    hold_type: str = field(metadata={'sa': Column(Enum('submission', 'cross', 'jref'), nullable=False, server_default=text("'submission'"))})
    hold_status: str = field(metadata={'sa': Column(Enum('held', 'extended', 'accepted', 'rejected'), nullable=False, server_default=text("'held'"))})
    hold_reason: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    hold_data: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    origin: str = field(metadata={'sa': Column(Enum('auto', 'user', 'admin', 'moderator'), nullable=False, server_default=text("'auto'"))})
    placed_by: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    last_changed_by: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})

    tapir_users: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[last_changed_by], back_populates='arXiv_control_holds')})
    tapir_users_: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[placed_by], back_populates='arXiv_control_holds_')})


@mapper_registry.mapped
@dataclass
class ArXivDocuments:
    __tablename__ = 'arXiv_documents'
    __table_args__ = (
        ForeignKeyConstraint(['submitter_id'], ['tapir_users.user_id'], name='0_580'),
        Index('idx_55_dated', 'dated'),
        Index('idx_56_paper_id', 'paper_id', unique=True),
        Index('idx_57_submitter_email', 'submitter_email'),
        Index('idx_58_submitter_id', 'submitter_id'),
        Index('idx_59_title', 'title')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    document_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    paper_id: str = field(metadata={'sa': Column(String(20), nullable=False, server_default=text("''"))})
    title: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    submitter_email: str = field(metadata={'sa': Column(String(64), nullable=False, server_default=text("''"))})
    dated: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    authors: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    submitter_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    primary_subject_class: Optional[str] = field(default=None, metadata={'sa': Column(String(16))})
    created: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})

    submitter: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_documents')})
    arXiv_admin_metadata: List[ArXivAdminMetadata] = field(default_factory=list, metadata={'sa': relationship('ArXivAdminMetadata', back_populates='document')})
    arXiv_cross_control: List[ArXivCrossControl] = field(default_factory=list, metadata={'sa': relationship('ArXivCrossControl', back_populates='document')})
    arXiv_dblp: Optional[ArXivDblp] = field(default=None, metadata={'sa': relationship('ArXivDblp', uselist=False, back_populates='document')})
    arXiv_dblp_document_authors: List[ArXivDblpDocumentAuthors] = field(default_factory=list, metadata={'sa': relationship('ArXivDblpDocumentAuthors', back_populates='document')})
    arXiv_document_category: List[ArXivDocumentCategory] = field(default_factory=list, metadata={'sa': relationship('ArXivDocumentCategory', back_populates='document')})
    arXiv_jref_control: List[ArXivJrefControl] = field(default_factory=list, metadata={'sa': relationship('ArXivJrefControl', back_populates='document')})
    arXiv_metadata: List[ArXivMetadata] = field(default_factory=list, metadata={'sa': relationship('ArXivMetadata', back_populates='document')})
    arXiv_mirror_list: List[ArXivMirrorList] = field(default_factory=list, metadata={'sa': relationship('ArXivMirrorList', back_populates='document')})
    arXiv_paper_pw: Optional[ArXivPaperPw] = field(default=None, metadata={'sa': relationship('ArXivPaperPw', uselist=False, back_populates='document')})
    arXiv_show_email_requests: List[ArXivShowEmailRequests] = field(default_factory=list, metadata={'sa': relationship('ArXivShowEmailRequests', back_populates='document')})
    arXiv_submission_control: List[ArXivSubmissionControl] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionControl', back_populates='document')})
    arXiv_submissions: List[ArXivSubmissions] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissions', back_populates='document')})
    arXiv_top_papers: List[ArXivTopPapers] = field(default_factory=list, metadata={'sa': relationship('ArXivTopPapers', back_populates='document')})
    arXiv_versions: List[ArXivVersions] = field(default_factory=list, metadata={'sa': relationship('ArXivVersions', back_populates='document')})


t_arXiv_duplicates = Table(
    'arXiv_duplicates', metadata,
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    Column('email', String(255)),
    Column('username', String(255)),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_599'),
    Index('idx_60_user_id', 'user_id')
)


@mapper_registry.mapped
@dataclass
class ArXivModeratorApiKey:
    __tablename__ = 'arXiv_moderator_api_key'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_moderator_api_key_ibfk_1'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    secret: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    valid: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    issued_when: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    issued_to: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_moderator_api_key')})


@mapper_registry.mapped
@dataclass
class ArXivOrcidIds:
    __tablename__ = 'arXiv_orcid_ids'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_orcid_ids_ibfk_1'),
        Index('idx_61_orcid', 'orcid')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True)})
    orcid: str = field(metadata={'sa': Column(String(19), nullable=False)})
    authenticated: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    updated: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_orcid_ids')})


@mapper_registry.mapped
@dataclass
class ArXivQueueView:
    __tablename__ = 'arXiv_queue_view'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_queue_view_ibfk_1'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    total_views: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    last_view: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    second_last_view: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_queue_view')})


@mapper_registry.mapped
@dataclass
class ArXivSuspiciousNames:
    __tablename__ = 'arXiv_suspicious_names'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_606'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    full_name: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_suspicious_names')})


@mapper_registry.mapped
@dataclass
class ArXivSwordLicenses:
    __tablename__ = 'arXiv_sword_licenses'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='user_id_fk'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True)})
    updated: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD)})
    license: Optional[str] = field(default=None, metadata={'sa': Column(String(127))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_sword_licenses')})


@mapper_registry.mapped
@dataclass
class TapirAddress:
    __tablename__ = 'tapir_address'
    __table_args__ = (
        ForeignKeyConstraint(['country'], ['tapir_countries.digraph'], name='0_523'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_522'),
        Index('idx_62_address_type', 'address_type'),
        Index('idx_63_city', 'city'),
        Index('idx_64_country', 'country'),
        Index('idx_65_postal_code', 'postal_code')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    address_type: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    company: str = field(metadata={'sa': Column(String(80), nullable=False, server_default=text("''"))})
    line1: str = field(metadata={'sa': Column(String(80), nullable=False, server_default=text("''"))})
    line2: str = field(metadata={'sa': Column(String(80), nullable=False, server_default=text("''"))})
    city: str = field(metadata={'sa': Column(String(50), nullable=False, server_default=text("''"))})
    state: str = field(metadata={'sa': Column(String(50), nullable=False, server_default=text("''"))})
    postal_code: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    country: str = field(metadata={'sa': Column(CHAR(2), nullable=False, server_default=text("''"))})
    share_addr: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    tapir_countries: Optional[TapirCountries] = field(default=None, metadata={'sa': relationship('TapirCountries', back_populates='tapir_address')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_address')})


@mapper_registry.mapped
@dataclass
class TapirDemographics:
    __tablename__ = 'tapir_demographics'
    __table_args__ = (
        ForeignKeyConstraint(['country'], ['tapir_countries.digraph'], name='0_518'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_517'),
        Index('idx_66_birthday', 'birthday'),
        Index('idx_67_country', 'country'),
        Index('idx_68_postal_code', 'postal_code')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    gender: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    share_gender: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'16'"))})
    share_birthday: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'16'"))})
    country: str = field(metadata={'sa': Column(CHAR(2), nullable=False, server_default=text("''"))})
    share_country: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'16'"))})
    postal_code: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    birthday: Optional[date] = field(default=None, metadata={'sa': Column(Date)})

    tapir_countries: Optional[TapirCountries] = field(default=None, metadata={'sa': relationship('TapirCountries', back_populates='tapir_demographics')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_demographics')})


@mapper_registry.mapped
@dataclass
class TapirEmailChangeTokens:
    __tablename__ = 'tapir_email_change_tokens'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_535'),
        Index('idx_69_secret', 'secret')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    secret: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    tapir_dest: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    issued_when: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    issued_to: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    used: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    session_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    old_email: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    new_email: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    consumed_when: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    consumed_from: Optional[str] = field(default=None, metadata={'sa': Column(String(16))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_email_change_tokens')})


@mapper_registry.mapped
@dataclass
class TapirEmailTemplates:
    __tablename__ = 'tapir_email_templates'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['tapir_users.user_id'], name='0_560'),
        ForeignKeyConstraint(['updated_by'], ['tapir_users.user_id'], name='0_561'),
        Index('idx_70_created_by', 'created_by'),
        Index('idx_71_short_name', 'short_name', 'lang', unique=True),
        Index('idx_72_update_date', 'update_date'),
        Index('idx_73_updated_by', 'updated_by')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    template_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    short_name: str = field(metadata={'sa': Column(String(32), nullable=False, server_default=text("''"))})
    lang: str = field(metadata={'sa': Column(CHAR(2), nullable=False, server_default=text("'en'"))})
    long_name: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    data: str = field(metadata={'sa': Column(Text, nullable=False)})
    sql_statement: str = field(metadata={'sa': Column(Text, nullable=False)})
    update_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    created_by: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    updated_by: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    workflow_status: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_system: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    tapir_users: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[created_by], back_populates='tapir_email_templates')})
    tapir_users_: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[updated_by], back_populates='tapir_email_templates_')})
    tapir_email_headers: List[TapirEmailHeaders] = field(default_factory=list, metadata={'sa': relationship('TapirEmailHeaders', back_populates='template')})
    tapir_email_mailings: List[TapirEmailMailings] = field(default_factory=list, metadata={'sa': relationship('TapirEmailMailings', back_populates='template')})


@mapper_registry.mapped
@dataclass
class TapirEmailTokens:
    __tablename__ = 'tapir_email_tokens'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_530'),
        Index('idx_74_secret', 'secret')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    secret: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    tapir_dest: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    issued_when: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    issued_to: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    wants_perm_token: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_email_tokens')})


@mapper_registry.mapped
@dataclass
class TapirNicknames:
    __tablename__ = 'tapir_nicknames'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_570'),
        Index('idx_75_flag_valid', 'flag_valid'),
        Index('idx_76_nickname', 'nickname', unique=True),
        Index('idx_77_policy', 'policy'),
        Index('idx_78_role', 'role'),
        Index('idx_79_user_id', 'user_id', 'user_seq', unique=True)
    )
    __sa_dataclass_metadata_key__ = 'sa'

    nick_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    nickname: str = field(metadata={'sa': Column(String(20), nullable=False, server_default=text("''"))})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    user_seq: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_valid: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    role: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    policy: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_primary: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_nicknames')})


@mapper_registry.mapped
@dataclass
class TapirPhone:
    __tablename__ = 'tapir_phone'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_520'),
        Index('idx_80_phone_number', 'phone_number'),
        Index('idx_81_phone_type', 'phone_type')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    phone_type: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    share_phone: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'16'"))})
    phone_number: Optional[str] = field(default=None, metadata={'sa': Column(String(32))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_phone')})


@mapper_registry.mapped
@dataclass
class TapirRecoveryTokens:
    __tablename__ = 'tapir_recovery_tokens'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_546'),
        Index('idx_82_secret', 'secret')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    secret: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    valid: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    tapir_dest: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    issued_when: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    issued_to: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_recovery_tokens')})


@mapper_registry.mapped
@dataclass
class TapirSessions:
    __tablename__ = 'tapir_sessions'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_525'),
        Index('idx_83_end_time', 'end_time'),
        Index('idx_84_start_time', 'start_time'),
        Index('idx_85_user_id', 'user_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    session_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    last_reissue: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    start_time: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    end_time: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_sessions')})
    tapir_admin_audit: List[TapirAdminAudit] = field(default_factory=list, metadata={'sa': relationship('TapirAdminAudit', back_populates='session')})
    tapir_permanent_tokens: List[TapirPermanentTokens] = field(default_factory=list, metadata={'sa': relationship('TapirPermanentTokens', back_populates='session')})
    tapir_recovery_tokens_used: List[TapirRecoveryTokensUsed] = field(default_factory=list, metadata={'sa': relationship('TapirRecoveryTokensUsed', back_populates='session')})
    tapir_sessions_audit: Optional[TapirSessionsAudit] = field(default=None, metadata={'sa': relationship('TapirSessionsAudit', uselist=False, back_populates='session')})


@mapper_registry.mapped
@dataclass
class TapirUsersHot:
    __tablename__ = 'tapir_users_hot'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_514'),
        Index('idx_86_last_login', 'last_login'),
        Index('idx_87_number_sessions', 'number_sessions'),
        Index('idx_88_second_last_login', 'second_last_login')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    last_login: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    second_last_login: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    number_sessions: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_users_hot')})


@mapper_registry.mapped
@dataclass
class TapirUsersPassword:
    __tablename__ = 'tapir_users_password'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_512'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    password_storage: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    password_enc: str = field(metadata={'sa': Column(String(50), nullable=False, server_default=text("''"))})

    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_users_password')})


@mapper_registry.mapped
@dataclass
class ArXivAdminMetadata:
    __tablename__ = 'arXiv_admin_metadata'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', name='meta_doc_fk'),
        Index('idx_89_document_id', 'document_id'),
        Index('idx_90_id', 'metadata_id'),
        Index('idx_91_pidv', 'paper_id', 'version', unique=True)
    )
    __sa_dataclass_metadata_key__ = 'sa'

    metadata_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    version: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    document_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    paper_id: Optional[str] = field(default=None, metadata={'sa': Column(String(64))})
    created: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    updated: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    submitter_name: Optional[str] = field(default=None, metadata={'sa': Column(String(64))})
    submitter_email: Optional[str] = field(default=None, metadata={'sa': Column(String(64))})
    history: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    source_size: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    source_type: Optional[str] = field(default=None, metadata={'sa': Column(String(12))})
    title: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    authors: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    category_string: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    comments: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    proxy: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    report_num: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    msc_class: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    acm_class: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    journal_ref: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    doi: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    abstract: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    license: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    modtime: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    is_current: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_admin_metadata')})


t_arXiv_bogus_subject_class = Table(
    'arXiv_bogus_subject_class', metadata,
    Column('document_id', Integer, nullable=False, server_default=text("'0'")),
    Column('category_name', String(255), nullable=False, server_default=text("''")),
    ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_604'),
    Index('idx_92_document_id', 'document_id')
)


@mapper_registry.mapped
@dataclass
class ArXivCrossControl:
    __tablename__ = 'arXiv_cross_control'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='arXiv_cross_control_ibfk_2'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_cross_control_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_cross_control_ibfk_3'),
        Index('idx_93_archive', 'archive', 'subject_class'),
        Index('idx_94_document_id', 'document_id', 'version'),
        Index('idx_95_freeze_date', 'freeze_date'),
        Index('idx_96_status', 'status'),
        Index('idx_97_user_id', 'user_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    control_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    version: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    desired_order: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    status: str = field(metadata={'sa': Column(Enum('new', 'frozen', 'published', 'rejected'), nullable=False, server_default=text("'new'"))})
    archive: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    subject_class: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    request_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    freeze_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    publish_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_must_notify: Optional[str] = field(default=None, metadata={'sa': Column(Enum('0', '1'), server_default=text("'1'"))})

    arXiv_categories: Optional[ArXivCategories] = field(default=None, metadata={'sa': relationship('ArXivCategories', back_populates='arXiv_cross_control')})
    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_cross_control')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_cross_control')})


@mapper_registry.mapped
@dataclass
class ArXivDblp:
    __tablename__ = 'arXiv_dblp'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_DBLP_cdfk1'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    document_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    url: Optional[str] = field(default=None, metadata={'sa': Column(String(80))})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_dblp')})


@mapper_registry.mapped
@dataclass
class ArXivDblpDocumentAuthors:
    __tablename__ = 'arXiv_dblp_document_authors'
    __table_args__ = (
        ForeignKeyConstraint(['author_id'], ['arXiv_dblp_authors.author_id'], name='arXiv_DBLP_ibfk2'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_DBLP_abfk1'),
        Index('idx_98_author_id', 'author_id'),
        Index('idx_99_document_id', 'document_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    document_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False)})
    author_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    position: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})

    author: Optional[ArXivDblpAuthors] = field(default=None, metadata={'sa': relationship('ArXivDblpAuthors', back_populates='arXiv_dblp_document_authors')})
    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_dblp_document_authors')})


@mapper_registry.mapped
@dataclass
class ArXivDemographics:
    __tablename__ = 'arXiv_demographics'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_588'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_587'),
        Index('idx_100_archive', 'archive', 'subject_class'),
        Index('idx_101_country', 'country'),
        Index('idx_102_flag_group_cs', 'flag_group_cs'),
        Index('idx_103_flag_group_econ', 'flag_group_econ'),
        Index('idx_104_flag_group_eess', 'flag_group_eess'),
        Index('idx_105_flag_group_math', 'flag_group_math'),
        Index('idx_106_flag_group_nlin', 'flag_group_nlin'),
        Index('idx_107_flag_group_physics', 'flag_group_physics'),
        Index('idx_108_flag_group_q_bio', 'flag_group_q_bio'),
        Index('idx_109_flag_group_q_fin', 'flag_group_q_fin'),
        Index('idx_110_flag_group_stat', 'flag_group_stat'),
        Index('idx_111_flag_journal', 'flag_journal'),
        Index('idx_112_flag_proxy', 'flag_proxy'),
        Index('idx_113_flag_suspect', 'flag_suspect'),
        Index('idx_114_flag_xml', 'flag_xml'),
        Index('idx_115_type', 'type')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    country: str = field(metadata={'sa': Column(CHAR(2), nullable=False, server_default=text("''"))})
    affiliation: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    url: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    original_subject_classes: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    flag_group_math: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_group_cs: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_group_nlin: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_proxy: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_journal: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_xml: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    dirty: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'2'"))})
    flag_group_test: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_suspect: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_group_q_bio: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_group_q_fin: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_group_stat: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_group_eess: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_group_econ: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    veto_status: str = field(metadata={'sa': Column(Enum('ok', 'no-endorse', 'no-upload', 'no-replace'), nullable=False, server_default=text("'ok'"))})
    type: Optional[int] = field(default=None, metadata={'sa': Column(SmallInteger)})
    archive: Optional[str] = field(default=None, metadata={'sa': Column(String(16))})
    subject_class: Optional[str] = field(default=None, metadata={'sa': Column(String(16))})
    flag_group_physics: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})

    arXiv_categories: Optional[ArXivCategories] = field(default=None, metadata={'sa': relationship('ArXivCategories', back_populates='arXiv_demographics')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_demographics')})


@mapper_registry.mapped
@dataclass
class ArXivDocumentCategory:
    __tablename__ = 'arXiv_document_category'
    __table_args__ = (
        ForeignKeyConstraint(['category'], ['arXiv_category_def.category'], name='doc_cat_cat'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', name='doc_cat_doc'),
        Index('idx_116_category', 'category'),
        Index('idx_117_document_id', 'document_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    document_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    category: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False)})
    is_primary: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})

    arXiv_category_def: Optional[ArXivCategoryDef] = field(default=None, metadata={'sa': relationship('ArXivCategoryDef', back_populates='arXiv_document_category')})
    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_document_category')})


@mapper_registry.mapped
@dataclass
class ArXivEndorsementRequests:
    __tablename__ = 'arXiv_endorsement_requests'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_723'),
        ForeignKeyConstraint(['endorsee_id'], ['tapir_users.user_id'], name='0_722'),
        Index('idx_118_archive', 'archive', 'subject_class'),
        Index('idx_119_endorsee_id', 'endorsee_id'),
        Index('idx_120_endorsee_id_2', 'endorsee_id', 'archive', 'subject_class', unique=True),
        Index('idx_121_secret', 'secret', unique=True)
    )
    __sa_dataclass_metadata_key__ = 'sa'

    request_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    endorsee_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    archive: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    subject_class: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    secret: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    flag_valid: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    issued_when: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    point_value: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    arXiv_categories: Optional[ArXivCategories] = field(default=None, metadata={'sa': relationship('ArXivCategories', back_populates='arXiv_endorsement_requests')})
    endorsee: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_endorsement_requests')})
    arXiv_endorsement_requests_audit: Optional[ArXivEndorsementRequestsAudit] = field(default=None, metadata={'sa': relationship('ArXivEndorsementRequestsAudit', uselist=False, back_populates='request')})
    arXiv_endorsements: List[ArXivEndorsements] = field(default_factory=list, metadata={'sa': relationship('ArXivEndorsements', back_populates='request')})
    arXiv_ownership_requests: List[ArXivOwnershipRequests] = field(default_factory=list, metadata={'sa': relationship('ArXivOwnershipRequests', back_populates='endorsement_request')})


t_arXiv_in_category = Table(
    'arXiv_in_category', metadata,
    Column('document_id', Integer, nullable=False, server_default=text("'0'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('is_primary', Boolean(), nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_583'),
    ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_582'),
    Index('arXiv_in_category_mp', 'archive', 'subject_class'),
    Index('idx_122_archive', 'archive', 'subject_class', 'document_id', unique=True),
    Index('idx_123_document_id', 'document_id')
)


@mapper_registry.mapped
@dataclass
class ArXivJrefControl:
    __tablename__ = 'arXiv_jref_control'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_jref_control_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_jref_control_ibfk_2'),
        Index('idx_124_document_id', 'document_id', 'version', unique=True),
        Index('idx_125_freeze_date', 'freeze_date'),
        Index('idx_126_status', 'status'),
        Index('idx_127_user_id', 'user_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    control_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    version: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    status: str = field(metadata={'sa': Column(Enum('new', 'frozen', 'published', 'rejected'), nullable=False, server_default=text("'new'"))})
    jref: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    request_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    freeze_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    publish_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_must_notify: Optional[str] = field(default=None, metadata={'sa': Column(Enum('0', '1'), server_default=text("'1'"))})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_jref_control')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_jref_control')})


@mapper_registry.mapped
@dataclass
class ArXivMetadata:
    __tablename__ = 'arXiv_metadata'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_metadata_fk_document_id'),
        ForeignKeyConstraint(['license'], ['arXiv_licenses.name'], name='arXiv_metadata_fk_license'),
        ForeignKeyConstraint(['submitter_id'], ['tapir_users.user_id'], name='arXiv_metadata_fk_submitter_id'),
        Index('idx_128_arXiv_metadata_idx_document_id', 'document_id'),
        Index('idx_129_arXiv_metadata_idx_license', 'license'),
        Index('idx_130_arXiv_metadata_idx_submitter_id', 'submitter_id'),
        Index('idx_131_pidv', 'paper_id', 'version', unique=True)
    )
    __sa_dataclass_metadata_key__ = 'sa'

    metadata_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    paper_id: str = field(metadata={'sa': Column(String(64), nullable=False)})
    submitter_name: str = field(metadata={'sa': Column(String(64), nullable=False)})
    submitter_email: str = field(metadata={'sa': Column(String(64), nullable=False)})
    version: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    is_withdrawn: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    created: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    updated: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    submitter_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    source_size: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    source_format: Optional[str] = field(default=None, metadata={'sa': Column(String(12))})
    source_flags: Optional[str] = field(default=None, metadata={'sa': Column(String(12))})
    title: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    authors: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    abs_categories: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    comments: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    proxy: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    report_num: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    msc_class: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    acm_class: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    journal_ref: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    doi: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    abstract: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    license: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    modtime: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    is_current: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'1'"))})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_metadata')})
    arXiv_licenses: Optional[ArXivLicenses] = field(default=None, metadata={'sa': relationship('ArXivLicenses', back_populates='arXiv_metadata')})
    submitter: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_metadata')})
    arXiv_datacite_dois: List[ArXivDataciteDois] = field(default_factory=list, metadata={'sa': relationship('ArXivDataciteDois', back_populates='metadata_')})


@mapper_registry.mapped
@dataclass
class ArXivMirrorList:
    __tablename__ = 'arXiv_mirror_list'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_mirror_list_fk_document_id'),
        Index('idx_132_arXiv_mirror_list_idx_document_id', 'document_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    mirror_list_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    version: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    write_source: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    write_abs: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    is_written: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    created: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    updated: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_mirror_list')})


t_arXiv_moderators = Table(
    'arXiv_moderators', metadata,
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('is_public', Boolean, nullable=False, server_default=text("'0'")),
    Column('no_email', Boolean(), server_default=text("'0'")),
    Column('no_web_email', Boolean(), server_default=text("'0'")),
    Column('no_reply_to', Boolean(), server_default=text("'0'")),
    Column('daily_update', Boolean(), server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_591'),
    ForeignKeyConstraint(['archive'], ['arXiv_archive_group.archive_id'], name='fk_archive_id'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_590'),
    Index('idx_133_arXiv_moderators_idx_no_email', 'no_email'),
    Index('idx_134_arXiv_moderators_idx_no_reply_to', 'no_reply_to'),
    Index('idx_135_arXiv_moderators_idx_no_web_email', 'no_web_email'),
    Index('idx_136_user_id', 'archive', 'subject_class', 'user_id', unique=True),
    Index('idx_137_user_id_2', 'user_id')
)


t_arXiv_paper_owners = Table(
    'arXiv_paper_owners', metadata,
    Column('document_id', Integer, nullable=False, server_default=text("'0'")),
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    Column('date', Integer, nullable=False, server_default=text("'0'")),
    Column('added_by', Integer, nullable=False, server_default=text("'0'")),
    Column('remote_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(32), nullable=False, server_default=text("''")),
    Column('valid', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_author', Integer, nullable=False, server_default=text("'0'")),
    Column('flag_auto', Integer, nullable=False, server_default=text("'1'")),
    ForeignKeyConstraint(['added_by'], ['tapir_users.user_id'], name='0_595'),
    ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_593'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_594'),
    Index('idx_138_added_by', 'added_by'),
    Index('idx_139_document_id', 'document_id', 'user_id', unique=True),
    Index('idx_140_user_id', 'user_id')
)


@mapper_registry.mapped
@dataclass
class ArXivPaperPw:
    __tablename__ = 'arXiv_paper_pw'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_585'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    document_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    password_storage: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    password_enc: Optional[str] = field(default=None, metadata={'sa': Column(String(50))})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_paper_pw')})


@mapper_registry.mapped
@dataclass
class ArXivQuestionableCategories:
    __tablename__ = 'arXiv_questionable_categories'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_756'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    archive: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, nullable=False, server_default=text("''"))})
    subject_class: str = field(init=False, metadata={'sa': Column(String(16), primary_key=True, nullable=False, server_default=text("''"))})

    arXiv_categories: Optional[ArXivCategories] = field(default=None, metadata={'sa': relationship('ArXivCategories', back_populates='arXiv_questionable_categories')})


@mapper_registry.mapped
@dataclass
class ArXivShowEmailRequests:
    __tablename__ = 'arXiv_show_email_requests'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_show_email_requests_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_show_email_requests_ibfk_2'),
        Index('idx_141_dated', 'dated'),
        Index('idx_142_document_id', 'document_id'),
        Index('idx_143_remote_addr', 'remote_addr'),
        Index('idx_144_user_id', 'user_id', 'dated')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    session_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    dated: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_allowed: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    remote_addr: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    request_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_show_email_requests')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_show_email_requests')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionControl:
    __tablename__ = 'arXiv_submission_control'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_submission_control_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_submission_control_ibfk_2'),
        Index('idx_145_document_id', 'document_id', 'version', unique=True),
        Index('idx_146_freeze_date', 'freeze_date'),
        Index('idx_147_pending_paper_id', 'pending_paper_id'),
        Index('idx_148_request_date', 'request_date'),
        Index('idx_149_status', 'status'),
        Index('idx_150_user_id', 'user_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    control_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    version: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    pending_paper_id: str = field(metadata={'sa': Column(String(20), nullable=False, server_default=text("''"))})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    status: str = field(metadata={'sa': Column(Enum('new', 'frozen', 'published', 'rejected'), nullable=False, server_default=text("'new'"))})
    request_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    freeze_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    publish_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_must_notify: Optional[str] = field(default=None, metadata={'sa': Column(Enum('0', '1'), server_default=text("'1'"))})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_submission_control')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_submission_control')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissions:
    __tablename__ = 'arXiv_submissions'
    __table_args__ = (
        ForeignKeyConstraint(['agreement_id'], ['arXiv_submission_agreements.agreement_id'], name='agreement_fk'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submissions_fk_document_id'),
        ForeignKeyConstraint(['license'], ['arXiv_licenses.name'], onupdate='CASCADE', name='arXiv_submissions_fk_license'),
        ForeignKeyConstraint(['submitter_id'], ['tapir_users.user_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submissions_fk_submitter_id'),
        ForeignKeyConstraint(['sword_id'], ['arXiv_tracking.sword_id'], name='arXiv_submissions_fk_sword_id'),
        Index('idx_151_agreement_fk', 'agreement_id'),
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
    __sa_dataclass_metadata_key__ = 'sa'

    submission_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    is_author: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    status: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    is_withdrawn: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    version: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    remote_addr: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    package: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    is_locked: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    document_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    doc_paper_id: Optional[str] = field(default=None, metadata={'sa': Column(String(20))})
    sword_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    userinfo: Optional[int] = field(default=None, metadata={'sa': Column(SmallInteger, server_default=text("'0'"))})
    agree_policy: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})
    viewed: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})
    stage: Optional[int] = field(default=None, metadata={'sa': Column(Integer, server_default=text("'0'"))})
    submitter_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    submitter_name: Optional[str] = field(default=None, metadata={'sa': Column(String(64))})
    submitter_email: Optional[str] = field(default=None, metadata={'sa': Column(String(64))})
    created: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    updated: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    sticky_status: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    must_process: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'1'"))})
    submit_time: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    release_time: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    source_size: Optional[int] = field(default=None, metadata={'sa': Column(Integer, server_default=text("'0'"))})
    source_format: Optional[str] = field(default=None, metadata={'sa': Column(String(12))})
    source_flags: Optional[str] = field(default=None, metadata={'sa': Column(String(12))})
    has_pilot_data: Optional[int] = field(default=None, metadata={'sa': Column(Boolean())})
    title: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    authors: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    comments: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    proxy: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    report_num: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    msc_class: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    acm_class: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    journal_ref: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    doi: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    abstract: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    license: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    type: Optional[str] = field(default=None, metadata={'sa': Column(CHAR(8))})
    is_ok: Optional[int] = field(default=None, metadata={'sa': Column(Boolean())})
    admin_ok: Optional[int] = field(default=None, metadata={'sa': Column(Boolean())})
    allow_tex_produced: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})
    is_oversize: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})
    rt_ticket_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    auto_hold: Optional[int] = field(default=None, metadata={'sa': Column(SmallInteger, server_default=text("'0'"))})
    agreement_id: Optional[int] = field(default=None, metadata={'sa': Column(SmallInteger)})

    agreement: Optional[ArXivSubmissionAgreements] = field(default=None, metadata={'sa': relationship('ArXivSubmissionAgreements', back_populates='arXiv_submissions')})
    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_submissions')})
    arXiv_licenses: Optional[ArXivLicenses] = field(default=None, metadata={'sa': relationship('ArXivLicenses', back_populates='arXiv_submissions')})
    submitter: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_submissions')})
    sword: Optional[ArXivTracking] = field(default=None, metadata={'sa': relationship('ArXivTracking', back_populates='arXiv_submissions')})
    arXiv_pilot_datasets: Optional[ArXivPilotDatasets] = field(default=None, metadata={'sa': relationship('ArXivPilotDatasets', uselist=False, back_populates='submission')})
    arXiv_pilot_files: List[ArXivPilotFiles] = field(default_factory=list, metadata={'sa': relationship('ArXivPilotFiles', back_populates='submission')})
    arXiv_submission_abs_classifier_data: Optional[ArXivSubmissionAbsClassifierData] = field(default=None, metadata={'sa': relationship('ArXivSubmissionAbsClassifierData', uselist=False, back_populates='submission')})
    arXiv_submission_category: List[ArXivSubmissionCategory] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionCategory', back_populates='submission')})
    arXiv_submission_category_proposal: List[ArXivSubmissionCategoryProposal] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionCategoryProposal', back_populates='submission')})
    arXiv_submission_classifier_data: Optional[ArXivSubmissionClassifierData] = field(default=None, metadata={'sa': relationship('ArXivSubmissionClassifierData', uselist=False, back_populates='submission')})
    arXiv_submission_flag: List[ArXivSubmissionFlag] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionFlag', back_populates='submission')})
    arXiv_submission_hold_reason: List[ArXivSubmissionHoldReason] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionHoldReason', back_populates='submission')})
    arXiv_submission_near_duplicates: List[ArXivSubmissionNearDuplicates] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionNearDuplicates', back_populates='submission')})
    arXiv_submission_qa_reports: List[ArXivSubmissionQaReports] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionQaReports', back_populates='submission')})
    arXiv_submission_view_flag: List[ArXivSubmissionViewFlag] = field(default_factory=list, metadata={'sa': relationship('ArXivSubmissionViewFlag', back_populates='submission')})


@mapper_registry.mapped
@dataclass
class ArXivTopPapers:
    __tablename__ = 'arXiv_top_papers'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_top_papers_ibfk_1'),
        Index('idx_152_document_id', 'document_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    from_week: date = field(init=False, metadata={'sa': Column(Date, primary_key=True, nullable=False, server_default=text("'0000-00-00'"))})
    class_: str = field(init=False, metadata={'sa': Column('class', CHAR(1), primary_key=True, nullable=False, server_default=text("''"))})
    rank: int = field(metadata={'sa': Column(SmallInteger, primary_key=True, nullable=False, server_default=text("'0'"))})
    document_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    viewers: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_top_papers')})


@mapper_registry.mapped
@dataclass
class ArXivVersions:
    __tablename__ = 'arXiv_versions'
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_versions_ibfk_1'),
        Index('idx_153_freeze_date', 'freeze_date'),
        Index('idx_154_publish_date', 'publish_date'),
        Index('idx_155_request_date', 'request_date')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    document_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    version: int = field(metadata={'sa': Column(SmallInteger, primary_key=True, nullable=False, server_default=text("'0'"))})
    request_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    freeze_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    publish_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_current: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    document: Optional[ArXivDocuments] = field(default=None, metadata={'sa': relationship('ArXivDocuments', back_populates='arXiv_versions')})
    arXiv_versions_checksum: Optional[ArXivVersionsChecksum] = field(default=None, metadata={'sa': relationship('ArXivVersionsChecksum', uselist=False, back_populates='arXiv_versions')})


@mapper_registry.mapped
@dataclass
class TapirAdminAudit:
    __tablename__ = 'tapir_admin_audit'
    __table_args__ = (
        ForeignKeyConstraint(['admin_user'], ['tapir_users.user_id'], name='0_554'),
        ForeignKeyConstraint(['affected_user'], ['tapir_users.user_id'], name='0_555'),
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_553'),
        Index('idx_156_admin_user', 'admin_user'),
        Index('idx_157_affected_user', 'affected_user'),
        Index('idx_158_data', 'data'),
        Index('idx_159_data_2', 'data'),
        Index('idx_160_data_3', 'data'),
        Index('idx_161_ip_addr', 'ip_addr'),
        Index('idx_162_log_date', 'log_date'),
        Index('idx_163_session_id', 'session_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    log_date: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    ip_addr: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    affected_user: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    action: str = field(metadata={'sa': Column(String(32), nullable=False, server_default=text("''"))})
    data: str = field(metadata={'sa': Column(Text, nullable=False)})
    comment: str = field(metadata={'sa': Column(Text, nullable=False)})
    entry_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    session_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    admin_user: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})

    tapir_users: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[admin_user], back_populates='tapir_admin_audit')})
    tapir_users_: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[affected_user], back_populates='tapir_admin_audit_')})
    session: Optional[TapirSessions] = field(default=None, metadata={'sa': relationship('TapirSessions', back_populates='tapir_admin_audit')})


t_tapir_email_change_tokens_used = Table(
    'tapir_email_change_tokens_used', metadata,
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', Integer, nullable=False, server_default=text("'0'")),
    Column('used_from', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', Integer, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_538'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_537'),
    Index('idx_164_session_id', 'session_id'),
    Index('idx_165_user_id', 'user_id')
)


@mapper_registry.mapped
@dataclass
class TapirEmailHeaders:
    __tablename__ = 'tapir_email_headers'
    __table_args__ = (
        ForeignKeyConstraint(['template_id'], ['tapir_email_templates.template_id'], name='0_563'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    template_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    header_name: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    header_content: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})

    template: Optional[TapirEmailTemplates] = field(default=None, metadata={'sa': relationship('TapirEmailTemplates', back_populates='tapir_email_headers')})


@mapper_registry.mapped
@dataclass
class TapirEmailMailings:
    __tablename__ = 'tapir_email_mailings'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['tapir_users.user_id'], name='0_565'),
        ForeignKeyConstraint(['sent_by'], ['tapir_users.user_id'], name='0_566'),
        ForeignKeyConstraint(['template_id'], ['tapir_email_templates.template_id'], name='0_567'),
        Index('idx_166_created_by', 'created_by'),
        Index('idx_167_sent_by', 'sent_by'),
        Index('idx_168_template_id', 'template_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    mailing_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    template_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    created_by: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    sent_by: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    created_date: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    sent_date: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    complete_date: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    mailing_name: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    comment: Optional[str] = field(default=None, metadata={'sa': Column(Text)})

    tapir_users: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[created_by], back_populates='tapir_email_mailings')})
    tapir_users_: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[sent_by], back_populates='tapir_email_mailings_')})
    template: Optional[TapirEmailTemplates] = field(default=None, metadata={'sa': relationship('TapirEmailTemplates', back_populates='tapir_email_mailings')})


t_tapir_email_tokens_used = Table(
    'tapir_email_tokens_used', metadata,
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', Integer, nullable=False, server_default=text("'0'")),
    Column('used_from', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', Integer, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_533'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_532'),
    Index('idx_169_session_id', 'session_id'),
    Index('idx_170_user_id', 'user_id')
)


@mapper_registry.mapped
@dataclass
class TapirPermanentTokens:
    __tablename__ = 'tapir_permanent_tokens'
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_541'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_540'),
        Index('idx_171_session_id', 'session_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    secret: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    valid: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'1'"))})
    issued_when: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    issued_to: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    session_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})

    session: Optional[TapirSessions] = field(default=None, metadata={'sa': relationship('TapirSessions', back_populates='tapir_permanent_tokens')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_permanent_tokens')})


t_tapir_permanent_tokens_used = Table(
    'tapir_permanent_tokens_used', metadata,
    Column('user_id', Integer),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', Integer),
    Column('used_from', String(16)),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', Integer, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_544'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_543'),
    Index('idx_172_session_id', 'session_id'),
    Index('idx_173_user_id', 'user_id')
)


@mapper_registry.mapped
@dataclass
class TapirRecoveryTokensUsed:
    __tablename__ = 'tapir_recovery_tokens_used'
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_549'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_548'),
        Index('idx_174_session_id', 'session_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    secret: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    used_when: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    used_from: Optional[str] = field(default=None, metadata={'sa': Column(String(16))})
    session_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})

    session: Optional[TapirSessions] = field(default=None, metadata={'sa': relationship('TapirSessions', back_populates='tapir_recovery_tokens_used')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='tapir_recovery_tokens_used')})


@mapper_registry.mapped
@dataclass
class TapirSessionsAudit:
    __tablename__ = 'tapir_sessions_audit'
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_527'),
        Index('idx_175_ip_addr', 'ip_addr'),
        Index('idx_176_tracking_cookie', 'tracking_cookie')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    session_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    ip_addr: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})

    session: Optional[TapirSessions] = field(default=None, metadata={'sa': relationship('TapirSessions', back_populates='tapir_sessions_audit')})


@mapper_registry.mapped
@dataclass
class ArXivDataciteDois:
    __tablename__ = 'arXiv_datacite_dois'
    __table_args__ = (
        ForeignKeyConstraint(['metadata_id'], ['arXiv_metadata.metadata_id'], name='arXiv_datacite_dois_ibfk_1'),
        Index('idx_177_account_paper_id', 'account', 'paper_id', unique=True),
        Index('idx_178_metadata_id', 'metadata_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    doi: str = field(init=False, metadata={'sa': Column(String(255), primary_key=True)})
    metadata_id: int = field(metadata={'sa': Column(Integer, nullable=False)})
    paper_id: str = field(metadata={'sa': Column(String(64), nullable=False)})
    account: Optional[str] = field(default=None, metadata={'sa': Column(Enum('test', 'prod'))})
    created: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))})
    updated: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime, server_default=CURRENT_TIMESTAMP_SD)})

    metadata_: Optional[ArXivMetadata] = field(default=None, metadata={'sa': relationship('ArXivMetadata', back_populates='arXiv_datacite_dois')})


@mapper_registry.mapped
@dataclass
class ArXivEndorsementRequestsAudit:
    __tablename__ = 'arXiv_endorsement_requests_audit'
    __table_args__ = (
        ForeignKeyConstraint(['request_id'], ['arXiv_endorsement_requests.request_id'], name='0_725'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    request_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    session_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    remote_addr: Optional[str] = field(default=None, metadata={'sa': Column(String(16))})
    remote_host: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})
    tracking_cookie: Optional[str] = field(default=None, metadata={'sa': Column(String(255))})

    request: Optional[ArXivEndorsementRequests] = field(default=None, metadata={'sa': relationship('ArXivEndorsementRequests', back_populates='arXiv_endorsement_requests_audit')})


@mapper_registry.mapped
@dataclass
class ArXivEndorsements:
    __tablename__ = 'arXiv_endorsements'
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_729'),
        ForeignKeyConstraint(['endorsee_id'], ['tapir_users.user_id'], name='0_728'),
        ForeignKeyConstraint(['endorser_id'], ['tapir_users.user_id'], name='0_727'),
        ForeignKeyConstraint(['request_id'], ['arXiv_endorsement_requests.request_id'], name='0_730'),
        Index('idx_179_archive', 'archive', 'subject_class'),
        Index('idx_180_endorsee_id', 'endorsee_id'),
        Index('idx_181_endorser_id', 'endorser_id'),
        Index('idx_182_endorser_id_2', 'endorser_id', 'endorsee_id', 'archive', 'subject_class', unique=True),
        Index('idx_183_request_id', 'request_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    endorsement_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    endorsee_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    archive: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    subject_class: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    flag_valid: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    point_value: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    issued_when: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    endorser_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    type: Optional[str] = field(default=None, metadata={'sa': Column(Enum('user', 'admin', 'auto'))})
    request_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})

    arXiv_categories: Optional[ArXivCategories] = field(default=None, metadata={'sa': relationship('ArXivCategories', back_populates='arXiv_endorsements')})
    endorsee: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[endorsee_id], back_populates='arXiv_endorsements')})
    endorser: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', foreign_keys=[endorser_id], back_populates='arXiv_endorsements_')})
    request: Optional[ArXivEndorsementRequests] = field(default=None, metadata={'sa': relationship('ArXivEndorsementRequests', back_populates='arXiv_endorsements')})
    arXiv_endorsements_audit: Optional[ArXivEndorsementsAudit] = field(default=None, metadata={'sa': relationship('ArXivEndorsementsAudit', uselist=False, back_populates='endorsement')})


@mapper_registry.mapped
@dataclass
class ArXivOwnershipRequests:
    __tablename__ = 'arXiv_ownership_requests'
    __table_args__ = (
        ForeignKeyConstraint(['endorsement_request_id'], ['arXiv_endorsement_requests.request_id'], name='0_735'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_734'),
        Index('idx_184_endorsement_request_id', 'endorsement_request_id'),
        Index('idx_185_user_id', 'user_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    request_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    workflow_status: str = field(metadata={'sa': Column(Enum('pending', 'accepted', 'rejected'), nullable=False, server_default=text("'pending'"))})
    endorsement_request_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})

    endorsement_request: Optional[ArXivEndorsementRequests] = field(default=None, metadata={'sa': relationship('ArXivEndorsementRequests', back_populates='arXiv_ownership_requests')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_ownership_requests')})
    arXiv_ownership_requests_audit: Optional[ArXivOwnershipRequestsAudit] = field(default=None, metadata={'sa': relationship('ArXivOwnershipRequestsAudit', uselist=False, back_populates='request')})


@mapper_registry.mapped
@dataclass
class ArXivPilotDatasets:
    __tablename__ = 'arXiv_pilot_datasets'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_pilot_datasets_cdfk3'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    submission_id: int = field(metadata={'sa': Column(Integer, primary_key=True)})
    created: datetime = field(metadata={'sa': Column(DateTime, nullable=False)})
    last_checked: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD)})
    numfiles: Optional[int] = field(default=None, metadata={'sa': Column(SmallInteger, server_default=text("'0'"))})
    feed_url: Optional[str] = field(default=None, metadata={'sa': Column(String(256))})
    manifestation: Optional[str] = field(default=None, metadata={'sa': Column(String(256))})
    published: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})

    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_pilot_datasets')})


@mapper_registry.mapped
@dataclass
class ArXivPilotFiles:
    __tablename__ = 'arXiv_pilot_files'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_pilot_files_cdfk3'),
        Index('arXiv_pilot_files_cdfk3', 'submission_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    file_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    submission_id: int = field(metadata={'sa': Column(Integer, nullable=False)})
    filename: Optional[str] = field(default=None, metadata={'sa': Column(String(256), server_default=text("''"))})
    entity_url: Optional[str] = field(default=None, metadata={'sa': Column(String(256))})
    description: Optional[str] = field(default=None, metadata={'sa': Column(String(80))})
    byRef: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'1'"))})

    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_pilot_files')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionAbsClassifierData:
    __tablename__ = 'arXiv_submission_abs_classifier_data'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_abs_classifier_data_ibfk_1'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    submission_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    last_update: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD)})
    json: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    status: Optional[str] = field(default=None, metadata={'sa': Column(Enum('processing', 'success', 'failed', 'no connection'))})
    message: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    is_oversize: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})
    suggested_primary: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    suggested_reason: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    autoproposal_primary: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    autoproposal_reason: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    classifier_service_version: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    classifier_model_version: Optional[str] = field(default=None, metadata={'sa': Column(Text)})

    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_abs_classifier_data')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionCategory:
    __tablename__ = 'arXiv_submission_category'
    __table_args__ = (
        ForeignKeyConstraint(['category'], ['arXiv_category_def.category'], name='arXiv_submission_category_fk_category'),
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submission_category_fk_submission_id'),
        Index('arXiv_submission_category_idx_category', 'category'),
        Index('arXiv_submission_category_idx_is_primary', 'is_primary'),
        Index('arXiv_submission_category_idx_is_published', 'is_published'),
        Index('arXiv_submission_category_idx_submission_id', 'submission_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    submission_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False)})
    category: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False, server_default=text("''"))})
    is_primary: int = field(metadata={'sa': Column(Boolean(), nullable=False, server_default=text("'0'"))})
    is_published: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})

    arXiv_category_def: Optional[ArXivCategoryDef] = field(default=None, metadata={'sa': relationship('ArXivCategoryDef', back_populates='arXiv_submission_category')})
    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_category')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionCategoryProposal:
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
    __sa_dataclass_metadata_key__ = 'sa'

    proposal_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True, nullable=False)})
    submission_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False)})
    category: str = field(init=False, metadata={'sa': Column(String(32), primary_key=True, nullable=False)})
    is_primary: int = field(metadata={'sa': Column(Boolean(), primary_key=True, nullable=False, server_default=text("'0'"))})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False)})
    proposal_status: Optional[int] = field(default=None, metadata={'sa': Column(Integer, server_default=text("'0'"))})
    updated: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})
    proposal_comment_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})
    response_comment_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})

    arXiv_category_def: Optional[ArXivCategoryDef] = field(default=None, metadata={'sa': relationship('ArXivCategoryDef', back_populates='arXiv_submission_category_proposal')})
    proposal_comment: Optional[ArXivAdminLog] = field(default=None, metadata={'sa': relationship('ArXivAdminLog', foreign_keys=[proposal_comment_id], back_populates='arXiv_submission_category_proposal')})
    response_comment: Optional[ArXivAdminLog] = field(default=None, metadata={'sa': relationship('ArXivAdminLog', foreign_keys=[response_comment_id], back_populates='arXiv_submission_category_proposal_')})
    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_category_proposal')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_submission_category_proposal')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionClassifierData:
    __tablename__ = 'arXiv_submission_classifier_data'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_classifier_data_ibfk_1'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    submission_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    last_update: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD)})
    json: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    status: Optional[str] = field(default=None, metadata={'sa': Column(Enum('processing', 'success', 'failed', 'no connection'))})
    message: Optional[str] = field(default=None, metadata={'sa': Column(Text)})
    is_oversize: Optional[int] = field(default=None, metadata={'sa': Column(Boolean(), server_default=text("'0'"))})

    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_classifier_data')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionFlag:
    __tablename__ = 'arXiv_submission_flag'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_flag_ibfk_2'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_flag_ibfk_1'),
        Index('idx_186_uniq_one_flag_per_mod', 'submission_id', 'user_id', unique=True),
        Index('idx_187_user_id', 'user_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    flag_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    user_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    submission_id: int = field(metadata={'sa': Column(Integer, nullable=False)})
    flag: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    updated: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD)})

    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_flag')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_submission_flag')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionHoldReason:
    __tablename__ = 'arXiv_submission_hold_reason'
    __table_args__ = (
        ForeignKeyConstraint(['comment_id'], ['arXiv_admin_log.id'], name='arXiv_submission_hold_reason_ibfk_3'),
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_hold_reason_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_hold_reason_ibfk_2'),
        Index('idx_188_comment_id', 'comment_id'),
        Index('idx_189_submission_id', 'submission_id'),
        Index('idx_190_user_id', 'user_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    reason_id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True, nullable=False)})
    submission_id: int = field(metadata={'sa': Column(Integer, nullable=False)})
    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False)})
    reason: Optional[str] = field(default=None, metadata={'sa': Column(String(30))})
    type: Optional[str] = field(default=None, metadata={'sa': Column(String(30))})
    comment_id: Optional[int] = field(default=None, metadata={'sa': Column(Integer)})

    comment: Optional[ArXivAdminLog] = field(default=None, metadata={'sa': relationship('ArXivAdminLog', back_populates='arXiv_submission_hold_reason')})
    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_hold_reason')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_submission_hold_reason')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionNearDuplicates:
    __tablename__ = 'arXiv_submission_near_duplicates'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_near_duplicates_ibfk_1'),
        Index('idx_191_match', 'submission_id', 'matching_id', unique=True)
    )
    __sa_dataclass_metadata_key__ = 'sa'

    submission_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    matching_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    similarity: Decimal = field(metadata={'sa': Column(Numeric(precision=2,scale=1), nullable=False)})
    last_update: datetime = field(metadata={'sa': Column(TIMESTAMP, nullable=False, server_default=CURRENT_TIMESTAMP_SD)})

    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_near_duplicates')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionQaReports:
    __tablename__ = 'arXiv_submission_qa_reports'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_submission_qa_reports_ibfk_1'),
        Index('idx_192_report_key_name', 'report_key_name'),
        Index('idx_193_submission_id', 'submission_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    id: int = field(init=False, metadata={'sa': Column(Integer, primary_key=True)})
    submission_id: int = field(metadata={'sa': Column(Integer, nullable=False)})
    report_key_name: str = field(metadata={'sa': Column(String(64), nullable=False)})
    num_flags: int = field(metadata={'sa': Column(SmallInteger, nullable=False, server_default=text("'0'"))})
    report: dict = field(metadata={'sa': Column(JSON, nullable=False)})
    created: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))})
    report_uri: Optional[str] = field(default=None, metadata={'sa': Column(String(256))})

    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_qa_reports')})


@mapper_registry.mapped
@dataclass
class ArXivSubmissionViewFlag:
    __tablename__ = 'arXiv_submission_view_flag'
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_view_flag_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_view_flag_ibfk_2'),
        Index('idx_194_user_id', 'user_id')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    submission_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False)})
    user_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False)})
    flag: Optional[int] = field(default=None, metadata={'sa': Column(SmallInteger, server_default=text("'0'"))})
    updated: Optional[datetime] = field(default=None, metadata={'sa': Column(DateTime)})

    submission: Optional[ArXivSubmissions] = field(default=None, metadata={'sa': relationship('ArXivSubmissions', back_populates='arXiv_submission_view_flag')})
    user: Optional[TapirUsers] = field(default=None, metadata={'sa': relationship('TapirUsers', back_populates='arXiv_submission_view_flag')})


@mapper_registry.mapped
@dataclass
class ArXivVersionsChecksum:
    __tablename__ = 'arXiv_versions_checksum'
    __table_args__ = (
        ForeignKeyConstraint(['document_id', 'version'], ['arXiv_versions.document_id', 'arXiv_versions.version'], name='arXiv_versions_checksum_ibfk_1'),
        Index('idx_195_abs_md5sum', 'abs_md5sum'),
        Index('idx_196_abs_size', 'abs_size'),
        Index('idx_197_src_md5sum', 'src_md5sum'),
        Index('idx_198_src_size', 'src_size')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    document_id: int = field(metadata={'sa': Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))})
    version: int = field(metadata={'sa': Column(SmallInteger, primary_key=True, nullable=False, server_default=text("'0'"))})
    flag_abs_present: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    abs_size: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_src_present: int = field(metadata={'sa': Column(Boolean, nullable=False, server_default=text("'0'"))})
    src_size: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    abs_md5sum: Optional[bytes] = field(default=None, metadata={'sa': Column(BINARY(16))})
    src_md5sum: Optional[bytes] = field(default=None, metadata={'sa': Column(BINARY(16))})

    arXiv_versions: Optional[ArXivVersions] = field(default=None, metadata={'sa': relationship('ArXivVersions', back_populates='arXiv_versions_checksum')})


@mapper_registry.mapped
@dataclass
class ArXivEndorsementsAudit:
    __tablename__ = 'arXiv_endorsements_audit'
    __table_args__ = (
        ForeignKeyConstraint(['endorsement_id'], ['arXiv_endorsements.endorsement_id'], name='0_732'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    endorsement_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    session_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    remote_addr: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    flag_knows_personally: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    flag_seen_paper: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    comment: Optional[str] = field(default=None, metadata={'sa': Column(Text)})

    endorsement: Optional[ArXivEndorsements] = field(default=None, metadata={'sa': relationship('ArXivEndorsements', back_populates='arXiv_endorsements_audit')})


@mapper_registry.mapped
@dataclass
class ArXivOwnershipRequestsAudit:
    __tablename__ = 'arXiv_ownership_requests_audit'
    __table_args__ = (
        ForeignKeyConstraint(['request_id'], ['arXiv_ownership_requests.request_id'], name='0_737'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    request_id: int = field(metadata={'sa': Column(Integer, primary_key=True, server_default=text("'0'"))})
    session_id: int = field(metadata={'sa': Column(Integer, nullable=False, server_default=text("'0'"))})
    remote_addr: str = field(metadata={'sa': Column(String(16), nullable=False, server_default=text("''"))})
    remote_host: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    tracking_cookie: str = field(metadata={'sa': Column(String(255), nullable=False, server_default=text("''"))})
    date_: int = field(metadata={'sa': Column('date', Integer, nullable=False, server_default=text("'0'"))})

    request: Optional[ArXivOwnershipRequests] = field(default=None, metadata={'sa': relationship('ArXivOwnershipRequests', back_populates='arXiv_ownership_requests_audit')})
