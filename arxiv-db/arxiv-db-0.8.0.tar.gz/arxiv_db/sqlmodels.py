"""Database models for use with arXiv.

# THIS PACKAGE DOES NOT WORK! #

Somehow the generated models don't
have the names of the tables the models are associated with.

# History
2022-09-23 Generated from the production DB  using sqlacodegen 3.0.0rc1

2022-09-23 Convert the mysql specific types to generic types

CHAR -> generic CHAR
DECIMAL -> Numeric()
INTEGER, MEDIUMINT -> Integer
SMALLINT -> SmallInteger
VARCHAR -> String()
MEDIUMTEXT -> Text
TINYINT -> Some to SmallInteger and any with "is_somehting" to Boolean

"""
from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text, Numeric, Boolean
from sqlalchemy.types import SmallInteger
from sqlmodel import Field, Relationship, SQLModel

metadata = SQLModel.metadata


class SubscriptionUniversalInstitution(SQLModel, table=True):
    __table_args__ = (
        Index('name', 'name'),
    )

    name: str = Field(sa_column=Column('name', String(255), nullable=False))
    id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
    resolver_URL: Optional[str] = Field(default=None, sa_column=Column('resolver_URL', String(255)))
    label: Optional[str] = Field(default=None, sa_column=Column('label', String(255)))
    alt_text: Optional[str] = Field(default=None, sa_column=Column('alt_text', String(255)))
    link_icon: Optional[str] = Field(default=None, sa_column=Column('link_icon', String(255)))
    note: Optional[str] = Field(default=None, sa_column=Column('note', String(255)))

    Subscription_UniversalInstitutionContact: List['SubscriptionUniversalInstitutionContact'] = Relationship(back_populates='Subscription_UniversalInstitution')
    Subscription_UniversalInstitutionIP: List['SubscriptionUniversalInstitutionIP'] = Relationship(back_populates='Subscription_UniversalInstitution')


class ArXivAdminLog(SQLModel, table=True):
    __table_args__ = (
        Index('arXiv_admin_log_idx_command', 'command'),
        Index('arXiv_admin_log_idx_paper_id', 'paper_id'),
        Index('arXiv_admin_log_idx_submission_id', 'submission_id'),
        Index('arXiv_admin_log_idx_username', 'username')
    )

    id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
    created: datetime = Field(sa_column=Column('created', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))
    logtime: Optional[str] = Field(default=None, sa_column=Column('logtime', String(24)))
    paper_id: Optional[str] = Field(default=None, sa_column=Column('paper_id', String(20)))
    username: Optional[str] = Field(default=None, sa_column=Column('username', String(20)))
    host: Optional[str] = Field(default=None, sa_column=Column('host', String(64)))
    program: Optional[str] = Field(default=None, sa_column=Column('program', String(20)))
    command: Optional[str] = Field(default=None, sa_column=Column('command', String(20)))
    logtext: Optional[str] = Field(default=None, sa_column=Column('logtext', Text))
    document_id: Optional[int] = Field(default=None, sa_column=Column('document_id', Integer))
    submission_id: Optional[int] = Field(default=None, sa_column=Column('submission_id', Integer))
    notify: Optional[int] = Field(default=None, sa_column=Column('notify', Boolean(), server_default=text("'0'")))

    arXiv_submission_category_proposal: List['ArXivSubmissionCategoryProposal'] = Relationship(back_populates='proposal_comment')
    arXiv_submission_category_proposal_: List['ArXivSubmissionCategoryProposal'] = Relationship(back_populates='response_comment')
    arXiv_submission_hold_reason: List['ArXivSubmissionHoldReason'] = Relationship(back_populates='comment')


