from sqlalchemy import BINARY, BigInteger, CHAR, Column, Date, DateTime, Enum, ForeignKey, ForeignKeyConstraint, Index, Integer, JSON, SmallInteger, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship

from arxiv_db.models.sqa_types import EpochIntArxivTz

from .. import Base

metadata = Base.metadata

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

t_arXiv_black_email = Table(
    'arXiv_black_email', metadata,
    Column('pattern', String(64))
)

t_arXiv_block_email = Table(
    'arXiv_block_email', metadata,
    Column('pattern', String(64))
)

t_arXiv_ownership_requests_papers = Table(
    'arXiv_ownership_requests_papers', metadata,
    Column('request_id', INTEGER, ForeignKey("arXiv_ownership_requests.request_id"), nullable=False, server_default=text("'0'"), ),
    Column('document_id', INTEGER, ForeignKey("arXiv_documents.document_id"), nullable=False, server_default=text("'0'"), ),
    Index('document_id', 'document_id'),
    Index('request_id', 'request_id', 'document_id', unique=True)
)

t_arXiv_refresh_list = Table(
    'arXiv_refresh_list', metadata,
    Column('filename', String(255)),
    Column('mtime', INTEGER),
    Index('arXiv_refresh_list_mtime', 'mtime')
)

t_arXiv_stats_hourly = Table(
    'arXiv_stats_hourly', metadata,
    Column('ymd', Date, nullable=False),
    Column('hour', TINYINT, nullable=False),
    Column('node_num', TINYINT, nullable=False),
    Column('access_type', CHAR(1), nullable=False),
    Column('connections', INTEGER, nullable=False),
    Index('arXiv_stats_hourly_idx_access_type', 'access_type'),
    Index('arXiv_stats_hourly_idx_hour', 'hour'),
    Index('arXiv_stats_hourly_idx_node_num', 'node_num'),
    Index('arXiv_stats_hourly_idx_ymd', 'ymd')
)

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
    Column('control_id', INTEGER),
    Column('type', Enum('submission', 'cross', 'jref')),
    Column('queued_date', INTEGER, nullable=False, server_default=text("'0'")),
    Column('sent_date', INTEGER, nullable=False, server_default=text("'0'")),
    Column('status', Enum('unsent', 'sent', 'failed')),
    Index('control_id', 'control_id'),
    Index('status', 'status')
)