t_arXiv_admin_state = Table(
    'arXiv_admin_state', metadata,
    Column('document_id', Integer),
    Column('timestamp', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    Column('abs_timestamp', Integer),
    Column('src_timestamp', Integer),
    Column('state', Enum('pending', 'ok', 'bad'), nullable=False, server_default=text("'pending'")),
    Column('admin', String(32)),
    Column('comment', String(255)),
    Index('document_id', 'document_id', unique=True)
)


class ArXivArchiveCategory(SQLModel, table=True):
    archive_id: Optional[str] = Field(default=None, sa_column=Column('archive_id', String(16), primary_key=True, nullable=False, server_default=text("''")))
    category_id: Optional[str] = Field(default=None, sa_column=Column('category_id', String(32), primary_key=True, nullable=False))


class ArXivArchiveDef(SQLModel, table=True):
    archive: Optional[str] = Field(default=None, sa_column=Column('archive', String(16), primary_key=True, server_default=text("''")))
    name: Optional[str] = Field(default=None, sa_column=Column('name', String(255)))


class ArXivArchiveGroup(SQLModel, table=True):
    archive_id: Optional[str] = Field(default=None, sa_column=Column('archive_id', String(16), primary_key=True, nullable=False, server_default=text("''")))
    group_id: Optional[str] = Field(default=None, sa_column=Column('group_id', String(16), primary_key=True, nullable=False, server_default=text("''")))


class ArXivAwsConfig(SQLModel, table=True):
    domain: Optional[str] = Field(default=None, sa_column=Column('domain', String(75), primary_key=True, nullable=False))
    keyname: Optional[str] = Field(default=None, sa_column=Column('keyname', String(60), primary_key=True, nullable=False))
    value: Optional[str] = Field(default=None, sa_column=Column('value', String(150)))


class ArXivAwsFiles(SQLModel, table=True):
    __table_args__ = (
        Index('type', 'type'),
    )

    type: str = Field(sa_column=Column('type', String(10), nullable=False, server_default=text("''")))
    filename: Optional[str] = Field(default=None, sa_column=Column('filename', String(100), primary_key=True, server_default=text("''")))
    md5sum: Optional[str] = Field(default=None, sa_column=Column('md5sum', String(50)))
    content_md5sum: Optional[str] = Field(default=None, sa_column=Column('content_md5sum', String(50)))
    size: Optional[int] = Field(default=None, sa_column=Column('size', Integer))
    timestamp: Optional[datetime] = Field(default=None, sa_column=Column('timestamp', DateTime))
    yymm: Optional[str] = Field(default=None, sa_column=Column('yymm', String(4)))
    seq_num: Optional[int] = Field(default=None, sa_column=Column('seq_num', Integer))
    first_item: Optional[str] = Field(default=None, sa_column=Column('first_item', String(20)))
    last_item: Optional[str] = Field(default=None, sa_column=Column('last_item', String(20)))
    num_items: Optional[int] = Field(default=None, sa_column=Column('num_items', Integer))


class ArXivBibFeeds(SQLModel, table=True):
    bib_id: Optional[int] = Field(default=None, sa_column=Column('bib_id', Integer, primary_key=True))
    name: str = Field(sa_column=Column('name', String(64), nullable=False, server_default=text("''")))
    priority: int = Field(sa_column=Column('priority', SmallInteger, nullable=False, server_default=text("'0'")))
    strip_journal_ref: int = Field(sa_column=Column('strip_journal_ref', Boolean(), nullable=False, server_default=text("'0'")))
    uri: Optional[str] = Field(default=None, sa_column=Column('uri', String(255)))
    identifier: Optional[str] = Field(default=None, sa_column=Column('identifier', String(255)))
    version: Optional[str] = Field(default=None, sa_column=Column('version', String(255)))
    concatenate_dupes: Optional[int] = Field(default=None, sa_column=Column('concatenate_dupes', Integer))
    max_updates: Optional[int] = Field(default=None, sa_column=Column('max_updates', Integer))
    email_errors: Optional[str] = Field(default=None, sa_column=Column('email_errors', String(255)))
    prune_ids: Optional[str] = Field(default=None, sa_column=Column('prune_ids', Text))
    prune_regex: Optional[str] = Field(default=None, sa_column=Column('prune_regex', Text))
    enabled: Optional[int] = Field(default=None, sa_column=Column('enabled', Boolean(), server_default=text("'0'")))


class ArXivBibUpdates(SQLModel, table=True):
    update_id: Optional[int] = Field(default=None, sa_column=Column('update_id', Integer, primary_key=True))
    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    bib_id: int = Field(sa_column=Column('bib_id', Integer, nullable=False, server_default=text("'0'")))
    updated: datetime = Field(sa_column=Column('updated', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP')))
    journal_ref: Optional[str] = Field(default=None, sa_column=Column('journal_ref', Text))
    doi: Optional[str] = Field(default=None, sa_column=Column('doi', Text))


t_arXiv_black_email = Table(
    'arXiv_black_email', metadata,
    Column('pattern', String(64))
)


t_arXiv_block_email = Table(
    'arXiv_block_email', metadata,
    Column('pattern', String(64))
)


class ArXivBogusCountries(SQLModel, table=True):
    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, server_default=text("'0'")))
    country_name: str = Field(sa_column=Column('country_name', String(255), nullable=False, server_default=text("''")))


class ArXivCategoryDef(SQLModel, table=True):
    category: Optional[str] = Field(default=None, sa_column=Column('category', String(32), primary_key=True))
    name: Optional[str] = Field(default=None, sa_column=Column('name', String(255)))
    active: Optional[int] = Field(default=None, sa_column=Column('active', Boolean(), server_default=text("'1'")))

    arXiv_document_category: List['ArXivDocumentCategory'] = Relationship(back_populates='arXiv_category_def')
    arXiv_submission_category: List['ArXivSubmissionCategory'] = Relationship(back_populates='arXiv_category_def')
    arXiv_submission_category_proposal: List['ArXivSubmissionCategoryProposal'] = Relationship(back_populates='arXiv_category_def')


class ArXivDblpAuthors(SQLModel, table=True):
    __table_args__ = (
        Index('author_id', 'author_id', unique=True),
        Index('name', 'name', unique=True)
    )

    author_id: Optional[int] = Field(default=None, sa_column=Column('author_id', Integer, primary_key=True))
    name: Optional[str] = Field(default=None, sa_column=Column('name', String(40)))

    arXiv_dblp_document_authors: List['ArXivDblpDocumentAuthors'] = Relationship(back_populates='author')


class ArXivEndorsementDomains(SQLModel, table=True):
    endorsement_domain: Optional[str] = Field(default=None, sa_column=Column('endorsement_domain', String(32), primary_key=True, server_default=text("''")))
    endorse_all: str = Field(sa_column=Column('endorse_all', Enum('y', 'n'), nullable=False, server_default=text("'n'")))
    mods_endorse_all: str = Field(sa_column=Column('mods_endorse_all', Enum('y', 'n'), nullable=False, server_default=text("'n'")))
    endorse_email: str = Field(sa_column=Column('endorse_email', Enum('y', 'n'), nullable=False, server_default=text("'y'")))
    papers_to_endorse: int = Field(sa_column=Column('papers_to_endorse', SmallInteger, nullable=False, server_default=text("'4'")))

    arXiv_categories: List['ArXivCategories'] = Relationship(back_populates='arXiv_endorsement_domains')


class ArXivFreezeLog(SQLModel, table=True):
    date_: int = Field(sa_column=Column('date', Integer, primary_key=True, server_default=text("'0'")))


class ArXivGroupDef(SQLModel, table=True):
    archive_group: Optional[str] = Field(default=None, sa_column=Column('archive_group', String(16), primary_key=True, server_default=text("''")))
    name: Optional[str] = Field(default=None, sa_column=Column('name', String(255)))


class ArXivGroups(SQLModel, table=True):
    group_id: Optional[str] = Field(default=None, sa_column=Column('group_id', String(16), primary_key=True, server_default=text("''")))
    group_name: str = Field(sa_column=Column('group_name', String(255), nullable=False, server_default=text("''")))
    start_year: str = Field(sa_column=Column('start_year', String(4), nullable=False, server_default=text("''")))

    arXiv_archives: List['ArXivArchives'] = Relationship(back_populates='arXiv_groups')


class ArXivLicenses(SQLModel, table=True):
    name: Optional[str] = Field(default=None, sa_column=Column('name', String(255), primary_key=True))
    label: Optional[str] = Field(default=None, sa_column=Column('label', String(255)))
    active: Optional[int] = Field(default=None, sa_column=Column('active', Boolean(), server_default=text("'1'")))
    note: Optional[str] = Field(default=None, sa_column=Column('note', String(400)))
    sequence: Optional[int] = Field(default=None, sa_column=Column('sequence', SmallInteger))

    arXiv_metadata: List['ArXivMetadata'] = Relationship(back_populates='arXiv_licenses')
    arXiv_submissions: List['ArXivSubmissions'] = Relationship(back_populates='arXiv_licenses')


class ArXivLogPositions(SQLModel, table=True):
    id: Optional[str] = Field(default=None, sa_column=Column('id', String(255), primary_key=True, server_default=text("''")))
    position: Optional[int] = Field(default=None, sa_column=Column('position', Integer))
    date_: Optional[int] = Field(default=None, sa_column=Column('date', Integer))


class ArXivMonitorKlog(SQLModel, table=True):
    t: int = Field(sa_column=Column('t', Integer, primary_key=True, server_default=text("'0'")))
    sent: Optional[int] = Field(default=None, sa_column=Column('sent', Integer))


class ArXivMonitorMailq(SQLModel, table=True):
    t: int = Field(sa_column=Column('t', Integer, primary_key=True, server_default=text("'0'")))
    main_q: int = Field(sa_column=Column('main_q', Integer, nullable=False, server_default=text("'0'")))
    local_q: int = Field(sa_column=Column('local_q', Integer, nullable=False, server_default=text("'0'")))
    local_host_map: int = Field(sa_column=Column('local_host_map', Integer, nullable=False, server_default=text("'0'")))
    local_timeout: int = Field(sa_column=Column('local_timeout', Integer, nullable=False, server_default=text("'0'")))
    local_refused: int = Field(sa_column=Column('local_refused', Integer, nullable=False, server_default=text("'0'")))
    local_in_flight: int = Field(sa_column=Column('local_in_flight', Integer, nullable=False, server_default=text("'0'")))


class ArXivMonitorMailsent(SQLModel, table=True):
    t: int = Field(sa_column=Column('t', Integer, primary_key=True, server_default=text("'0'")))
    sent: Optional[int] = Field(default=None, sa_column=Column('sent', Integer))


class ArXivNextMail(SQLModel, table=True):
    __table_args__ = (
        Index('arXiv_next_mail_idx_document_id', 'document_id'),
        Index('arXiv_next_mail_idx_document_id_version', 'document_id', 'version')
    )

    next_mail_id: Optional[int] = Field(default=None, sa_column=Column('next_mail_id', Integer, primary_key=True))
    submission_id: int = Field(sa_column=Column('submission_id', Integer, nullable=False))
    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    version: int = Field(sa_column=Column('version', Integer, nullable=False, server_default=text("'1'")))
    type: str = Field(sa_column=Column('type', String(255), nullable=False, server_default=text("'new'")))
    is_written: int = Field(sa_column=Column('is_written', Boolean(), nullable=False, server_default=text("'0'")))
    paper_id: Optional[str] = Field(default=None, sa_column=Column('paper_id', String(20)))
    extra: Optional[str] = Field(default=None, sa_column=Column('extra', String(255)))
    mail_id: Optional[str] = Field(default=None, sa_column=Column('mail_id', CHAR(6)))


class ArXivOrcidConfig(SQLModel, table=True):
    domain: Optional[str] = Field(default=None, sa_column=Column('domain', String(75), primary_key=True, nullable=False))
    keyname: Optional[str] = Field(default=None, sa_column=Column('keyname', String(60), primary_key=True, nullable=False))
    value: Optional[str] = Field(default=None, sa_column=Column('value', String(150)))


t_arXiv_ownership_requests_papers = Table(
    'arXiv_ownership_requests_papers', metadata,
    Column('request_id', Integer, nullable=False, server_default=text("'0'")),
    Column('document_id', Integer, nullable=False, server_default=text("'0'")),
    Index('document_id', 'document_id'),
    Index('request_id', 'request_id', 'document_id', unique=True)
)


class ArXivPaperSessions(SQLModel, table=True):
    paper_session_id: Optional[int] = Field(default=None, sa_column=Column('paper_session_id', Integer, primary_key=True))
    paper_id: str = Field(sa_column=Column('paper_id', String(16), nullable=False, server_default=text("''")))
    start_time: int = Field(sa_column=Column('start_time', Integer, nullable=False, server_default=text("'0'")))
    end_time: int = Field(sa_column=Column('end_time', Integer, nullable=False, server_default=text("'0'")))
    ip_name: str = Field(sa_column=Column('ip_name', String(16), nullable=False, server_default=text("''")))


class ArXivPublishLog(SQLModel, table=True):
    date_: int = Field(sa_column=Column('date', Integer, primary_key=True, server_default=text("'0'")))


t_arXiv_refresh_list = Table(
    'arXiv_refresh_list', metadata,
    Column('filename', String(255)),
    Column('mtime', Integer),
    Index('arXiv_refresh_list_mtime', 'mtime')
)


class ArXivRejectSessionUsernames(SQLModel, table=True):
    username: Optional[str] = Field(default=None, sa_column=Column('username', String(64), primary_key=True, server_default=text("''")))


class ArXivSciencewisePings(SQLModel, table=True):
    paper_id_v: Optional[str] = Field(default=None, sa_column=Column('paper_id_v', String(32), primary_key=True))
    updated: Optional[datetime] = Field(default=None, sa_column=Column('updated', DateTime))


class ArXivState(SQLModel, table=True):
    id: int = Field(sa_column=Column('id', Integer, primary_key=True))
    name: Optional[str] = Field(default=None, sa_column=Column('name', String(24)))
    value: Optional[str] = Field(default=None, sa_column=Column('value', String(24)))


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


class ArXivStatsMonthlyDownloads(SQLModel, table=True):
    ym: Optional[date] = Field(default=None, sa_column=Column('ym', Date, primary_key=True))
    downloads: int = Field(sa_column=Column('downloads', Integer, nullable=False))


class ArXivStatsMonthlySubmissions(SQLModel, table=True):
    ym: Optional[date] = Field(default=None, sa_column=Column('ym', Date, primary_key=True, server_default=text("'0000-00-00'")))
    num_submissions: int = Field(sa_column=Column('num_submissions', SmallInteger, nullable=False))
    historical_delta: int = Field(sa_column=Column('historical_delta', SmallInteger, nullable=False, server_default=text("'0'")))


class ArXivSubmissionAgreements(SQLModel, table=True):
    agreement_id: Optional[int] = Field(default=None, sa_column=Column('agreement_id', SmallInteger, primary_key=True))
    commit_ref: str = Field(sa_column=Column('commit_ref', String(255), nullable=False))
    effective_date: Optional[datetime] = Field(default=None, sa_column=Column('effective_date', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    content: Optional[str] = Field(default=None, sa_column=Column('content', Text))

    arXiv_submissions: List['ArXivSubmissions'] = Relationship(back_populates='agreement')


class ArXivSubmitterFlags(SQLModel, table=True):
    flag_id: int = Field(sa_column=Column('flag_id', Integer, primary_key=True))
    comment: Optional[str] = Field(default=None, sa_column=Column('comment', String(255)))
    pattern: Optional[str] = Field(default=None, sa_column=Column('pattern', String(255)))


class ArXivSuspectEmails(SQLModel, table=True):
    id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
    type: str = Field(sa_column=Column('type', String(10), nullable=False))
    pattern: str = Field(sa_column=Column('pattern', Text, nullable=False))
    comment: str = Field(sa_column=Column('comment', Text, nullable=False))
    updated: datetime = Field(sa_column=Column('updated', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))


class ArXivTitles(SQLModel, table=True):
    __table_args__ = (
        Index('arXiv_repno_idx', 'report_num'),
        Index('arXiv_titles_idx', 'title')
    )

    paper_id: Optional[str] = Field(default=None, sa_column=Column('paper_id', String(64), primary_key=True))
    title: Optional[str] = Field(default=None, sa_column=Column('title', String(255)))
    report_num: Optional[str] = Field(default=None, sa_column=Column('report_num', String(255)))
    date_: Optional[date] = Field(default=None, sa_column=Column('date', Date))


class ArXivTrackbackPings(SQLModel, table=True):
    __table_args__ = (
        Index('arXiv_trackback_pings__document_id', 'document_id'),
        Index('arXiv_trackback_pings__posted_date', 'posted_date'),
        Index('arXiv_trackback_pings__status', 'status'),
        Index('arXiv_trackback_pings__url', 'url')
    )

    trackback_id: Optional[int] = Field(default=None, sa_column=Column('trackback_id', Integer, primary_key=True))
    title: str = Field(sa_column=Column('title', String(255), nullable=False, server_default=text("''")))
    excerpt: str = Field(sa_column=Column('excerpt', String(255), nullable=False, server_default=text("''")))
    url: str = Field(sa_column=Column('url', String(255), nullable=False, server_default=text("''")))
    blog_name: str = Field(sa_column=Column('blog_name', String(255), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    remote_addr: str = Field(sa_column=Column('remote_addr', String(16), nullable=False, server_default=text("''")))
    posted_date: int = Field(sa_column=Column('posted_date', Integer, nullable=False, server_default=text("'0'")))
    is_stale: int = Field(sa_column=Column('is_stale', Boolean, nullable=False, server_default=text("'0'")))
    approved_by_user: int = Field(sa_column=Column('approved_by_user', Integer, nullable=False, server_default=text("'0'")))
    approved_time: int = Field(sa_column=Column('approved_time', Integer, nullable=False, server_default=text("'0'")))
    status: str = Field(sa_column=Column('status', Enum('pending', 'pending2', 'accepted', 'rejected', 'spam'), nullable=False, server_default=text("'pending'")))
    document_id: Optional[int] = Field(default=None, sa_column=Column('document_id', Integer))
    site_id: Optional[int] = Field(default=None, sa_column=Column('site_id', Integer))


class ArXivTrackbackSites(SQLModel, table=True):
    __table_args__ = (
        Index('arXiv_trackback_sites__pattern', 'pattern'),
    )

    pattern: str = Field(sa_column=Column('pattern', String(255), nullable=False, server_default=text("''")))
    site_id: Optional[int] = Field(default=None, sa_column=Column('site_id', Integer, primary_key=True))
    action: str = Field(sa_column=Column('action', Enum('neutral', 'accept', 'reject', 'spam'), nullable=False, server_default=text("'neutral'")))


class ArXivTracking(SQLModel, table=True):
    __table_args__ = (
        Index('sword_id', 'sword_id', unique=True),
    )

    tracking_id: Optional[int] = Field(default=None, sa_column=Column('tracking_id', Integer, primary_key=True))
    sword_id: int = Field(sa_column=Column('sword_id', Integer, nullable=False, server_default=text("'00000000'")))
    paper_id: str = Field(sa_column=Column('paper_id', String(32), nullable=False))
    timestamp: datetime = Field(sa_column=Column('timestamp', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP')))
    submission_errors: Optional[str] = Field(default=None, sa_column=Column('submission_errors', Text))

    arXiv_submissions: List['ArXivSubmissions'] = Relationship(back_populates='sword')


t_arXiv_updates = Table(
    'arXiv_updates', metadata,
    Column('document_id', Integer),
    Column('version', Integer, nullable=False, server_default=text("'1'")),
    Column('date', Date),
    Column('action', Enum('new', 'replace', 'absonly', 'cross', 'repcro')),
    Column('archive', String(20)),
    Column('category', String(20)),
    Index('archive_index', 'archive'),
    Index('category_index', 'category'),
    Index('date_index', 'date'),
    Index('document_id', 'document_id', 'date', 'action', 'category', unique=True),
    Index('document_id_index', 'document_id')
)


t_arXiv_updates_tmp = Table(
    'arXiv_updates_tmp', metadata,
    Column('document_id', Integer),
    Column('date', Date),
    Column('action', Enum('new', 'replace', 'absonly', 'cross', 'repcro')),
    Column('category', String(20)),
    Index('document_id', 'document_id', 'date', 'action', 'category', unique=True)
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
    Index('control_id', 'control_id'),
    Index('status', 'status')
)


class DbixClassSchemaVersions(SQLModel, table=True):
    version: Optional[str] = Field(default=None, sa_column=Column('version', String(10), primary_key=True))
    installed: str = Field(sa_column=Column('installed', String(20), nullable=False))


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


class Sessions(SQLModel, table=True):
    id: Optional[str] = Field(default=None, sa_column=Column('id', CHAR(72), primary_key=True))
    session_data: Optional[str] = Field(default=None, sa_column=Column('session_data', Text))
    expires: Optional[int] = Field(default=None, sa_column=Column('expires', Integer))


class TapirCountries(SQLModel, table=True):
    digraph: Optional[str] = Field(default=None, sa_column=Column('digraph', CHAR(2), primary_key=True, server_default=text("''")))
    country_name: str = Field(sa_column=Column('country_name', String(255), nullable=False, server_default=text("''")))
    rank: int = Field(sa_column=Column('rank', Integer, nullable=False, server_default=text("'255'")))

    tapir_address: List['TapirAddress'] = Relationship(back_populates='tapir_countries')
    tapir_demographics: List['TapirDemographics'] = Relationship(back_populates='tapir_countries')


class TapirEmailLog(SQLModel, table=True):
    __table_args__ = (
        Index('mailing_id', 'mailing_id'),
    )

    mail_id: Optional[int] = Field(default=None, sa_column=Column('mail_id', Integer, primary_key=True))
    sent_date: int = Field(sa_column=Column('sent_date', Integer, nullable=False, server_default=text("'0'")))
    template_id: int = Field(sa_column=Column('template_id', Integer, nullable=False, server_default=text("'0'")))
    reference_type: Optional[str] = Field(default=None, sa_column=Column('reference_type', CHAR(1)))
    reference_id: Optional[int] = Field(default=None, sa_column=Column('reference_id', Integer))
    email: Optional[str] = Field(default=None, sa_column=Column('email', String(255)))
    flag_bounced: Optional[int] = Field(default=None, sa_column=Column('flag_bounced', Integer))
    mailing_id: Optional[int] = Field(default=None, sa_column=Column('mailing_id', Integer))


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
    Index('error_date', 'error_date'),
    Index('ip_addr', 'ip_addr'),
    Index('message', 'message'),
    Index('session_id', 'session_id'),
    Index('tracking_cookie', 'tracking_cookie'),
    Index('user_id', 'user_id')
)


class TapirIntegerVariables(SQLModel, table=True):
    variable_id: Optional[str] = Field(default=None, sa_column=Column('variable_id', String(32), primary_key=True, server_default=text("''")))
    value: int = Field(sa_column=Column('value', Integer, nullable=False, server_default=text("'0'")))


class TapirNicknamesAudit(SQLModel, table=True):
    __table_args__ = (
        Index('creation_date', 'creation_date'),
        Index('creation_ip_num', 'creation_ip_num'),
        Index('tracking_cookie', 'tracking_cookie')
    )

    nick_id: int = Field(sa_column=Column('nick_id', Integer, primary_key=True, server_default=text("'0'")))
    creation_date: int = Field(sa_column=Column('creation_date', Integer, nullable=False, server_default=text("'0'")))
    creation_ip_num: str = Field(sa_column=Column('creation_ip_num', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))


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


class TapirPolicyClasses(SQLModel, table=True):
    class_id: Optional[int] = Field(default=None, sa_column=Column('class_id', SmallInteger, primary_key=True))
    name: str = Field(sa_column=Column('name', String(64), nullable=False, server_default=text("''")))
    description: str = Field(sa_column=Column('description', Text, nullable=False))
    password_storage: int = Field(sa_column=Column('password_storage', Integer, nullable=False, server_default=text("'0'")))
    recovery_policy: int = Field(sa_column=Column('recovery_policy', Integer, nullable=False, server_default=text("'0'")))
    permanent_login: int = Field(sa_column=Column('permanent_login', Integer, nullable=False, server_default=text("'0'")))

    tapir_users: List['TapirUsers'] = Relationship(back_populates='tapir_policy_classes')


class TapirPresessions(SQLModel, table=True):
    presession_id: Optional[int] = Field(default=None, sa_column=Column('presession_id', Integer, primary_key=True))
    ip_num: str = Field(sa_column=Column('ip_num', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))
    created_at: int = Field(sa_column=Column('created_at', Integer, nullable=False, server_default=text("'0'")))


class TapirStringVariables(SQLModel, table=True):
    variable_id: Optional[str] = Field(default=None, sa_column=Column('variable_id', String(32), primary_key=True, server_default=text("''")))
    value: str = Field(sa_column=Column('value', Text, nullable=False))


class TapirStrings(SQLModel, table=True):
    name: Optional[str] = Field(default=None, sa_column=Column('name', String(32), primary_key=True, nullable=False, server_default=text("''")))
    module: Optional[str] = Field(default=None, sa_column=Column('module', String(32), primary_key=True, nullable=False, server_default=text("''")))
    language: Optional[str] = Field(default=None, sa_column=Column('language', String(32), primary_key=True, nullable=False, server_default=text("'en'")))
    string: str = Field(sa_column=Column('string', Text, nullable=False))


class SubscriptionUniversalInstitutionContact(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['sid'], ['Subscription_UniversalInstitution.id'], ondelete='CASCADE', name='Subscription_Institution_Contact_Universal'),
        Index('sid', 'sid')
    )

    sid: int = Field(sa_column=Column('sid', Integer, nullable=False))
    id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
    email: Optional[str] = Field(default=None, sa_column=Column('email', String(255)))
    active: Optional[int] = Field(default=None, sa_column=Column('active', Boolean, server_default=text("'0'")))
    contact_name: Optional[str] = Field(default=None, sa_column=Column('contact_name', String(255)))
    phone: Optional[str] = Field(default=None, sa_column=Column('phone', String(255)))
    note: Optional[str] = Field(default=None, sa_column=Column('note', String(2048)))

    Subscription_UniversalInstitution: Optional['SubscriptionUniversalInstitution'] = Relationship(back_populates='Subscription_UniversalInstitutionContact')


class SubscriptionUniversalInstitutionIP(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['sid'], ['Subscription_UniversalInstitution.id'], ondelete='CASCADE', name='Subscription_Institution_IP_Universal'),
        Index('end', 'end'),
        Index('ip', 'start', 'end'),
        Index('sid', 'sid'),
        Index('start', 'start')
    )

    sid: int = Field(sa_column=Column('sid', Integer, nullable=False))
    id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
    end: int = Field(sa_column=Column('end', BigInteger, nullable=False))
    start: int = Field(sa_column=Column('start', BigInteger, nullable=False))
    exclude: Optional[int] = Field(default=None, sa_column=Column('exclude', Boolean, server_default=text("'0'")))

    Subscription_UniversalInstitution: Optional['SubscriptionUniversalInstitution'] = Relationship(back_populates='Subscription_UniversalInstitutionIP')


class ArXivArchives(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['in_group'], ['arXiv_groups.group_id'], name='0_576'),
        Index('in_group', 'in_group')
    )

    archive_id: Optional[str] = Field(default=None, sa_column=Column('archive_id', String(16), primary_key=True, server_default=text("''")))
    in_group: str = Field(sa_column=Column('in_group', String(16), nullable=False, server_default=text("''")))
    archive_name: str = Field(sa_column=Column('archive_name', String(255), nullable=False, server_default=text("''")))
    start_date: str = Field(sa_column=Column('start_date', String(4), nullable=False, server_default=text("''")))
    end_date: str = Field(sa_column=Column('end_date', String(4), nullable=False, server_default=text("''")))
    subdivided: int = Field(sa_column=Column('subdivided', Integer, nullable=False, server_default=text("'0'")))

    arXiv_groups: Optional['ArXivGroups'] = Relationship(back_populates='arXiv_archives')
    arXiv_categories: List['ArXivCategories'] = Relationship(back_populates='arXiv_archives')


t_tapir_save_post_variables = Table(
    'tapir_save_post_variables', metadata,
    Column('presession_id', Integer, nullable=False, server_default=text("'0'")),
    Column('name', String(255)),
    Column('value', Text, nullable=False),
    Column('seq', Integer, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['presession_id'], ['tapir_presessions.presession_id'], name='0_558'),
    Index('presession_id', 'presession_id')
)


class TapirUsers(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['policy_class'], ['tapir_policy_classes.class_id'], name='0_510'),
        Index('email', 'email', unique=True),
        Index('first_name', 'first_name'),
        Index('flag_approved', 'flag_approved'),
        Index('flag_banned', 'flag_banned'),
        Index('flag_can_lock', 'flag_can_lock'),
        Index('flag_deleted', 'flag_deleted'),
        Index('flag_edit_users', 'flag_edit_users'),
        Index('flag_internal', 'flag_internal'),
        Index('joined_date', 'joined_date'),
        Index('joined_ip_num', 'joined_ip_num'),
        Index('last_name', 'last_name'),
        Index('policy_class', 'policy_class'),
        Index('tracking_cookie', 'tracking_cookie')
    )

    user_id: Optional[int] = Field(default=None, sa_column=Column('user_id', Integer, primary_key=True))
    share_first_name: int = Field(sa_column=Column('share_first_name', Integer, nullable=False, server_default=text("'1'")))
    share_last_name: int = Field(sa_column=Column('share_last_name', Integer, nullable=False, server_default=text("'1'")))
    email: str = Field(sa_column=Column('email', String(255), nullable=False, server_default=text("''")))
    share_email: int = Field(sa_column=Column('share_email', Integer, nullable=False, server_default=text("'8'")))
    email_bouncing: int = Field(sa_column=Column('email_bouncing', Integer, nullable=False, server_default=text("'0'")))
    policy_class: int = Field(sa_column=Column('policy_class', SmallInteger, nullable=False, server_default=text("'0'")))
    joined_date: int = Field(sa_column=Column('joined_date', Integer, nullable=False, server_default=text("'0'")))
    joined_remote_host: str = Field(sa_column=Column('joined_remote_host', String(255), nullable=False, server_default=text("''")))
    flag_internal: int = Field(sa_column=Column('flag_internal', Integer, nullable=False, server_default=text("'0'")))
    flag_edit_users: int = Field(sa_column=Column('flag_edit_users', Integer, nullable=False, server_default=text("'0'")))
    flag_edit_system: int = Field(sa_column=Column('flag_edit_system', Integer, nullable=False, server_default=text("'0'")))
    flag_email_verified: int = Field(sa_column=Column('flag_email_verified', Integer, nullable=False, server_default=text("'0'")))
    flag_approved: int = Field(sa_column=Column('flag_approved', Integer, nullable=False, server_default=text("'1'")))
    flag_deleted: int = Field(sa_column=Column('flag_deleted', Integer, nullable=False, server_default=text("'0'")))
    flag_banned: int = Field(sa_column=Column('flag_banned', Integer, nullable=False, server_default=text("'0'")))
    flag_wants_email: int = Field(sa_column=Column('flag_wants_email', Integer, nullable=False, server_default=text("'0'")))
    flag_html_email: int = Field(sa_column=Column('flag_html_email', Integer, nullable=False, server_default=text("'0'")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))
    flag_allow_tex_produced: int = Field(sa_column=Column('flag_allow_tex_produced', Integer, nullable=False, server_default=text("'0'")))
    flag_can_lock: int = Field(sa_column=Column('flag_can_lock', Integer, nullable=False, server_default=text("'0'")))
    first_name: Optional[str] = Field(default=None, sa_column=Column('first_name', String(50)))
    last_name: Optional[str] = Field(default=None, sa_column=Column('last_name', String(50)))
    suffix_name: Optional[str] = Field(default=None, sa_column=Column('suffix_name', String(50)))
    joined_ip_num: Optional[str] = Field(default=None, sa_column=Column('joined_ip_num', String(16)))

    tapir_policy_classes: Optional['TapirPolicyClasses'] = Relationship(back_populates='tapir_users')
    arXiv_control_holds: List['ArXivControlHolds'] = Relationship(back_populates='tapir_users')
    arXiv_control_holds_: List['ArXivControlHolds'] = Relationship(back_populates='tapir_users_')
    arXiv_documents: List['ArXivDocuments'] = Relationship(back_populates='submitter')
    arXiv_moderator_api_key: List['ArXivModeratorApiKey'] = Relationship(back_populates='user')
    tapir_address: List['TapirAddress'] = Relationship(back_populates='user')
    tapir_email_change_tokens: List['TapirEmailChangeTokens'] = Relationship(back_populates='user')
    tapir_email_templates: List['TapirEmailTemplates'] = Relationship(back_populates='tapir_users')
    tapir_email_templates_: List['TapirEmailTemplates'] = Relationship(back_populates='tapir_users_')
    tapir_email_tokens: List['TapirEmailTokens'] = Relationship(back_populates='user')
    tapir_nicknames: List['TapirNicknames'] = Relationship(back_populates='user')
    tapir_phone: List['TapirPhone'] = Relationship(back_populates='user')
    tapir_recovery_tokens: List['TapirRecoveryTokens'] = Relationship(back_populates='user')
    tapir_sessions: List['TapirSessions'] = Relationship(back_populates='user')
    arXiv_cross_control: List['ArXivCrossControl'] = Relationship(back_populates='user')
    arXiv_endorsement_requests: List['ArXivEndorsementRequests'] = Relationship(back_populates='endorsee')
    arXiv_jref_control: List['ArXivJrefControl'] = Relationship(back_populates='user')
    arXiv_metadata: List['ArXivMetadata'] = Relationship(back_populates='submitter')
    arXiv_show_email_requests: List['ArXivShowEmailRequests'] = Relationship(back_populates='user')
    arXiv_submission_control: List['ArXivSubmissionControl'] = Relationship(back_populates='user')
    arXiv_submissions: List['ArXivSubmissions'] = Relationship(back_populates='submitter')
    tapir_admin_audit: List['TapirAdminAudit'] = Relationship(back_populates='tapir_users')
    tapir_admin_audit_: List['TapirAdminAudit'] = Relationship(back_populates='tapir_users_')
    tapir_email_mailings: List['TapirEmailMailings'] = Relationship(back_populates='tapir_users')
    tapir_email_mailings_: List['TapirEmailMailings'] = Relationship(back_populates='tapir_users_')
    tapir_permanent_tokens: List['TapirPermanentTokens'] = Relationship(back_populates='user')
    tapir_recovery_tokens_used: List['TapirRecoveryTokensUsed'] = Relationship(back_populates='user')
    arXiv_endorsements: List['ArXivEndorsements'] = Relationship(back_populates='endorsee')
    arXiv_endorsements_: List['ArXivEndorsements'] = Relationship(back_populates='endorser')
    arXiv_ownership_requests: List['ArXivOwnershipRequests'] = Relationship(back_populates='user')
    arXiv_submission_category_proposal: List['ArXivSubmissionCategoryProposal'] = Relationship(back_populates='user')
    arXiv_submission_flag: List['ArXivSubmissionFlag'] = Relationship(back_populates='user')
    arXiv_submission_hold_reason: List['ArXivSubmissionHoldReason'] = Relationship(back_populates='user')
    arXiv_submission_view_flag: List['ArXivSubmissionViewFlag'] = Relationship(back_populates='user')


class ArXivAuthorIds(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_author_ids_ibfk_1'),
        Index('author_id', 'author_id')
    )

    user_id_x: int = Field(alias='user_id', sa_column=Column('user_id', Integer, primary_key=True))
    author_id: str = Field(sa_column=Column('author_id', String(50), nullable=False))
    updated: datetime = Field(sa_column=Column('updated', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP')))


t_arXiv_bad_pw = Table(
    'arXiv_bad_pw', metadata,
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_601'),
    Index('user_id', 'user_id')
)


class ArXivCategories(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['archive'], ['arXiv_archives.archive_id'], name='0_578'),
        ForeignKeyConstraint(['endorsement_domain'], ['arXiv_endorsement_domains.endorsement_domain'], name='0_753'),
        Index('endorsement_domain', 'endorsement_domain')
    )

    archive: Optional[str] = Field(default=None, sa_column=Column('archive', String(16), primary_key=True, nullable=False, server_default=text("''")))
    subject_class: Optional[str] = Field(default=None, sa_column=Column('subject_class', String(16), primary_key=True, nullable=False, server_default=text("''")))
    definitive: int = Field(sa_column=Column('definitive', Integer, nullable=False, server_default=text("'0'")))
    active: int = Field(sa_column=Column('active', Integer, nullable=False, server_default=text("'0'")))
    endorse_all: str = Field(sa_column=Column('endorse_all', Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'")))
    endorse_email: str = Field(sa_column=Column('endorse_email', Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'")))
    papers_to_endorse: int = Field(sa_column=Column('papers_to_endorse', SmallInteger, nullable=False, server_default=text("'0'")))
    category_name: Optional[str] = Field(default=None, sa_column=Column('category_name', String(255)))
    endorsement_domain: Optional[str] = Field(default=None, sa_column=Column('endorsement_domain', String(32)))

    arXiv_archives: Optional['ArXivArchives'] = Relationship(back_populates='arXiv_categories')
    arXiv_endorsement_domains: Optional['ArXivEndorsementDomains'] = Relationship(back_populates='arXiv_categories')
    arXiv_cross_control: List['ArXivCrossControl'] = Relationship(back_populates='arXiv_categories')
    arXiv_demographics: List['ArXivDemographics'] = Relationship(back_populates='arXiv_categories')
    arXiv_endorsement_requests: List['ArXivEndorsementRequests'] = Relationship(back_populates='arXiv_categories')
    arXiv_endorsements: List['ArXivEndorsements'] = Relationship(back_populates='arXiv_categories')


class ArXivControlHolds(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['last_changed_by'], ['tapir_users.user_id'], name='arXiv_control_holds_ibfk_2'),
        ForeignKeyConstraint(['placed_by'], ['tapir_users.user_id'], name='arXiv_control_holds_ibfk_1'),
        Index('control_id', 'control_id', 'hold_type', unique=True),
        Index('hold_reason', 'hold_reason'),
        Index('hold_status', 'hold_status'),
        Index('hold_type', 'hold_type'),
        Index('last_changed_by', 'last_changed_by'),
        Index('origin', 'origin'),
        Index('placed_by', 'placed_by')
    )

    hold_id: Optional[int] = Field(default=None, sa_column=Column('hold_id', Integer, primary_key=True))
    control_id: int = Field(sa_column=Column('control_id', Integer, nullable=False, server_default=text("'0'")))
    hold_type: str = Field(sa_column=Column('hold_type', Enum('submission', 'cross', 'jref'), nullable=False, server_default=text("'submission'")))
    hold_status: str = Field(sa_column=Column('hold_status', Enum('held', 'extended', 'accepted', 'rejected'), nullable=False, server_default=text("'held'")))
    hold_reason: str = Field(sa_column=Column('hold_reason', String(255), nullable=False, server_default=text("''")))
    hold_data: str = Field(sa_column=Column('hold_data', String(255), nullable=False, server_default=text("''")))
    origin: str = Field(sa_column=Column('origin', Enum('auto', 'user', 'admin', 'moderator'), nullable=False, server_default=text("'auto'")))
    placed_by: Optional[int] = Field(default=None, sa_column=Column('placed_by', Integer))
    last_changed_by: Optional[int] = Field(default=None, sa_column=Column('last_changed_by', Integer))

    tapir_users: Optional['TapirUsers'] = Relationship(back_populates='arXiv_control_holds')
    tapir_users_: Optional['TapirUsers'] = Relationship(back_populates='arXiv_control_holds_')


class ArXivDocuments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['submitter_id'], ['tapir_users.user_id'], name='0_580'),
        Index('dated', 'dated'),
        Index('paper_id', 'paper_id', unique=True),
        Index('submitter_email', 'submitter_email'),
        Index('submitter_id', 'submitter_id'),
        Index('title', 'title')
    )

    document_id: Optional[int] = Field(default=None, sa_column=Column('document_id', Integer, primary_key=True))
    paper_id: str = Field(sa_column=Column('paper_id', String(20), nullable=False, server_default=text("''")))
    title: str = Field(sa_column=Column('title', String(255), nullable=False, server_default=text("''")))
    submitter_email: str = Field(sa_column=Column('submitter_email', String(64), nullable=False, server_default=text("''")))
    dated: int = Field(sa_column=Column('dated', Integer, nullable=False, server_default=text("'0'")))
    authors: Optional[str] = Field(default=None, sa_column=Column('authors', Text))
    submitter_id: Optional[int] = Field(default=None, sa_column=Column('submitter_id', Integer))
    primary_subject_class: Optional[str] = Field(default=None, sa_column=Column('primary_subject_class', String(16)))
    created: Optional[datetime] = Field(default=None, sa_column=Column('created', DateTime))

    submitter: Optional['TapirUsers'] = Relationship(back_populates='arXiv_documents')
    arXiv_admin_metadata: List['ArXivAdminMetadata'] = Relationship(back_populates='document')
    arXiv_cross_control: List['ArXivCrossControl'] = Relationship(back_populates='document')
    arXiv_dblp_document_authors: List['ArXivDblpDocumentAuthors'] = Relationship(back_populates='document')
    arXiv_document_category: List['ArXivDocumentCategory'] = Relationship(back_populates='document')
    arXiv_jref_control: List['ArXivJrefControl'] = Relationship(back_populates='document')
    arXiv_metadata: List['ArXivMetadata'] = Relationship(back_populates='document')
    arXiv_mirror_list: List['ArXivMirrorList'] = Relationship(back_populates='document')
    arXiv_show_email_requests: List['ArXivShowEmailRequests'] = Relationship(back_populates='document')
    arXiv_submission_control: List['ArXivSubmissionControl'] = Relationship(back_populates='document')
    arXiv_submissions: List['ArXivSubmissions'] = Relationship(back_populates='document')
    arXiv_top_papers: List['ArXivTopPapers'] = Relationship(back_populates='document')
    arXiv_versions: List['ArXivVersions'] = Relationship(back_populates='document')


t_arXiv_duplicates = Table(
    'arXiv_duplicates', metadata,
    Column('user_id', Integer, nullable=False, server_default=text("'0'")),
    Column('email', String(255)),
    Column('username', String(255)),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_599'),
    Index('user_id', 'user_id')
)


class ArXivModeratorApiKey(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_moderator_api_key_ibfk_1'),
    )

    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    secret: Optional[str] = Field(default=None, sa_column=Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")))
    valid: int = Field(sa_column=Column('valid', Integer, nullable=False, server_default=text("'1'")))
    issued_when: int = Field(sa_column=Column('issued_when', Integer, nullable=False, server_default=text("'0'")))
    issued_to: str = Field(sa_column=Column('issued_to', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))

    user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_moderator_api_key')


class ArXivOrcidIds(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_orcid_ids_ibfk_1'),
        Index('orcid', 'orcid')
    )

    user_id_x: int = Field(alias="user_id", sa_column=Column('user_id', Integer, primary_key=True))
    orcid: str = Field(sa_column=Column('orcid', String(19), nullable=False))
    authenticated: int = Field(sa_column=Column('authenticated', Boolean(), nullable=False, server_default=text("'0'")))
    updated: datetime = Field(sa_column=Column('updated', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP')))


class ArXivQueueView(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_queue_view_ibfk_1'),
    )

    user_id_x: int = Field(alias='user_id', sa_column=Column('user_id', Integer, primary_key=True, server_default=text("'0'")))
    total_views: int = Field(sa_column=Column('total_views', Integer, nullable=False, server_default=text("'0'")))
    last_view: Optional[datetime] = Field(default=None, sa_column=Column('last_view', DateTime))
    second_last_view: Optional[datetime] = Field(default=None, sa_column=Column('second_last_view', DateTime))


class ArXivSuspiciousNames(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_606'),
    )

    user_id_x: int = Field(alias='user_id',sa_column=Column('user_id', Integer, primary_key=True, server_default=text("'0'")))
    full_name: str = Field(sa_column=Column('full_name', String(255), nullable=False, server_default=text("''")))


class ArXivSwordLicenses(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='user_id_fk'),
    )

    user_id_x: int = Field(alias='user_id',sa_column=Column('user_id', Integer, primary_key=True))
    updated: datetime = Field(sa_column=Column('updated', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))
    license: Optional[str] = Field(default=None, sa_column=Column('license', String(127)))


class TapirAddress(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['country'], ['tapir_countries.digraph'], name='0_523'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_522'),
        Index('address_type', 'address_type'),
        Index('city', 'city'),
        Index('country', 'country'),
        Index('postal_code', 'postal_code')
    )

    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    address_type: int = Field(sa_column=Column('address_type', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    company: str = Field(sa_column=Column('company', String(80), nullable=False, server_default=text("''")))
    line1: str = Field(sa_column=Column('line1', String(80), nullable=False, server_default=text("''")))
    line2: str = Field(sa_column=Column('line2', String(80), nullable=False, server_default=text("''")))
    city: str = Field(sa_column=Column('city', String(50), nullable=False, server_default=text("''")))
    state: str = Field(sa_column=Column('state', String(50), nullable=False, server_default=text("''")))
    postal_code: str = Field(sa_column=Column('postal_code', String(16), nullable=False, server_default=text("''")))
    country: str = Field(sa_column=Column('country', CHAR(2), nullable=False, server_default=text("''")))
    share_addr: int = Field(sa_column=Column('share_addr', Integer, nullable=False, server_default=text("'0'")))

    tapir_countries: Optional['TapirCountries'] = Relationship(back_populates='tapir_address')
    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_address')


class TapirDemographics(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['country'], ['tapir_countries.digraph'], name='0_518'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_517'),
        Index('birthday', 'birthday'),
        Index('country', 'country'),
        Index('postal_code', 'postal_code')
    )

    user_id_x: int = Field(alias='user_id',sa_column=Column('user_id', Integer, primary_key=True, server_default=text("'0'")))
    gender: int = Field(sa_column=Column('gender', Integer, nullable=False, server_default=text("'0'")))
    share_gender: int = Field(sa_column=Column('share_gender', Integer, nullable=False, server_default=text("'16'")))
    share_birthday: int = Field(sa_column=Column('share_birthday', Integer, nullable=False, server_default=text("'16'")))
    country: str = Field(sa_column=Column('country', CHAR(2), nullable=False, server_default=text("''")))
    share_country: int = Field(sa_column=Column('share_country', Integer, nullable=False, server_default=text("'16'")))
    postal_code: str = Field(sa_column=Column('postal_code', String(16), nullable=False, server_default=text("''")))
    birthday: Optional[date] = Field(default=None, sa_column=Column('birthday', Date))

    tapir_countries: Optional['TapirCountries'] = Relationship(back_populates='tapir_demographics')


class TapirEmailChangeTokens(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_535'),
        Index('secret', 'secret')
    )

    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    secret: Optional[str] = Field(default=None, sa_column=Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")))
    tapir_dest: str = Field(sa_column=Column('tapir_dest', String(255), nullable=False, server_default=text("''")))
    issued_when: int = Field(sa_column=Column('issued_when', Integer, nullable=False, server_default=text("'0'")))
    issued_to: str = Field(sa_column=Column('issued_to', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(16), nullable=False, server_default=text("''")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))
    used: int = Field(sa_column=Column('used', Integer, nullable=False, server_default=text("'0'")))
    session_id: int = Field(sa_column=Column('session_id', Integer, nullable=False, server_default=text("'0'")))
    old_email: Optional[str] = Field(default=None, sa_column=Column('old_email', String(255)))
    new_email: Optional[str] = Field(default=None, sa_column=Column('new_email', String(255)))
    consumed_when: Optional[int] = Field(default=None, sa_column=Column('consumed_when', Integer))
    consumed_from: Optional[str] = Field(default=None, sa_column=Column('consumed_from', String(16)))

    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_email_change_tokens')


class TapirEmailTemplates(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['tapir_users.user_id'], name='0_560'),
        ForeignKeyConstraint(['updated_by'], ['tapir_users.user_id'], name='0_561'),
        Index('created_by', 'created_by'),
        Index('short_name', 'short_name', 'lang', unique=True),
        Index('update_date', 'update_date'),
        Index('updated_by', 'updated_by')
    )

    template_id: Optional[int] = Field(default=None, sa_column=Column('template_id', Integer, primary_key=True))
    short_name: str = Field(sa_column=Column('short_name', String(32), nullable=False, server_default=text("''")))
    lang: str = Field(sa_column=Column('lang', CHAR(2), nullable=False, server_default=text("'en'")))
    long_name: str = Field(sa_column=Column('long_name', String(255), nullable=False, server_default=text("''")))
    data: str = Field(sa_column=Column('data', Text, nullable=False))
    sql_statement: str = Field(sa_column=Column('sql_statement', Text, nullable=False))
    update_date: int = Field(sa_column=Column('update_date', Integer, nullable=False, server_default=text("'0'")))
    created_by: int = Field(sa_column=Column('created_by', Integer, nullable=False, server_default=text("'0'")))
    updated_by: int = Field(sa_column=Column('updated_by', Integer, nullable=False, server_default=text("'0'")))
    workflow_status: int = Field(sa_column=Column('workflow_status', Integer, nullable=False, server_default=text("'0'")))
    flag_system: int = Field(sa_column=Column('flag_system', Integer, nullable=False, server_default=text("'0'")))

    tapir_users: Optional['TapirUsers'] = Relationship(back_populates='tapir_email_templates')
    tapir_users_: Optional['TapirUsers'] = Relationship(back_populates='tapir_email_templates_')
    tapir_email_headers: List['TapirEmailHeaders'] = Relationship(back_populates='template')
    tapir_email_mailings: List['TapirEmailMailings'] = Relationship(back_populates='template')


class TapirEmailTokens(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_530'),
        Index('secret', 'secret')
    )

    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    secret: Optional[str] = Field(default=None, sa_column=Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")))
    tapir_dest: str = Field(sa_column=Column('tapir_dest', String(255), nullable=False, server_default=text("''")))
    issued_when: int = Field(sa_column=Column('issued_when', Integer, nullable=False, server_default=text("'0'")))
    issued_to: str = Field(sa_column=Column('issued_to', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))
    wants_perm_token: int = Field(sa_column=Column('wants_perm_token', Integer, nullable=False, server_default=text("'0'")))

    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_email_tokens')


class TapirNicknames(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_570'),
        Index('flag_valid', 'flag_valid'),
        Index('nickname', 'nickname', unique=True),
        Index('policy', 'policy'),
        Index('role', 'role'),
        Index('user_id', 'user_id', 'user_seq', unique=True)
    )

    nick_id: Optional[int] = Field(default=None, sa_column=Column('nick_id', Integer, primary_key=True))
    nickname: str = Field(sa_column=Column('nickname', String(20), nullable=False, server_default=text("''")))
    user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False, server_default=text("'0'")))
    user_seq: int = Field(sa_column=Column('user_seq', Integer, nullable=False, server_default=text("'0'")))
    flag_valid: int = Field(sa_column=Column('flag_valid', Integer, nullable=False, server_default=text("'0'")))
    role: int = Field(sa_column=Column('role', Integer, nullable=False, server_default=text("'0'")))
    policy: int = Field(sa_column=Column('policy', Integer, nullable=False, server_default=text("'0'")))
    flag_primary: int = Field(sa_column=Column('flag_primary', Integer, nullable=False, server_default=text("'0'")))

    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_nicknames')


class TapirPhone(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_520'),
        Index('phone_number', 'phone_number'),
        Index('phone_type', 'phone_type')
    )

    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    phone_type: int = Field(sa_column=Column('phone_type', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    share_phone: int = Field(sa_column=Column('share_phone', Integer, nullable=False, server_default=text("'16'")))
    phone_number: Optional[str] = Field(default=None, sa_column=Column('phone_number', String(32)))

    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_phone')


class TapirRecoveryTokens(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_546'),
        Index('secret', 'secret')
    )

    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    secret: Optional[str] = Field(default=None, sa_column=Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")))
    valid: int = Field(sa_column=Column('valid', Integer, nullable=False, server_default=text("'1'")))
    tapir_dest: str = Field(sa_column=Column('tapir_dest', String(255), nullable=False, server_default=text("''")))
    issued_when: int = Field(sa_column=Column('issued_when', Integer, nullable=False, server_default=text("'0'")))
    issued_to: str = Field(sa_column=Column('issued_to', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))

    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_recovery_tokens')


class TapirSessions(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_525'),
        Index('end_time', 'end_time'),
        Index('start_time', 'start_time'),
        Index('user_id', 'user_id')
    )

    session_id: Optional[int] = Field(default=None, sa_column=Column('session_id', Integer, primary_key=True))
    user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False, server_default=text("'0'")))
    last_reissue: int = Field(sa_column=Column('last_reissue', Integer, nullable=False, server_default=text("'0'")))
    start_time: int = Field(sa_column=Column('start_time', Integer, nullable=False, server_default=text("'0'")))
    end_time: int = Field(sa_column=Column('end_time', Integer, nullable=False, server_default=text("'0'")))

    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_sessions')
    tapir_admin_audit: List['TapirAdminAudit'] = Relationship(back_populates='session')
    tapir_permanent_tokens: List['TapirPermanentTokens'] = Relationship(back_populates='session')
    tapir_recovery_tokens_used: List['TapirRecoveryTokensUsed'] = Relationship(back_populates='session')


class TapirUsersHot(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_514'),
        Index('last_login', 'last_login'),
        Index('number_sessions', 'number_sessions'),
        Index('second_last_login', 'second_last_login')
    )

    user_id_x: int = Field(alias='user_id',sa_column=Column('user_id', Integer, primary_key=True, server_default=text("'0'")))
    last_login: int = Field(sa_column=Column('last_login', Integer, nullable=False, server_default=text("'0'")))
    second_last_login: int = Field(sa_column=Column('second_last_login', Integer, nullable=False, server_default=text("'0'")))
    number_sessions: int = Field(sa_column=Column('number_sessions', Integer, nullable=False, server_default=text("'0'")))


class TapirUsersPassword(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_512'),
    )

    user_id_x: int = Field(alias='user_id',sa_column=Column('user_id', Integer, primary_key=True, server_default=text("'0'")))
    password_storage: int = Field(sa_column=Column('password_storage', Integer, nullable=False, server_default=text("'0'")))
    password_enc: str = Field(sa_column=Column('password_enc', String(50), nullable=False, server_default=text("''")))


class ArXivAdminMetadata(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', name='meta_doc_fk'),
        Index('document_id', 'document_id'),
        Index('id', 'metadata_id'),
        Index('pidv', 'paper_id', 'version', unique=True)
    )

    metadata_id: Optional[int] = Field(default=None, sa_column=Column('metadata_id', Integer, primary_key=True))
    version: int = Field(sa_column=Column('version', Integer, nullable=False, server_default=text("'1'")))
    document_id: Optional[int] = Field(default=None, sa_column=Column('document_id', Integer))
    paper_id: Optional[str] = Field(default=None, sa_column=Column('paper_id', String(64)))
    created: Optional[datetime] = Field(default=None, sa_column=Column('created', DateTime))
    updated: Optional[datetime] = Field(default=None, sa_column=Column('updated', DateTime))
    submitter_name: Optional[str] = Field(default=None, sa_column=Column('submitter_name', String(64)))
    submitter_email: Optional[str] = Field(default=None, sa_column=Column('submitter_email', String(64)))
    history: Optional[str] = Field(default=None, sa_column=Column('history', Text))
    source_size: Optional[int] = Field(default=None, sa_column=Column('source_size', Integer))
    source_type: Optional[str] = Field(default=None, sa_column=Column('source_type', String(12)))
    title: Optional[str] = Field(default=None, sa_column=Column('title', Text))
    authors: Optional[str] = Field(default=None, sa_column=Column('authors', Text))
    category_string: Optional[str] = Field(default=None, sa_column=Column('category_string', String(255)))
    comments: Optional[str] = Field(default=None, sa_column=Column('comments', Text))
    proxy: Optional[str] = Field(default=None, sa_column=Column('proxy', String(255)))
    report_num: Optional[str] = Field(default=None, sa_column=Column('report_num', Text))
    msc_class: Optional[str] = Field(default=None, sa_column=Column('msc_class', String(255)))
    acm_class: Optional[str] = Field(default=None, sa_column=Column('acm_class', String(255)))
    journal_ref: Optional[str] = Field(default=None, sa_column=Column('journal_ref', Text))
    doi: Optional[str] = Field(default=None, sa_column=Column('doi', String(255)))
    abstract: Optional[str] = Field(default=None, sa_column=Column('abstract', Text))
    license: Optional[str] = Field(default=None, sa_column=Column('license', String(255)))
    modtime: Optional[int] = Field(default=None, sa_column=Column('modtime', Integer))
    is_current: Optional[int] = Field(default=None, sa_column=Column('is_current', Boolean(), server_default=text("'0'")))

    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_admin_metadata')


t_arXiv_bogus_subject_class = Table(
    'arXiv_bogus_subject_class', metadata,
    Column('document_id', Integer, nullable=False, server_default=text("'0'")),
    Column('category_name', String(255), nullable=False, server_default=text("''")),
    ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_604'),
    Index('document_id', 'document_id')
)


class ArXivCrossControl(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='arXiv_cross_control_ibfk_2'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_cross_control_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_cross_control_ibfk_3'),
        Index('archive', 'archive', 'subject_class'),
        Index('document_id', 'document_id', 'version'),
        Index('freeze_date', 'freeze_date'),
        Index('status', 'status'),
        Index('user_id', 'user_id')
    )

    control_id: Optional[int] = Field(default=None, sa_column=Column('control_id', Integer, primary_key=True))
    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    version: int = Field(sa_column=Column('version', SmallInteger, nullable=False, server_default=text("'0'")))
    desired_order: int = Field(sa_column=Column('desired_order', SmallInteger, nullable=False, server_default=text("'0'")))
    user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False, server_default=text("'0'")))
    status: str = Field(sa_column=Column('status', Enum('new', 'frozen', 'published', 'rejected'), nullable=False, server_default=text("'new'")))
    archive: str = Field(sa_column=Column('archive', String(16), nullable=False, server_default=text("''")))
    subject_class: str = Field(sa_column=Column('subject_class', String(16), nullable=False, server_default=text("''")))
    request_date: int = Field(sa_column=Column('request_date', Integer, nullable=False, server_default=text("'0'")))
    freeze_date: int = Field(sa_column=Column('freeze_date', Integer, nullable=False, server_default=text("'0'")))
    publish_date: int = Field(sa_column=Column('publish_date', Integer, nullable=False, server_default=text("'0'")))
    flag_must_notify: Optional[str] = Field(default=None, sa_column=Column('flag_must_notify', Enum('0', '1'), server_default=text("'1'")))

    arXiv_categories: Optional['ArXivCategories'] = Relationship(back_populates='arXiv_cross_control')
    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_cross_control')
    user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_cross_control')


class ArXivDblp(ArXivDocuments, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_DBLP_cdfk1'),
    )

    document_id_x: int = Field(alias='document_id',sa_column=Column('document_id', Integer, primary_key=True, server_default=text("'0'")))
    url: Optional[str] = Field(default=None, sa_column=Column('url', String(80)))


class ArXivDblpDocumentAuthors(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['author_id'], ['arXiv_dblp_authors.author_id'], name='arXiv_DBLP_ibfk2'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_DBLP_abfk1'),
        Index('author_id', 'author_id'),
        Index('document_id', 'document_id')
    )

    document_id: int = Field(sa_column=Column('document_id', Integer, primary_key=True, nullable=False))
    author_id: int = Field(sa_column=Column('author_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    position: int = Field(sa_column=Column('position', SmallInteger, nullable=False, server_default=text("'0'")))

    author: Optional['ArXivDblpAuthors'] = Relationship(back_populates='arXiv_dblp_document_authors')
    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_dblp_document_authors')


class ArXivDemographics(TapirUsers, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_588'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_587'),
        Index('archive', 'archive', 'subject_class'),
        Index('country', 'country'),
        Index('flag_group_cs', 'flag_group_cs'),
        Index('flag_group_econ', 'flag_group_econ'),
        Index('flag_group_eess', 'flag_group_eess'),
        Index('flag_group_math', 'flag_group_math'),
        Index('flag_group_nlin', 'flag_group_nlin'),
        Index('flag_group_physics', 'flag_group_physics'),
        Index('flag_group_q_bio', 'flag_group_q_bio'),
        Index('flag_group_q_fin', 'flag_group_q_fin'),
        Index('flag_group_stat', 'flag_group_stat'),
        Index('flag_journal', 'flag_journal'),
        Index('flag_proxy', 'flag_proxy'),
        Index('flag_suspect', 'flag_suspect'),
        Index('flag_xml', 'flag_xml'),
        Index('type', 'type')
    )

    user_id_x: int = Field(alias='user_id', sa_column=Column('user_id', Integer, primary_key=True, server_default=text("'0'")))
    country: str = Field(sa_column=Column('country', CHAR(2), nullable=False, server_default=text("''")))
    affiliation: str = Field(sa_column=Column('affiliation', String(255), nullable=False, server_default=text("''")))
    url: str = Field(sa_column=Column('url', String(255), nullable=False, server_default=text("''")))
    original_subject_classes: str = Field(sa_column=Column('original_subject_classes', String(255), nullable=False, server_default=text("''")))
    flag_group_math: int = Field(sa_column=Column('flag_group_math', Integer, nullable=False, server_default=text("'0'")))
    flag_group_cs: int = Field(sa_column=Column('flag_group_cs', Integer, nullable=False, server_default=text("'0'")))
    flag_group_nlin: int = Field(sa_column=Column('flag_group_nlin', Integer, nullable=False, server_default=text("'0'")))
    flag_proxy: int = Field(sa_column=Column('flag_proxy', Integer, nullable=False, server_default=text("'0'")))
    flag_journal: int = Field(sa_column=Column('flag_journal', Integer, nullable=False, server_default=text("'0'")))
    flag_xml: int = Field(sa_column=Column('flag_xml', Integer, nullable=False, server_default=text("'0'")))
    dirty: int = Field(sa_column=Column('dirty', Integer, nullable=False, server_default=text("'2'")))
    flag_group_test: int = Field(sa_column=Column('flag_group_test', Integer, nullable=False, server_default=text("'0'")))
    flag_suspect: int = Field(sa_column=Column('flag_suspect', Integer, nullable=False, server_default=text("'0'")))
    flag_group_q_bio: int = Field(sa_column=Column('flag_group_q_bio', Integer, nullable=False, server_default=text("'0'")))
    flag_group_q_fin: int = Field(sa_column=Column('flag_group_q_fin', Integer, nullable=False, server_default=text("'0'")))
    flag_group_stat: int = Field(sa_column=Column('flag_group_stat', Integer, nullable=False, server_default=text("'0'")))
    flag_group_eess: int = Field(sa_column=Column('flag_group_eess', Integer, nullable=False, server_default=text("'0'")))
    flag_group_econ: int = Field(sa_column=Column('flag_group_econ', Integer, nullable=False, server_default=text("'0'")))
    veto_status: str = Field(sa_column=Column('veto_status', Enum('ok', 'no-endorse', 'no-upload', 'no-replace'), nullable=False, server_default=text("'ok'")))
    type: Optional[int] = Field(default=None, sa_column=Column('type', SmallInteger))
    archive: Optional[str] = Field(default=None, sa_column=Column('archive', String(16)))
    subject_class: Optional[str] = Field(default=None, sa_column=Column('subject_class', String(16)))
    flag_group_physics: Optional[int] = Field(default=None, sa_column=Column('flag_group_physics', Integer))

    arXiv_categories: Optional['ArXivCategories'] = Relationship(back_populates='arXiv_demographics')


class ArXivDocumentCategory(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['category'], ['arXiv_category_def.category'], name='doc_cat_cat'),
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', name='doc_cat_doc'),
        Index('category', 'category'),
        Index('document_id', 'document_id')
    )

    document_id: int = Field(sa_column=Column('document_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    category: Optional[str] = Field(default=None, sa_column=Column('category', String(32), primary_key=True, nullable=False))
    is_primary: int = Field(sa_column=Column('is_primary', Boolean(), nullable=False, server_default=text("'0'")))

    arXiv_category_def: Optional['ArXivCategoryDef'] = Relationship(back_populates='arXiv_document_category')
    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_document_category')


class ArXivEndorsementRequests(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_723'),
        ForeignKeyConstraint(['endorsee_id'], ['tapir_users.user_id'], name='0_722'),
        Index('archive', 'archive', 'subject_class'),
        Index('endorsee_id', 'endorsee_id'),
        Index('endorsee_id_2', 'endorsee_id', 'archive', 'subject_class', unique=True),
        Index('secret', 'secret', unique=True)
    )

    request_id: Optional[int] = Field(default=None, sa_column=Column('request_id', Integer, primary_key=True))
    endorsee_id: int = Field(sa_column=Column('endorsee_id', Integer, nullable=False, server_default=text("'0'")))
    archive: str = Field(sa_column=Column('archive', String(16), nullable=False, server_default=text("''")))
    subject_class: str = Field(sa_column=Column('subject_class', String(16), nullable=False, server_default=text("''")))
    secret: str = Field(sa_column=Column('secret', String(16), nullable=False, server_default=text("''")))
    flag_valid: int = Field(sa_column=Column('flag_valid', Integer, nullable=False, server_default=text("'0'")))
    issued_when: int = Field(sa_column=Column('issued_when', Integer, nullable=False, server_default=text("'0'")))
    point_value: int = Field(sa_column=Column('point_value', Integer, nullable=False, server_default=text("'0'")))

    arXiv_categories: Optional['ArXivCategories'] = Relationship(back_populates='arXiv_endorsement_requests')
    endorsee: Optional['TapirUsers'] = Relationship(back_populates='arXiv_endorsement_requests')
    arXiv_endorsements: List['ArXivEndorsements'] = Relationship(back_populates='request')
    arXiv_ownership_requests: List['ArXivOwnershipRequests'] = Relationship(back_populates='endorsement_request')


t_arXiv_in_category = Table(
    'arXiv_in_category', metadata,
    Column('document_id', Integer, nullable=False, server_default=text("'0'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('is_primary', Boolean(), nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_583'),
    ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_582'),
    Index('arXiv_in_category_mp', 'archive', 'subject_class'),
    Index('archive', 'archive', 'subject_class', 'document_id', unique=True),
    Index('document_id', 'document_id')
)


class ArXivJrefControl(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_jref_control_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_jref_control_ibfk_2'),
        Index('document_id', 'document_id', 'version', unique=True),
        Index('freeze_date', 'freeze_date'),
        Index('status', 'status'),
        Index('user_id', 'user_id')
    )

    control_id: Optional[int] = Field(default=None, sa_column=Column('control_id', Integer, primary_key=True))
    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    version: int = Field(sa_column=Column('version', SmallInteger, nullable=False, server_default=text("'0'")))
    user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False, server_default=text("'0'")))
    status: str = Field(sa_column=Column('status', Enum('new', 'frozen', 'published', 'rejected'), nullable=False, server_default=text("'new'")))
    jref: str = Field(sa_column=Column('jref', String(255), nullable=False, server_default=text("''")))
    request_date: int = Field(sa_column=Column('request_date', Integer, nullable=False, server_default=text("'0'")))
    freeze_date: int = Field(sa_column=Column('freeze_date', Integer, nullable=False, server_default=text("'0'")))
    publish_date: int = Field(sa_column=Column('publish_date', Integer, nullable=False, server_default=text("'0'")))
    flag_must_notify: Optional[str] = Field(default=None, sa_column=Column('flag_must_notify', Enum('0', '1'), server_default=text("'1'")))

    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_jref_control')
    user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_jref_control')


class ArXivMetadata(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_metadata_fk_document_id'),
        ForeignKeyConstraint(['license'], ['arXiv_licenses.name'], name='arXiv_metadata_fk_license'),
        ForeignKeyConstraint(['submitter_id'], ['tapir_users.user_id'], name='arXiv_metadata_fk_submitter_id'),
        Index('arXiv_metadata_idx_document_id', 'document_id'),
        Index('arXiv_metadata_idx_license', 'license'),
        Index('arXiv_metadata_idx_submitter_id', 'submitter_id'),
        Index('pidv', 'paper_id', 'version', unique=True)
    )

    metadata_id: Optional[int] = Field(default=None, sa_column=Column('metadata_id', Integer, primary_key=True))
    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    paper_id: str = Field(sa_column=Column('paper_id', String(64), nullable=False))
    submitter_name: str = Field(sa_column=Column('submitter_name', String(64), nullable=False))
    submitter_email: str = Field(sa_column=Column('submitter_email', String(64), nullable=False))
    version: int = Field(sa_column=Column('version', Integer, nullable=False, server_default=text("'1'")))
    is_withdrawn: int = Field(sa_column=Column('is_withdrawn', Boolean(), nullable=False, server_default=text("'0'")))
    created: Optional[datetime] = Field(default=None, sa_column=Column('created', DateTime))
    updated: Optional[datetime] = Field(default=None, sa_column=Column('updated', DateTime))
    submitter_id: Optional[int] = Field(default=None, sa_column=Column('submitter_id', Integer))
    source_size: Optional[int] = Field(default=None, sa_column=Column('source_size', Integer))
    source_format: Optional[str] = Field(default=None, sa_column=Column('source_format', String(12)))
    source_flags: Optional[str] = Field(default=None, sa_column=Column('source_flags', String(12)))
    title: Optional[str] = Field(default=None, sa_column=Column('title', Text))
    authors: Optional[str] = Field(default=None, sa_column=Column('authors', Text))
    abs_categories: Optional[str] = Field(default=None, sa_column=Column('abs_categories', String(255)))
    comments: Optional[str] = Field(default=None, sa_column=Column('comments', Text))
    proxy: Optional[str] = Field(default=None, sa_column=Column('proxy', String(255)))
    report_num: Optional[str] = Field(default=None, sa_column=Column('report_num', Text))
    msc_class: Optional[str] = Field(default=None, sa_column=Column('msc_class', String(255)))
    acm_class: Optional[str] = Field(default=None, sa_column=Column('acm_class', String(255)))
    journal_ref: Optional[str] = Field(default=None, sa_column=Column('journal_ref', Text))
    doi: Optional[str] = Field(default=None, sa_column=Column('doi', String(255)))
    abstract: Optional[str] = Field(default=None, sa_column=Column('abstract', Text))
    license: Optional[str] = Field(default=None, sa_column=Column('license', String(255)))
    modtime: Optional[int] = Field(default=None, sa_column=Column('modtime', Integer))
    is_current: Optional[int] = Field(default=None, sa_column=Column('is_current', Boolean(), server_default=text("'1'")))

    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_metadata')
    arXiv_licenses: Optional['ArXivLicenses'] = Relationship(back_populates='arXiv_metadata')
    submitter: Optional['TapirUsers'] = Relationship(back_populates='arXiv_metadata')
    arXiv_datacite_dois: List['ArXivDataciteDois'] = Relationship(back_populates='metadata_')


class ArXivMirrorList(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_mirror_list_fk_document_id'),
        Index('arXiv_mirror_list_idx_document_id', 'document_id')
    )

    mirror_list_id: Optional[int] = Field(default=None, sa_column=Column('mirror_list_id', Integer, primary_key=True))
    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    version: int = Field(sa_column=Column('version', Integer, nullable=False, server_default=text("'1'")))
    write_source: int = Field(sa_column=Column('write_source', Boolean(), nullable=False, server_default=text("'0'")))
    write_abs: int = Field(sa_column=Column('write_abs', Boolean(), nullable=False, server_default=text("'0'")))
    is_written: int = Field(sa_column=Column('is_written', Boolean(), nullable=False, server_default=text("'0'")))
    created: Optional[datetime] = Field(default=None, sa_column=Column('created', DateTime))
    updated: Optional[datetime] = Field(default=None, sa_column=Column('updated', DateTime))

    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_mirror_list')


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
    Index('arXiv_moderators_idx_no_email', 'no_email'),
    Index('arXiv_moderators_idx_no_reply_to', 'no_reply_to'),
    Index('arXiv_moderators_idx_no_web_email', 'no_web_email'),
    Index('user_id', 'archive', 'subject_class', 'user_id', unique=True),
    Index('user_id_2', 'user_id')
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
    Index('added_by', 'added_by'),
    Index('document_id', 'document_id', 'user_id', unique=True),
    Index('user_id', 'user_id')
)


class ArXivPaperPw(ArXivDocuments, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_585'),
    )

    document_id_x: int = Field(alias='document_id', sa_column=Column('document_id', Integer, primary_key=True, server_default=text("'0'")))
    password_storage: Optional[int] = Field(default=None, sa_column=Column('password_storage', Integer))
    password_enc: Optional[str] = Field(default=None, sa_column=Column('password_enc', String(50)))


# class ArXivQuestionableCategories(ArXivCategories, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_756'),
#     )

#     archive_x: Optional[str] = Field(alias='archive', default=None, sa_column=Column('archive', String(16), primary_key=True, nullable=False, server_default=text("''")))
#     subject_class: Optional[str] = Field(default=None, sa_column=Column('subject_class', String(16), primary_key=True, nullable=False, server_default=text("''")))


class ArXivShowEmailRequests(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_show_email_requests_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_show_email_requests_ibfk_2'),
        Index('dated', 'dated'),
        Index('document_id', 'document_id'),
        Index('remote_addr', 'remote_addr'),
        Index('user_id', 'user_id', 'dated')
    )

    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False, server_default=text("'0'")))
    session_id: int = Field(sa_column=Column('session_id', Integer, nullable=False, server_default=text("'0'")))
    dated: int = Field(sa_column=Column('dated', Integer, nullable=False, server_default=text("'0'")))
    flag_allowed: int = Field(sa_column=Column('flag_allowed', Boolean, nullable=False, server_default=text("'0'")))
    remote_addr: str = Field(sa_column=Column('remote_addr', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))
    request_id: Optional[int] = Field(default=None, sa_column=Column('request_id', Integer, primary_key=True))

    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_show_email_requests')
    user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_show_email_requests')


class ArXivSubmissionControl(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_submission_control_ibfk_1'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_submission_control_ibfk_2'),
        Index('document_id', 'document_id', 'version', unique=True),
        Index('freeze_date', 'freeze_date'),
        Index('pending_paper_id', 'pending_paper_id'),
        Index('request_date', 'request_date'),
        Index('status', 'status'),
        Index('user_id', 'user_id')
    )

    control_id: Optional[int] = Field(default=None, sa_column=Column('control_id', Integer, primary_key=True))
    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    version: int = Field(sa_column=Column('version', SmallInteger, nullable=False, server_default=text("'0'")))
    pending_paper_id: str = Field(sa_column=Column('pending_paper_id', String(20), nullable=False, server_default=text("''")))
    user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False, server_default=text("'0'")))
    status: str = Field(sa_column=Column('status', Enum('new', 'frozen', 'published', 'rejected'), nullable=False, server_default=text("'new'")))
    request_date: int = Field(sa_column=Column('request_date', Integer, nullable=False, server_default=text("'0'")))
    freeze_date: int = Field(sa_column=Column('freeze_date', Integer, nullable=False, server_default=text("'0'")))
    publish_date: int = Field(sa_column=Column('publish_date', Integer, nullable=False, server_default=text("'0'")))
    flag_must_notify: Optional[str] = Field(default=None, sa_column=Column('flag_must_notify', Enum('0', '1'), server_default=text("'1'")))

    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_submission_control')
    user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_submission_control')


class ArXivSubmissions(SQLModel, table=True):
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

    submission_id: Optional[int] = Field(default=None, sa_column=Column('submission_id', Integer, primary_key=True))
    is_author: int = Field(sa_column=Column('is_author', Boolean(), nullable=False, server_default=text("'0'")))
    status: int = Field(sa_column=Column('status', Integer, nullable=False, server_default=text("'0'")))
    is_withdrawn: int = Field(sa_column=Column('is_withdrawn', Boolean(), nullable=False, server_default=text("'0'")))
    version: int = Field(sa_column=Column('version', Integer, nullable=False, server_default=text("'1'")))
    remote_addr: str = Field(sa_column=Column('remote_addr', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    package: str = Field(sa_column=Column('package', String(255), nullable=False, server_default=text("''")))
    is_locked: int = Field(sa_column=Column('is_locked', Integer, nullable=False, server_default=text("'0'")))
    document_id: Optional[int] = Field(default=None, sa_column=Column('document_id', Integer))
    doc_paper_id: Optional[str] = Field(default=None, sa_column=Column('doc_paper_id', String(20)))
    sword_id: Optional[int] = Field(default=None, sa_column=Column('sword_id', Integer))
    userinfo: Optional[int] = Field(default=None, sa_column=Column('userinfo', SmallInteger, server_default=text("'0'")))
    agree_policy: Optional[int] = Field(default=None, sa_column=Column('agree_policy', Boolean(), server_default=text("'0'")))
    viewed: Optional[int] = Field(default=None, sa_column=Column('viewed', Boolean(), server_default=text("'0'")))
    stage: Optional[int] = Field(default=None, sa_column=Column('stage', Integer, server_default=text("'0'")))
    submitter_id: Optional[int] = Field(default=None, sa_column=Column('submitter_id', Integer))
    submitter_name: Optional[str] = Field(default=None, sa_column=Column('submitter_name', String(64)))
    submitter_email: Optional[str] = Field(default=None, sa_column=Column('submitter_email', String(64)))
    created: Optional[datetime] = Field(default=None, sa_column=Column('created', DateTime))
    updated: Optional[datetime] = Field(default=None, sa_column=Column('updated', DateTime))
    sticky_status: Optional[int] = Field(default=None, sa_column=Column('sticky_status', Integer))
    must_process: Optional[int] = Field(default=None, sa_column=Column('must_process', Boolean(), server_default=text("'1'")))
    submit_time: Optional[datetime] = Field(default=None, sa_column=Column('submit_time', DateTime))
    release_time: Optional[datetime] = Field(default=None, sa_column=Column('release_time', DateTime))
    source_size: Optional[int] = Field(default=None, sa_column=Column('source_size', Integer, server_default=text("'0'")))
    source_format: Optional[str] = Field(default=None, sa_column=Column('source_format', String(12)))
    source_flags: Optional[str] = Field(default=None, sa_column=Column('source_flags', String(12)))
    has_pilot_data: Optional[int] = Field(default=None, sa_column=Column('has_pilot_data', Boolean()))
    title: Optional[str] = Field(default=None, sa_column=Column('title', Text))
    authors: Optional[str] = Field(default=None, sa_column=Column('authors', Text))
    comments: Optional[str] = Field(default=None, sa_column=Column('comments', Text))
    proxy: Optional[str] = Field(default=None, sa_column=Column('proxy', String(255)))
    report_num: Optional[str] = Field(default=None, sa_column=Column('report_num', Text))
    msc_class: Optional[str] = Field(default=None, sa_column=Column('msc_class', String(255)))
    acm_class: Optional[str] = Field(default=None, sa_column=Column('acm_class', String(255)))
    journal_ref: Optional[str] = Field(default=None, sa_column=Column('journal_ref', Text))
    doi: Optional[str] = Field(default=None, sa_column=Column('doi', String(255)))
    abstract: Optional[str] = Field(default=None, sa_column=Column('abstract', Text))
    license: Optional[str] = Field(default=None, sa_column=Column('license', String(255)))
    type: Optional[str] = Field(default=None, sa_column=Column('type', CHAR(8)))
    is_ok: Optional[int] = Field(default=None, sa_column=Column('is_ok', Boolean()))
    admin_ok: Optional[int] = Field(default=None, sa_column=Column('admin_ok', Boolean()))
    allow_tex_produced: Optional[int] = Field(default=None, sa_column=Column('allow_tex_produced', Boolean(), server_default=text("'0'")))
    is_oversize: Optional[int] = Field(default=None, sa_column=Column('is_oversize', Boolean(), server_default=text("'0'")))
    rt_ticket_id: Optional[int] = Field(default=None, sa_column=Column('rt_ticket_id', Integer))
    auto_hold: Optional[int] = Field(default=None, sa_column=Column('auto_hold', Boolean(), server_default=text("'0'")))
    agreement_id: Optional[int] = Field(default=None, sa_column=Column('agreement_id', SmallInteger))

    agreement: Optional['ArXivSubmissionAgreements'] = Relationship(back_populates='arXiv_submissions')
    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_submissions')
    arXiv_licenses: Optional['ArXivLicenses'] = Relationship(back_populates='arXiv_submissions')
    submitter: Optional['TapirUsers'] = Relationship(back_populates='arXiv_submissions')
    sword: Optional['ArXivTracking'] = Relationship(back_populates='arXiv_submissions')
    arXiv_pilot_files: List['ArXivPilotFiles'] = Relationship(back_populates='submission')
    arXiv_submission_category: List['ArXivSubmissionCategory'] = Relationship(back_populates='submission')
    arXiv_submission_category_proposal: List['ArXivSubmissionCategoryProposal'] = Relationship(back_populates='submission')
    arXiv_submission_flag: List['ArXivSubmissionFlag'] = Relationship(back_populates='submission')
    arXiv_submission_hold_reason: List['ArXivSubmissionHoldReason'] = Relationship(back_populates='submission')
    arXiv_submission_near_duplicates: List['ArXivSubmissionNearDuplicates'] = Relationship(back_populates='submission')
    arXiv_submission_qa_reports: List['ArXivSubmissionQaReports'] = Relationship(back_populates='submission')
    arXiv_submission_view_flag: List['ArXivSubmissionViewFlag'] = Relationship(back_populates='submission')


class ArXivTopPapers(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_top_papers_ibfk_1'),
        Index('document_id', 'document_id')
    )

    from_week: Optional[date] = Field(default=None, sa_column=Column('from_week', Date, primary_key=True, nullable=False, server_default=text("'0000-00-00'")))
    class_: Optional[str] = Field(default=None, sa_column=Column('class', CHAR(1), primary_key=True, nullable=False, server_default=text("''")))
    rank: int = Field(sa_column=Column('rank', SmallInteger, primary_key=True, nullable=False, server_default=text("'0'")))
    document_id: int = Field(sa_column=Column('document_id', Integer, nullable=False, server_default=text("'0'")))
    viewers: int = Field(sa_column=Column('viewers', Integer, nullable=False, server_default=text("'0'")))

    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_top_papers')


class ArXivVersions(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='arXiv_versions_ibfk_1'),
        Index('freeze_date', 'freeze_date'),
        Index('publish_date', 'publish_date'),
        Index('request_date', 'request_date')
    )

    document_id: int = Field(sa_column=Column('document_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    version: int = Field(sa_column=Column('version', SmallInteger, primary_key=True, nullable=False, server_default=text("'0'")))
    request_date: int = Field(sa_column=Column('request_date', Integer, nullable=False, server_default=text("'0'")))
    freeze_date: int = Field(sa_column=Column('freeze_date', Integer, nullable=False, server_default=text("'0'")))
    publish_date: int = Field(sa_column=Column('publish_date', Integer, nullable=False, server_default=text("'0'")))
    flag_current: int = Field(sa_column=Column('flag_current', Integer, nullable=False, server_default=text("'0'")))

    document: Optional['ArXivDocuments'] = Relationship(back_populates='arXiv_versions')


class TapirAdminAudit(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['admin_user'], ['tapir_users.user_id'], name='0_554'),
        ForeignKeyConstraint(['affected_user'], ['tapir_users.user_id'], name='0_555'),
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_553'),
        Index('admin_user', 'admin_user'),
        Index('affected_user', 'affected_user'),
        Index('data', 'data'),
        Index('data_2', 'data'),
        Index('data_3', 'data'),
        Index('ip_addr', 'ip_addr'),
        Index('log_date', 'log_date'),
        Index('session_id', 'session_id')
    )

    log_date: int = Field(sa_column=Column('log_date', Integer, nullable=False, server_default=text("'0'")))
    ip_addr: str = Field(sa_column=Column('ip_addr', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    affected_user: int = Field(sa_column=Column('affected_user', Integer, nullable=False, server_default=text("'0'")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))
    action: str = Field(sa_column=Column('action', String(32), nullable=False, server_default=text("''")))
    data: str = Field(sa_column=Column('data', Text, nullable=False))
    comment: str = Field(sa_column=Column('comment', Text, nullable=False))
    entry_id: Optional[int] = Field(default=None, sa_column=Column('entry_id', Integer, primary_key=True))
    session_id: Optional[int] = Field(default=None, sa_column=Column('session_id', Integer))
    admin_user: Optional[int] = Field(default=None, sa_column=Column('admin_user', Integer))

    tapir_users: Optional['TapirUsers'] = Relationship(back_populates='tapir_admin_audit')
    tapir_users_: Optional['TapirUsers'] = Relationship(back_populates='tapir_admin_audit_')
    session: Optional['TapirSessions'] = Relationship(back_populates='tapir_admin_audit')


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
    Index('session_id', 'session_id'),
    Index('user_id', 'user_id')
)


class TapirEmailHeaders(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['template_id'], ['tapir_email_templates.template_id'], name='0_563'),
    )

    template_id: int = Field(sa_column=Column('template_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    header_name: Optional[str] = Field(default=None, sa_column=Column('header_name', String(32), primary_key=True, nullable=False, server_default=text("''")))
    header_content: str = Field(sa_column=Column('header_content', String(255), nullable=False, server_default=text("''")))

    template: Optional['TapirEmailTemplates'] = Relationship(back_populates='tapir_email_headers')


class TapirEmailMailings(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['tapir_users.user_id'], name='0_565'),
        ForeignKeyConstraint(['sent_by'], ['tapir_users.user_id'], name='0_566'),
        ForeignKeyConstraint(['template_id'], ['tapir_email_templates.template_id'], name='0_567'),
        Index('created_by', 'created_by'),
        Index('sent_by', 'sent_by'),
        Index('template_id', 'template_id')
    )

    mailing_id: Optional[int] = Field(default=None, sa_column=Column('mailing_id', Integer, primary_key=True))
    template_id: Optional[int] = Field(default=None, sa_column=Column('template_id', Integer))
    created_by: Optional[int] = Field(default=None, sa_column=Column('created_by', Integer))
    sent_by: Optional[int] = Field(default=None, sa_column=Column('sent_by', Integer))
    created_date: Optional[int] = Field(default=None, sa_column=Column('created_date', Integer))
    sent_date: Optional[int] = Field(default=None, sa_column=Column('sent_date', Integer))
    complete_date: Optional[int] = Field(default=None, sa_column=Column('complete_date', Integer))
    mailing_name: Optional[str] = Field(default=None, sa_column=Column('mailing_name', String(255)))
    comment: Optional[str] = Field(default=None, sa_column=Column('comment', Text))

    tapir_users: Optional['TapirUsers'] = Relationship(back_populates='tapir_email_mailings')
    tapir_users_: Optional['TapirUsers'] = Relationship(back_populates='tapir_email_mailings_')
    template: Optional['TapirEmailTemplates'] = Relationship(back_populates='tapir_email_mailings')


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
    Index('session_id', 'session_id'),
    Index('user_id', 'user_id')
)


class TapirPermanentTokens(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_541'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_540'),
        Index('session_id', 'session_id')
    )

    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    secret: Optional[str] = Field(default=None, sa_column=Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")))
    valid: int = Field(sa_column=Column('valid', Integer, nullable=False, server_default=text("'1'")))
    issued_when: int = Field(sa_column=Column('issued_when', Integer, nullable=False, server_default=text("'0'")))
    issued_to: str = Field(sa_column=Column('issued_to', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    session_id: int = Field(sa_column=Column('session_id', Integer, nullable=False, server_default=text("'0'")))

    session: Optional['TapirSessions'] = Relationship(back_populates='tapir_permanent_tokens')
    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_permanent_tokens')


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
    Index('session_id', 'session_id'),
    Index('user_id', 'user_id')
)


class TapirRecoveryTokensUsed(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_549'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_548'),
        Index('session_id', 'session_id')
    )

    user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
    secret: Optional[str] = Field(default=None, sa_column=Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    used_when: Optional[int] = Field(default=None, sa_column=Column('used_when', Integer))
    used_from: Optional[str] = Field(default=None, sa_column=Column('used_from', String(16)))
    session_id: Optional[int] = Field(default=None, sa_column=Column('session_id', Integer))

    session: Optional['TapirSessions'] = Relationship(back_populates='tapir_recovery_tokens_used')
    user: Optional['TapirUsers'] = Relationship(back_populates='tapir_recovery_tokens_used')


class TapirSessionsAudit(TapirSessions, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_527'),
        Index('ip_addr', 'ip_addr'),
        Index('tracking_cookie', 'tracking_cookie')
    )

    session_id_x: int = Field(alias='session_id', sa_column=Column('session_id', Integer, primary_key=True, server_default=text("'0'")))
    ip_addr: str = Field(sa_column=Column('ip_addr', String(16), nullable=False, server_default=text("''")))
    remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
    tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))


class ArXivDataciteDois(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['metadata_id'], ['arXiv_metadata.metadata_id'], name='arXiv_datacite_dois_ibfk_1'),
        Index('account_paper_id', 'account', 'paper_id', unique=True),
        Index('metadata_id', 'metadata_id')
    )

    doi: Optional[str] = Field(default=None, sa_column=Column('doi', String(255), primary_key=True))
    metadata_id: int = Field(sa_column=Column('metadata_id', Integer, nullable=False))
    paper_id: str = Field(sa_column=Column('paper_id', String(64), nullable=False))
    account: Optional[str] = Field(default=None, sa_column=Column('account', Enum('test', 'prod')))
    created: Optional[datetime] = Field(default=None, sa_column=Column('created', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updated: Optional[datetime] = Field(default=None, sa_column=Column('updated', DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))

    metadata_: Optional['ArXivMetadata'] = Relationship(back_populates='arXiv_datacite_dois')


class ArXivEndorsementRequestsAudit(ArXivEndorsementRequests, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['request_id'], ['arXiv_endorsement_requests.request_id'], name='0_725'),
    )

    request_id_x: int = Field(alias='request_id', sa_column=Column('request_id', Integer, primary_key=True, server_default=text("'0'")))
    session_id: int = Field(sa_column=Column('session_id', Integer, nullable=False, server_default=text("'0'")))
    remote_addr: Optional[str] = Field(default=None, sa_column=Column('remote_addr', String(16)))
    remote_host: Optional[str] = Field(default=None, sa_column=Column('remote_host', String(255)))
    tracking_cookie: Optional[str] = Field(default=None, sa_column=Column('tracking_cookie', String(255)))


class ArXivEndorsements(SQLModel, table=True):
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

    endorsement_id: Optional[int] = Field(default=None, sa_column=Column('endorsement_id', Integer, primary_key=True))
    endorsee_id: int = Field(sa_column=Column('endorsee_id', Integer, nullable=False, server_default=text("'0'")))
    archive: str = Field(sa_column=Column('archive', String(16), nullable=False, server_default=text("''")))
    subject_class: str = Field(sa_column=Column('subject_class', String(16), nullable=False, server_default=text("''")))
    flag_valid: int = Field(sa_column=Column('flag_valid', Integer, nullable=False, server_default=text("'0'")))
    point_value: int = Field(sa_column=Column('point_value', Integer, nullable=False, server_default=text("'0'")))
    issued_when: int = Field(sa_column=Column('issued_when', Integer, nullable=False, server_default=text("'0'")))
    endorser_id: Optional[int] = Field(default=None, sa_column=Column('endorser_id', Integer))
    type: Optional[str] = Field(default=None, sa_column=Column('type', Enum('user', 'admin', 'auto')))
    request_id: Optional[int] = Field(default=None, sa_column=Column('request_id', Integer))

    arXiv_categories: Optional['ArXivCategories'] = Relationship(back_populates='arXiv_endorsements')
    endorsee: Optional['TapirUsers'] = Relationship(back_populates='arXiv_endorsements')
    endorser: Optional['TapirUsers'] = Relationship(back_populates='arXiv_endorsements_')
    request: Optional['ArXivEndorsementRequests'] = Relationship(back_populates='arXiv_endorsements')


class ArXivOwnershipRequests(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['endorsement_request_id'], ['arXiv_endorsement_requests.request_id'], name='0_735'),
        ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_734'),
        Index('endorsement_request_id', 'endorsement_request_id'),
        Index('user_id', 'user_id')
    )

    request_id: Optional[int] = Field(default=None, sa_column=Column('request_id', Integer, primary_key=True))
    user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False, server_default=text("'0'")))
    workflow_status: str = Field(sa_column=Column('workflow_status', Enum('pending', 'accepted', 'rejected'), nullable=False, server_default=text("'pending'")))
    endorsement_request_id: Optional[int] = Field(default=None, sa_column=Column('endorsement_request_id', Integer))

    endorsement_request: Optional['ArXivEndorsementRequests'] = Relationship(back_populates='arXiv_ownership_requests')
    user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_ownership_requests')


class ArXivPilotDatasets(ArXivSubmissions, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_pilot_datasets_cdfk3'),
    )

    submission_id_x: int = Field(alias='submission_id', sa_column=Column('submission_id', Integer, primary_key=True))
    created_x: datetime = Field(alias='created', sa_column=Column('created', DateTime, nullable=False))
    last_checked: datetime = Field(sa_column=Column('last_checked', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))
    numfiles: Optional[int] = Field(default=None, sa_column=Column('numfiles', SmallInteger, server_default=text("'0'")))
    feed_url: Optional[str] = Field(default=None, sa_column=Column('feed_url', String(256)))
    manifestation: Optional[str] = Field(default=None, sa_column=Column('manifestation', String(256)))
    published: Optional[int] = Field(default=None, sa_column=Column('published', Boolean(), server_default=text("'0'")))


class ArXivPilotFiles(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_pilot_files_cdfk3'),
        Index('arXiv_pilot_files_cdfk3', 'submission_id')
    )

    file_id: Optional[int] = Field(default=None, sa_column=Column('file_id', Integer, primary_key=True))
    submission_id: int = Field(sa_column=Column('submission_id', Integer, nullable=False))
    filename: Optional[str] = Field(default=None, sa_column=Column('filename', String(256), server_default=text("''")))
    entity_url: Optional[str] = Field(default=None, sa_column=Column('entity_url', String(256)))
    description: Optional[str] = Field(default=None, sa_column=Column('description', String(80)))
    byRef: Optional[int] = Field(default=None, sa_column=Column('byRef', Boolean(), server_default=text("'1'")))

    submission: Optional['ArXivSubmissions'] = Relationship(back_populates='arXiv_pilot_files')