t_demographics_backup = Table(
    'demographics_backup', metadata,
    Column('user_id', INTEGER, nullable=False, server_default=text("'0'")),
    Column('country', CHAR(2), nullable=False, server_default=text("''")),
    Column('affiliation', String(255), nullable=False, server_default=text("''")),
    Column('url', String(255), nullable=False, server_default=text("''")),
    Column('type', SMALLINT),
    Column('os', SMALLINT),
    Column('archive', String(16)),
    Column('subject_class', String(16)),
    Column('original_subject_classes', String(255), nullable=False, server_default=text("''")),
    Column('flag_group_physics', INTEGER),
    Column('flag_group_math', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_group_cs', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_group_nlin', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_proxy', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_journal', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_xml', INTEGER, nullable=False, server_default=text("'0'")),
    Column('dirty', INTEGER, nullable=False, server_default=text("'2'")),
    Column('flag_group_test', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_suspect', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_group_q_bio', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_no_upload', INTEGER, nullable=False, server_default=text("'0'")),
    Column('flag_no_endorse', INTEGER, nullable=False, server_default=text("'0'")),
    Column('veto_status', Enum('ok', 'no-endorse', 'no-upload'), server_default=text("'ok'"))
)

t_tapir_error_log = Table(
    'tapir_error_log', metadata,
    Column('error_date', INTEGER, nullable=False, server_default=text("'0'")),
    Column('user_id', INTEGER),
    Column('session_id', INTEGER),
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

t_tapir_no_cookies = Table(
    'tapir_no_cookies', metadata,
    Column('log_date', INTEGER, nullable=False, server_default=text("'0'")),
    Column('ip_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('session_data', String(255), nullable=False, server_default=text("''")),
    Column('user_agent', String(255), nullable=False, server_default=text("''"))
)

t_tapir_periodic_tasks_log = Table(
    'tapir_periodic_tasks_log', metadata,
    Column('t', INTEGER, nullable=False, server_default=text("'0'")),
    Column('entry', Text),
    Index('tapir_periodic_tasks_log_1', 't')
)

t_tapir_save_post_variables = Table(
    'tapir_save_post_variables', metadata,
    Column('presession_id', INTEGER, nullable=False, server_default=text("'0'")),
    Column('name', String(255)),
    Column('value', MEDIUMTEXT, nullable=False),
    Column('seq', INTEGER, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['presession_id'], ['tapir_presessions.presession_id'], name='0_558'),
    Index('presession_id', 'presession_id')
)

t_arXiv_bad_pw = Table(
    'arXiv_bad_pw', metadata,
    Column('user_id', INTEGER, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_601'),
    Index('user_id', 'user_id')
)

t_arXiv_duplicates = Table(
    'arXiv_duplicates', metadata,
    Column('user_id', INTEGER, nullable=False, server_default=text("'0'")),
    Column('email', String(255)),
    Column('username', String(255)),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_599'),
    Index('user_id', 'user_id')
)

t_arXiv_bogus_subject_class = Table(
    'arXiv_bogus_subject_class', metadata,
    Column('document_id', MEDIUMINT, nullable=False, server_default=text("'0'")),
    Column('category_name', String(255), nullable=False, server_default=text("''")),
    ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_604'),
    Index('document_id', 'document_id')
)

t_arXiv_in_category = Table(
    'arXiv_in_category', metadata,
    Column('document_id', MEDIUMINT, nullable=False, server_default=text("'0'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('is_primary', TINYINT(1), nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_583'),
    ForeignKeyConstraint(['document_id'], ['arXiv_documents.document_id'], name='0_582'),
    Index('arXiv_in_category_mp', 'archive', 'subject_class'),
    Index('archive', 'archive', 'subject_class', 'document_id', unique=True),
    Index('document_id', 'document_id')
)

t_arXiv_moderators = Table(
    'arXiv_moderators', metadata,
    Column('user_id', INTEGER, nullable=False, server_default=text("'0'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('is_public', TINYINT, nullable=False, server_default=text("'0'")),
    Column('no_email', TINYINT(1), server_default=text("'0'")),
    Column('no_web_email', TINYINT(1), server_default=text("'0'")),
    Column('no_reply_to', TINYINT(1), server_default=text("'0'")),
    Column('daily_update', TINYINT(1), server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'], name='0_591'),
    ForeignKeyConstraint(['archive'], ['arXiv_archive_group.archive_id'], name='fk_archive_id'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_590'),
    Index('arXiv_moderators_idx_no_email', 'no_email'),
    Index('arXiv_moderators_idx_no_reply_to', 'no_reply_to'),
    Index('arXiv_moderators_idx_no_web_email', 'no_web_email'),
    Index('user_id', 'archive', 'subject_class', 'user_id', unique=True),
    Index('user_id_2', 'user_id')
)

t_tapir_email_change_tokens_used = Table(
    'tapir_email_change_tokens_used', metadata,
    Column('user_id', INTEGER, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', INTEGER, nullable=False, server_default=text("'0'")),
    Column('used_from', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', INTEGER, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_538'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_537'),
    Index('session_id', 'session_id'),
    Index('user_id', 'user_id')
)

t_tapir_email_tokens_used = Table(
    'tapir_email_tokens_used', metadata,
    Column('user_id', INTEGER, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', INTEGER, nullable=False, server_default=text("'0'")),
    Column('used_from', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', INTEGER, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_533'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_532'),
    Index('session_id', 'session_id'),
    Index('user_id', 'user_id')
)

t_tapir_permanent_tokens_used = Table(
    'tapir_permanent_tokens_used', metadata,
    Column('user_id', INTEGER),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', INTEGER),
    Column('used_from', String(16)),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', INTEGER, nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['session_id'], ['tapir_sessions.session_id'], name='0_544'),
    ForeignKeyConstraint(['user_id'], ['tapir_users.user_id'], name='0_543'),
    Index('session_id', 'session_id'),
    Index('user_id', 'user_id')
)