# class ArXivSubmissionAbsClassifierData(ArXivSubmissions, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_abs_classifier_data_ibfk_1'),
#     )

#     submission_id_x: int = Field(alias='submission_id', sa_column=Column('submission_id', Integer, primary_key=True, server_default=text("'0'")))
#     last_update: datetime = Field(sa_column=Column('last_update', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))
#     json_x: Optional[str] = Field(alias='json', default=None, sa_column=Column('json', Text))
#     status: Optional[str] = Field(default=None, sa_column=Column('status', Enum('processing', 'success', 'failed', 'no connection')))
#     message: Optional[str] = Field(default=None, sa_column=Column('message', Text))
#     is_oversize: Optional[int] = Field(default=None, sa_column=Column('is_oversize', Boolean(), server_default=text("'0'")))
#     suggested_primary: Optional[str] = Field(default=None, sa_column=Column('suggested_primary', Text))
#     suggested_reason: Optional[str] = Field(default=None, sa_column=Column('suggested_reason', Text))
#     autoproposal_primary: Optional[str] = Field(default=None, sa_column=Column('autoproposal_primary', Text))
#     autoproposal_reason: Optional[str] = Field(default=None, sa_column=Column('autoproposal_reason', Text))
#     classifier_service_version: Optional[str] = Field(default=None, sa_column=Column('classifier_service_version', Text))
#     classifier_model_version: Optional[str] = Field(default=None, sa_column=Column('classifier_model_version', Text))


# class ArXivSubmissionCategory(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['category'], ['arXiv_category_def.category'], name='arXiv_submission_category_fk_category'),
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submission_category_fk_submission_id'),
#         Index('arXiv_submission_category_idx_category', 'category'),
#         Index('arXiv_submission_category_idx_is_primary', 'is_primary'),
#         Index('arXiv_submission_category_idx_is_published', 'is_published'),
#         Index('arXiv_submission_category_idx_submission_id', 'submission_id')
#     )

#     submission_id: int = Field(sa_column=Column('submission_id', Integer, primary_key=True, nullable=False))
#     category: Optional[str] = Field(default=None, sa_column=Column('category', String(32), primary_key=True, nullable=False, server_default=text("''")))
#     is_primary: int = Field(sa_column=Column('is_primary', Boolean(), nullable=False, server_default=text("'0'")))
#     is_published: Optional[int] = Field(default=None, sa_column=Column('is_published', Boolean(), server_default=text("'0'")))

#     arXiv_category_def: Optional['ArXivCategoryDef'] = Relationship(back_populates='arXiv_submission_category')
#     submission: Optional['ArXivSubmissions'] = Relationship(back_populates='arXiv_submission_category')


# class ArXivSubmissionCategoryProposal(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['category'], ['arXiv_category_def.category'], name='arXiv_submission_category_proposal_fk_category'),
#         ForeignKeyConstraint(['proposal_comment_id'], ['arXiv_admin_log.id'], name='arXiv_submission_category_proposal_fk_prop_comment_id'),
#         ForeignKeyConstraint(['response_comment_id'], ['arXiv_admin_log.id'], name='arXiv_submission_category_proposal_fk_resp_comment_id'),
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', onupdate='CASCADE', name='arXiv_submission_category_proposal_fk_submission_id'),
#         ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='arXiv_submission_category_proposal_fk_user_id'),
#         Index('arXiv_submission_category_proposal_fk_prop_comment_id', 'proposal_comment_id'),
#         Index('arXiv_submission_category_proposal_fk_resp_comment_id', 'response_comment_id'),
#         Index('arXiv_submission_category_proposal_fk_user_id', 'user_id'),
#         Index('arXiv_submission_category_proposal_idx_category', 'category'),
#         Index('arXiv_submission_category_proposal_idx_is_primary', 'is_primary'),
#         Index('arXiv_submission_category_proposal_idx_key', 'proposal_id'),
#         Index('arXiv_submission_category_proposal_idx_submission_id', 'submission_id')
#     )

#     proposal_id: Optional[int] = Field(default=None, sa_column=Column('proposal_id', Integer, primary_key=True, nullable=False))
#     submission_id: int = Field(sa_column=Column('submission_id', Integer, primary_key=True, nullable=False))
#     category: Optional[str] = Field(default=None, sa_column=Column('category', String(32), primary_key=True, nullable=False))
#     is_primary: int = Field(sa_column=Column('is_primary', Boolean(), primary_key=True, nullable=False, server_default=text("'0'")))
#     user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False))
#     proposal_status: Optional[int] = Field(default=None, sa_column=Column('proposal_status', Integer, server_default=text("'0'")))
#     updated: Optional[datetime] = Field(default=None, sa_column=Column('updated', DateTime))
#     proposal_comment_id: Optional[int] = Field(default=None, sa_column=Column('proposal_comment_id', Integer))
#     response_comment_id: Optional[int] = Field(default=None, sa_column=Column('response_comment_id', Integer))

#     arXiv_category_def: Optional['ArXivCategoryDef'] = Relationship(back_populates='arXiv_submission_category_proposal')
#     proposal_comment: Optional['ArXivAdminLog'] = Relationship(back_populates='arXiv_submission_category_proposal')
#     response_comment: Optional['ArXivAdminLog'] = Relationship(back_populates='arXiv_submission_category_proposal_')
#     submission: Optional['ArXivSubmissions'] = Relationship(back_populates='arXiv_submission_category_proposal')
#     user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_submission_category_proposal')


# class ArXivSubmissionClassifierData(ArXivSubmissions, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_classifier_data_ibfk_1'),
#     )

#     submission_id: int = Field(sa_column=Column('submission_id', Integer, primary_key=True, server_default=text("'0'")))
#     last_update: datetime = Field(sa_column=Column('last_update', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))
#     json: Optional[str] = Field(default=None, sa_column=Column('json', Text))
#     status: Optional[str] = Field(default=None, sa_column=Column('status', Enum('processing', 'success', 'failed', 'no connection')))
#     message: Optional[str] = Field(default=None, sa_column=Column('message', Text))
#     is_oversize: Optional[int] = Field(default=None, sa_column=Column('is_oversize', Boolean(), server_default=text("'0'")))


# class ArXivSubmissionFlag(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_flag_ibfk_2'),
#         ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_flag_ibfk_1'),
#         Index('uniq_one_flag_per_mod', 'submission_id', 'user_id', unique=True),
#         Index('user_id', 'user_id')
#     )

#     flag_id: Optional[int] = Field(default=None, sa_column=Column('flag_id', Integer, primary_key=True))
#     user_id: int = Field(sa_column=Column('user_id', Integer, nullable=False, server_default=text("'0'")))
#     submission_id: int = Field(sa_column=Column('submission_id', Integer, nullable=False))
#     flag: int = Field(sa_column=Column('flag', SmallInteger, nullable=False, server_default=text("'0'")))
#     updated: datetime = Field(sa_column=Column('updated', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))

#     submission: Optional['ArXivSubmissions'] = Relationship(back_populates='arXiv_submission_flag')
#     user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_submission_flag')


# class ArXivSubmissionHoldReason(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['comment_id'], ['arXiv_admin_log.id'], name='arXiv_submission_hold_reason_ibfk_3'),
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_hold_reason_ibfk_1'),
#         ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_hold_reason_ibfk_2'),
#         Index('comment_id', 'comment_id'),
#         Index('submission_id', 'submission_id'),
#         Index('user_id', 'user_id')
#     )

#     reason_id: Optional[int] = Field(default=None, sa_column=Column('reason_id', Integer, primary_key=True, nullable=False))
#     submission_id: int = Field(sa_column=Column('submission_id', Integer, nullable=False))
#     user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False))
#     reason: Optional[str] = Field(default=None, sa_column=Column('reason', String(30)))
#     type: Optional[str] = Field(default=None, sa_column=Column('type', String(30)))
#     comment_id: Optional[int] = Field(default=None, sa_column=Column('comment_id', Integer))

#     comment: Optional['ArXivAdminLog'] = Relationship(back_populates='arXiv_submission_hold_reason')
#     submission: Optional['ArXivSubmissions'] = Relationship(back_populates='arXiv_submission_hold_reason')
#     user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_submission_hold_reason')


# class ArXivSubmissionNearDuplicates(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_near_duplicates_ibfk_1'),
#         Index('match', 'submission_id', 'matching_id', unique=True)
#     )

#     submission_id: int = Field(sa_column=Column('submission_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
#     matching_id: int = Field(sa_column=Column('matching_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
#     similarity: Decimal = Field(sa_column=Column('similarity', Numeric(precision=2, scale=1), nullable=False))
#     last_update: datetime = Field(sa_column=Column('last_update', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')))

#     submission: Optional['ArXivSubmissions'] = Relationship(back_populates='arXiv_submission_near_duplicates')


# class ArXivSubmissionQaReports(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], name='arXiv_submission_qa_reports_ibfk_1'),
#         Index('report_key_name', 'report_key_name'),
#         Index('submission_id', 'submission_id')
#     )

#     id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
#     submission_id: int = Field(sa_column=Column('submission_id', Integer, nullable=False))
#     report_key_name: str = Field(sa_column=Column('report_key_name', String(64), nullable=False))
#     num_flags: int = Field(sa_column=Column('num_flags', SmallInteger, nullable=False, server_default=text("'0'")))
#     report: dict = Field(sa_column=Column('report', JSON, nullable=False))
#     created: Optional[datetime] = Field(default=None, sa_column=Column('created', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     report_uri: Optional[str] = Field(default=None, sa_column=Column('report_uri', String(256)))

#     submission: Optional['ArXivSubmissions'] = Relationship(back_populates='arXiv_submission_qa_reports')


# class ArXivSubmissionViewFlag(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['submission_id'], ['arXiv_submissions.submission_id'], ondelete='CASCADE', name='arXiv_submission_view_flag_ibfk_1'),
#         ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], ondelete='CASCADE', name='arXiv_submission_view_flag_ibfk_2'),
#         Index('user_id', 'user_id')
#     )

#     submission_id: int = Field(sa_column=Column('submission_id', Integer, primary_key=True, nullable=False))
#     user_id: int = Field(sa_column=Column('user_id', Integer, primary_key=True, nullable=False))
#     flag: Optional[int] = Field(default=None, sa_column=Column('flag', SmallInteger, server_default=text("'0'")))
#     updated: Optional[datetime] = Field(default=None, sa_column=Column('updated', DateTime))

#     submission: Optional['ArXivSubmissions'] = Relationship(back_populates='arXiv_submission_view_flag')
#     user: Optional['TapirUsers'] = Relationship(back_populates='arXiv_submission_view_flag')


# class ArXivVersionsChecksum(ArXivVersions, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['document_id', 'version'], ['arXiv_versions.document_id', 'arXiv_versions.version'], name='arXiv_versions_checksum_ibfk_1'),
#         Index('abs_md5sum', 'abs_md5sum'),
#         Index('abs_size', 'abs_size'),
#         Index('src_md5sum', 'src_md5sum'),
#         Index('src_size', 'src_size')
#     )

#     document_id: int = Field(sa_column=Column('document_id', Integer, primary_key=True, nullable=False, server_default=text("'0'")))
#     version: int = Field(sa_column=Column('version', SmallInteger, primary_key=True, nullable=False, server_default=text("'0'")))
#     flag_abs_present: int = Field(sa_column=Column('flag_abs_present', Integer, nullable=False, server_default=text("'0'")))
#     abs_size: int = Field(sa_column=Column('abs_size', Integer, nullable=False, server_default=text("'0'")))
#     flag_src_present: int = Field(sa_column=Column('flag_src_present', Boolean(), nullable=False, server_default=text("'0'")))
#     src_size: int = Field(sa_column=Column('src_size', Integer, nullable=False, server_default=text("'0'")))
#     abs_md5sum: Optional[bytes] = Field(default=None, sa_column=Column('abs_md5sum', BINARY(16)))
#     src_md5sum: Optional[bytes] = Field(default=None, sa_column=Column('src_md5sum', BINARY(16)))


# class ArXivEndorsementsAudit(ArXivEndorsements, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['endorsement_id'], ['arXiv_endorsements.endorsement_id'], name='0_732'),
#     )

#     endorsement_id: int = Field(sa_column=Column('endorsement_id', Integer, primary_key=True, server_default=text("'0'")))
#     session_id: int = Field(sa_column=Column('session_id', Integer, nullable=False, server_default=text("'0'")))
#     remote_addr: str = Field(sa_column=Column('remote_addr', String(16), nullable=False, server_default=text("''")))
#     remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
#     tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))
#     flag_knows_personally: int = Field(sa_column=Column('flag_knows_personally', Integer, nullable=False, server_default=text("'0'")))
#     flag_seen_paper: int = Field(sa_column=Column('flag_seen_paper', Integer, nullable=False, server_default=text("'0'")))
#     comment: Optional[str] = Field(default=None, sa_column=Column('comment', Text))


# class ArXivOwnershipRequestsAudit(ArXivOwnershipRequests, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['request_id'], ['arXiv_ownership_requests.request_id'], name='0_737'),
#     )

#     request_id: int = Field(sa_column=Column('request_id', Integer, primary_key=True, server_default=text("'0'")))
#     session_id: int = Field(sa_column=Column('session_id', Integer, nullable=False, server_default=text("'0'")))
#     remote_addr: str = Field(sa_column=Column('remote_addr', String(16), nullable=False, server_default=text("''")))
#     remote_host: str = Field(sa_column=Column('remote_host', String(255), nullable=False, server_default=text("''")))
#     tracking_cookie: str = Field(sa_column=Column('tracking_cookie', String(255), nullable=False, server_default=text("''")))
#     date_: int = Field(sa_column=Column('date', Integer, nullable=False, server_default=text("'0'")))
