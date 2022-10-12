from sqlalchemy import BINARY, CHAR, Column, Date, DateTime, \
    Enum, ForeignKey, ForeignKeyConstraint, Index, MetaData, \
    String, TIMESTAMP, Table, Text, text, UniqueConstraint, \
    MetaData, BigInteger, Numeric, Integer

metadata = MetaData()

#from modapi.db import metadata


Subscription_UniversalInstitution = Table(
    'Subscription_UniversalInstitution', metadata,
    Column('resolver_URL', String(255)),
    Column('name', String(255), nullable=False, index=True),
    Column('label', String(255)),
    Column('id', Integer(), primary_key=True),
    Column('alt_text', String(255)),
    Column('link_icon', String(255)),
    Column('note', String(255))
)


arXiv_admin_log = Table(
    'arXiv_admin_log', metadata,
    Column('id', Integer(), primary_key=True),
    Column('logtime', String(24)),
    Column('created', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")),
    Column('paper_id', String(20), index=True),
    Column('username', String(20), index=True),
    Column('host', String(64)),
    Column('program', String(20)),
    Column('command', String(20), index=True),
    Column('logtext', Text),
    Column('document_id', Integer()),
    Column('submission_id', Integer(), index=True),
    Column('notify', Integer(), server_default=text("'0'"))
)


arXiv_admin_state = Table(
    'arXiv_admin_state', metadata,
    Column('document_id', Integer(), unique=True),
    Column('timestamp', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")),
    Column('abs_timestamp', Integer()),
    Column('src_timestamp', Integer()),
    Column('state', Enum('pending', 'ok', 'bad'), nullable=False, server_default=text("'pending'")),
    Column('admin', String(32)),
    Column('comment', String(255))
)


arXiv_archive_category = Table(
    'arXiv_archive_category', metadata,
    Column('archive_id', String(16), primary_key=True, nullable=False, server_default=text("''")),
    Column('category_id', String(32), primary_key=True, nullable=False)
)


arXiv_archive_def = Table(
    'arXiv_archive_def', metadata,
    Column('archive', String(16), primary_key=True, server_default=text("''")),
    Column('name', String(255))
)


arXiv_archive_group = Table(
    'arXiv_archive_group', metadata,
    Column('archive_id', String(16), primary_key=True, nullable=False, server_default=text("''")),
    Column('group_id', String(16), primary_key=True, nullable=False, server_default=text("''"))
)


arXiv_aws_config = Table(
    'arXiv_aws_config', metadata,
    Column('domain', String(75), primary_key=True, nullable=False),
    Column('keyname', String(60), primary_key=True, nullable=False),
    Column('value', String(150))
)


arXiv_aws_files = Table(
    'arXiv_aws_files', metadata,
    Column('type', String(10), nullable=False, index=True, server_default=text("''")),
    Column('filename', String(100), primary_key=True, server_default=text("''")),
    Column('md5sum', String(50)),
    Column('content_md5sum', String(50)),
    Column('size', Integer()),
    Column('timestamp', DateTime),
    Column('yymm', String(4)),
    Column('seq_num', Integer()),
    Column('first_item', String(20)),
    Column('last_item', String(20)),
    Column('num_items', Integer())
)


arXiv_bib_feeds = Table(
    'arXiv_bib_feeds', metadata,
    Column('bib_id', Integer(), primary_key=True),
    Column('name', String(64), nullable=False, server_default=text("''")),
    Column('priority', Integer(), nullable=False, server_default=text("'0'")),
    Column('uri', String(255)),
    Column('identifier', String(255)),
    Column('version', String(255)),
    Column('strip_journal_ref', Integer(), nullable=False, server_default=text("'0'")),
    Column('concatenate_dupes', Integer()),
    Column('max_updates', Integer()),
    Column('email_errors', String(255)),
    Column('prune_ids', Text),
    Column('prune_regex', Text),
    Column('enabled', Integer(), server_default=text("'0'"))
)


arXiv_bib_updates = Table(
    'arXiv_bib_updates', metadata,
    Column('update_id', Integer(), primary_key=True),
    Column('document_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('bib_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('updated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")),
    Column('journal_ref', Text),
    Column('doi', Text)
)


arXiv_black_email = Table(
    'arXiv_black_email', metadata,
    Column('pattern', String(64))
)


arXiv_block_email = Table(
    'arXiv_block_email', metadata,
    Column('pattern', String(64))
)


arXiv_bogus_countries = Table(
    'arXiv_bogus_countries', metadata,
    Column('user_id', Integer(), primary_key=True, server_default=text("'0'")),
    Column('country_name', String(255), nullable=False, server_default=text("''"))
)


arXiv_category_def = Table(
    'arXiv_category_def', metadata,
    Column('category', String(32), primary_key=True),
    Column('name', String(255)),
    Column('active', Integer(), server_default=text("'1'"))
)


arXiv_dblp_authors = Table(
    'arXiv_dblp_authors', metadata,
    Column('author_id', Integer(), primary_key=True, unique=True),
    Column('name', String(40), unique=True)
)


arXiv_endorsement_domains = Table(
    'arXiv_endorsement_domains', metadata,
    Column('endorsement_domain', String(32), primary_key=True, server_default=text("''")),
    Column('endorse_all', Enum('y', 'n'), nullable=False, server_default=text("'n'")),
    Column('mods_endorse_all', Enum('y', 'n'), nullable=False, server_default=text("'n'")),
    Column('endorse_email', Enum('y', 'n'), nullable=False, server_default=text("'y'")),
    Column('papers_to_endorse', Integer(), nullable=False, server_default=text("'4'"))
)


arXiv_freeze_log = Table(
    'arXiv_freeze_log', metadata,
    Column('date', Integer(), primary_key=True, server_default=text("'0'"))
)


arXiv_group_def = Table(
    'arXiv_group_def', metadata,
    Column('archive_group', String(16), primary_key=True, server_default=text("''")),
    Column('name', String(255))
)


arXiv_groups = Table(
    'arXiv_groups', metadata,
    Column('group_id', String(16), primary_key=True, server_default=text("''")),
    Column('group_name', String(255), nullable=False, server_default=text("''")),
    Column('start_year', String(4), nullable=False, server_default=text("''"))
)


arXiv_licenses = Table(
    'arXiv_licenses', metadata,
    Column('name', String(255), primary_key=True),
    Column('label', String(255)),
    Column('active', Integer(), server_default=text("'1'")),
    Column('note', String(255)),
    Column('sequence', Integer())
)


arXiv_log_positions = Table(
    'arXiv_log_positions', metadata,
    Column('id', String(255), primary_key=True, server_default=text("''")),
    Column('position', Integer()),
    Column('date', Integer())
)


arXiv_monitor_klog = Table(
    'arXiv_monitor_klog', metadata,
    Column('t', Integer(), primary_key=True, server_default=text("'0'")),
    Column('sent', Integer())
)


arXiv_monitor_mailq = Table(
    'arXiv_monitor_mailq', metadata,
    Column('t', Integer(), primary_key=True, server_default=text("'0'")),
    Column('main_q', Integer(), nullable=False, server_default=text("'0'")),
    Column('local_q', Integer(), nullable=False, server_default=text("'0'")),
    Column('local_host_map', Integer(), nullable=False, server_default=text("'0'")),
    Column('local_timeout', Integer(), nullable=False, server_default=text("'0'")),
    Column('local_refused', Integer(), nullable=False, server_default=text("'0'")),
    Column('local_in_flight', Integer(), nullable=False, server_default=text("'0'"))
)


arXiv_monitor_mailsent = Table(
    'arXiv_monitor_mailsent', metadata,
    Column('t', Integer(), primary_key=True, server_default=text("'0'")),
    Column('sent', Integer())
)


arXiv_next_mail = Table(
    'arXiv_next_mail', metadata,
    Column('next_mail_id', Integer(), primary_key=True),
    Column('submission_id', Integer(), nullable=False),
    Column('document_id', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('paper_id', String(20)),
    Column('version', Integer(), nullable=False, server_default=text("'1'")),
    Column('type', String(255), nullable=False, server_default=text("'new'")),
    Column('extra', String(255)),
    Column('mail_id', String(6)),
    Column('is_written', Integer(), nullable=False, server_default=text("'0'")),
    Index('arXiv_next_mail_idx_document_id_version', 'document_id', 'version')
)


arXiv_orcid_config = Table(
    'arXiv_orcid_config', metadata,
    Column('domain', String(75), primary_key=True, nullable=False),
    Column('keyname', String(60), primary_key=True, nullable=False),
    Column('value', String(150))
)


arXiv_ownership_requests_papers = Table(
    'arXiv_ownership_requests_papers', metadata,
    Column('request_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('document_id', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Index('request_id', 'request_id', 'document_id', unique=True)
)


arXiv_paper_sessions = Table(
    'arXiv_paper_sessions', metadata,
    Column('paper_session_id', Integer(), primary_key=True),
    Column('paper_id', String(16), nullable=False, server_default=text("''")),
    Column('start_time', Integer(), nullable=False, server_default=text("'0'")),
    Column('end_time', Integer(), nullable=False, server_default=text("'0'")),
    Column('ip_name', String(16), nullable=False, server_default=text("''"))
)


arXiv_publish_log = Table(
    'arXiv_publish_log', metadata,
    Column('date', Integer(), primary_key=True, server_default=text("'0'"))
)


arXiv_refresh_list = Table(
    'arXiv_refresh_list', metadata,
    Column('filename', String(255)),
    Column('mtime', Integer(), index=True)
)


arXiv_reject_session_usernames = Table(
    'arXiv_reject_session_usernames', metadata,
    Column('username', String(64), primary_key=True, server_default=text("''"))
)


arXiv_sciencewise_pings = Table(
    'arXiv_sciencewise_pings', metadata,
    Column('paper_id_v', String(32), primary_key=True),
    Column('updated', DateTime)
)


arXiv_state = Table(
    'arXiv_state', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(24)),
    Column('value', String(24))
)


arXiv_stats_hourly = Table(
    'arXiv_stats_hourly', metadata,
    Column('ymd', Date, nullable=False, index=True),
    Column('hour', Integer(), nullable=False, index=True),
    Column('node_num', Integer(), nullable=False, index=True),
    Column('access_type', String(1), nullable=False, index=True),
    Column('connections', Integer(), nullable=False)
)


arXiv_stats_monthly_downloads = Table(
    'arXiv_stats_monthly_downloads', metadata,
    Column('ym', Date, primary_key=True),
    Column('downloads', Integer(), nullable=False)
)


arXiv_stats_monthly_submissions = Table(
    'arXiv_stats_monthly_submissions', metadata,
    Column('ym', Date, primary_key=True, server_default=text("'1970-01-01'")),
    Column('num_submissions', Integer(), nullable=False),
    Column('historical_delta', Integer(), nullable=False, server_default=text("'0'"))
)


arXiv_submitter_flags = Table(
    'arXiv_submitter_flags', metadata,
    Column('flag_id', Integer(), primary_key=True),
    Column('comment', String(255)),
    Column('pattern', String(255))
)


arXiv_suspect_emails = Table(
    'arXiv_suspect_emails', metadata,
    Column('id', Integer(), primary_key=True),
    Column('type', String(10), nullable=False),
    Column('pattern', Text, nullable=False),
    Column('comment', Text, nullable=False),
    Column('updated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
)


arXiv_titles = Table(
    'arXiv_titles', metadata,
    Column('paper_id', String(64), primary_key=True),
    Column('title', String(255), index=True),
    Column('report_num', String(255), index=True),
    Column('date', Date)
)


arXiv_trackback_pings = Table(
    'arXiv_trackback_pings', metadata,
    Column('trackback_id', Integer(), primary_key=True),
    Column('document_id', Integer(), index=True),
    Column('title', String(255), nullable=False, server_default=text("''")),
    Column('excerpt', String(255), nullable=False, server_default=text("''")),
    Column('url', String(255), nullable=False, index=True, server_default=text("''")),
    Column('blog_name', String(255), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('remote_addr', String(16), nullable=False, server_default=text("''")),
    Column('posted_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('is_stale', Integer(), nullable=False, server_default=text("'0'")),
    Column('approved_by_user', Integer(), nullable=False, server_default=text("'0'")),
    Column('approved_time', Integer(), nullable=False, server_default=text("'0'")),
    Column('status', Enum('pending', 'pending2', 'accepted', 'rejected', 'spam'), nullable=False, index=True, server_default=text("'pending'")),
    Column('site_id', Integer())
)


arXiv_trackback_sites = Table(
    'arXiv_trackback_sites', metadata,
    Column('pattern', String(255), nullable=False, index=True, server_default=text("''")),
    Column('site_id', Integer(), primary_key=True),
    Column('action', Enum('neutral', 'accept', 'reject', 'spam'), nullable=False, server_default=text("'neutral'"))
)


arXiv_tracking = Table(
    'arXiv_tracking', metadata,
    Column('tracking_id', Integer(), primary_key=True),
    Column('sword_id', Integer(), nullable=False, unique=True, server_default=text("'00000000'")),
    Column('paper_id', String(32), nullable=False),
    Column('submission_errors', Text),
    Column('timestamp', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
)


arXiv_updates = Table(
    'arXiv_updates', metadata,
    Column('document_id', Integer(), index=True),
    Column('version', Integer(), nullable=False, server_default=text("'1'")),
    Column('date', Date, index=True),
    Column('action', Enum('new', 'replace', 'absonly', 'cross', 'repcro')),
    Column('archive', String(20), index=True),
    Column('category', String(20), index=True),
    Index('document_id', 'document_id', 'date', 'action', 'category', unique=True)
)


arXiv_updates_tmp = Table(
    'arXiv_updates_tmp', metadata,
    Column('document_id', Integer()),
    Column('date', Date),
    Column('action', Enum('new', 'replace', 'absonly', 'cross', 'repcro')),
    Column('category', String(20)),
    Index('document_idkey', 'document_id', 'date', 'action', 'category', unique=True)
)


arXiv_white_email = Table(
    'arXiv_white_email', metadata,
    Column('pattern', String(64))
)


arXiv_xml_notifications = Table(
    'arXiv_xml_notifications', metadata,
    Column('control_id', Integer(), index=True),
    Column('type', Enum('submission', 'cross', 'jref')),
    Column('queued_date', Integer(), nullable=False, server_default=text("'0'")),
    Column('sent_date', Integer(), nullable=False, server_default=text("'0'")),
    Column('status', Enum('unsent', 'sent', 'failed'), index=True)
)


dbix_class_schema_versions = Table(
    'dbix_class_schema_versions', metadata,
    Column('version', String(10), primary_key=True),
    Column('installed', String(20), nullable=False)
)


demographics_backup = Table(
    'demographics_backup', metadata,
    Column('user_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('country', String(2), nullable=False, server_default=text("''")),
    Column('affiliation', String(255), nullable=False, server_default=text("''")),
    Column('url', String(255), nullable=False, server_default=text("''")),
    Column('type', Integer()),
    Column('os', Integer()),
    Column('archive', String(16)),
    Column('subject_class', String(16)),
    Column('original_subject_classes', String(255), nullable=False, server_default=text("''")),
    Column('flag_group_physics', Integer()),
    Column('flag_group_math', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_group_cs', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_group_nlin', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_proxy', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_journal', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_xml', Integer(), nullable=False, server_default=text("'0'")),
    Column('dirty', Integer(), nullable=False, server_default=text("'2'")),
    Column('flag_group_test', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_suspect', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_group_q_bio', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_no_upload', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_no_endorse', Integer(), nullable=False, server_default=text("'0'")),
    Column('veto_status', Enum('ok', 'no-endorse', 'no-upload'), server_default=text("'ok'"))
)


sessions = Table(
    'sessions', metadata,
    Column('id', String(72), primary_key=True),
    Column('session_data', Text),
    Column('expires', Integer())
)


tapir_countries = Table(
    'tapir_countries', metadata,
    Column('digraph', String(2), primary_key=True, server_default=text("''")),
    Column('country_name', String(255), nullable=False, server_default=text("''")),
    Column('rank', Integer(), nullable=False, server_default=text("'255'"))
)


tapir_email_log = Table(
    'tapir_email_log', metadata,
    Column('mail_id', Integer(), primary_key=True),
    Column('reference_type', String(1)),
    Column('reference_id', Integer()),
    Column('sent_date', Integer(), nullable=False, server_default=text("'0'")),
    Column('email', String(50), nullable=False, server_default=text("''")),
    Column('flag_bounced', Integer()),
    Column('mailing_id', Integer(), index=True),
    Column('template_id', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_error_log = Table(
    'tapir_error_log', metadata,
    Column('error_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('user_id', Integer(), index=True),
    Column('session_id', Integer(), index=True),
    Column('ip_addr', String(16), nullable=False, index=True, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(32), nullable=False, index=True, server_default=text("''")),
    Column('message', String(32), nullable=False, index=True, server_default=text("''")),
    Column('url', String(255), nullable=False, server_default=text("''")),
    Column('error_url', String(255), nullable=False, server_default=text("''"))
)


tapir_integer_variables = Table(
    'tapir_integer_variables', metadata,
    Column('variable_id', String(32), primary_key=True, server_default=text("''")),
    Column('value', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_nicknames_audit = Table(
    'tapir_nicknames_audit', metadata,
    Column('nick_id', Integer(), primary_key=True, server_default=text("'0'")),
    Column('creation_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('creation_ip_num', String(16), nullable=False, index=True, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, index=True, server_default=text("''"))
)


tapir_no_cookies = Table(
    'tapir_no_cookies', metadata,
    Column('log_date', Integer(), nullable=False, server_default=text("'0'")),
    Column('ip_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('session_data', String(255), nullable=False, server_default=text("''")),
    Column('user_agent', String(255), nullable=False, server_default=text("''"))
)


tapir_periodic_tasks_log = Table(
    'tapir_periodic_tasks_log', metadata,
    Column('t', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('entry', Text)
)


tapir_policy_classes = Table(
    'tapir_policy_classes', metadata,
    Column('class_id', Integer(), primary_key=True),
    Column('name', String(64), nullable=False, server_default=text("''")),
    Column('description', Text, nullable=False),
    Column('password_storage', Integer(), nullable=False, server_default=text("'0'")),
    Column('recovery_policy', Integer(), nullable=False, server_default=text("'0'")),
    Column('permanent_login', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_presessions = Table(
    'tapir_presessions', metadata,
    Column('presession_id', Integer(), primary_key=True),
    Column('ip_num', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('created_at', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_string_variables = Table(
    'tapir_string_variables', metadata,
    Column('variable_id', String(32), primary_key=True, server_default=text("''")),
    Column('value', Text, nullable=False)
)


tapir_strings = Table(
    'tapir_strings', metadata,
    Column('name', String(32), primary_key=True, nullable=False, server_default=text("''")),
    Column('module', String(32), primary_key=True, nullable=False, server_default=text("''")),
    Column('language', String(32), primary_key=True, nullable=False, server_default=text("'en'")),
    Column('string', Text, nullable=False)
)


Subscription_UniversalInstitutionContact = Table(
    'Subscription_UniversalInstitutionContact', metadata,
    Column('email', String(255)),
    Column('sid', ForeignKey('Subscription_UniversalInstitution.id', ondelete='CASCADE'), nullable=False, index=True),
    Column('active', Integer(), server_default=text("'0'")),
    Column('contact_name', String(255)),
    Column('id', Integer(), primary_key=True),
    Column('phone', String(255)),
    Column('note', String(2048))
)


Subscription_UniversalInstitutionIP = Table(
    'Subscription_UniversalInstitutionIP', metadata,
    Column('sid', ForeignKey('Subscription_UniversalInstitution.id', ondelete='CASCADE'), nullable=False, index=True),
    Column('id', Integer(), primary_key=True),
    Column('exclude', Integer(), server_default=text("'0'")),
    Column('end', BigInteger(), nullable=False, index=True),
    Column('start', BigInteger(), nullable=False, index=True),
    Index('ip', 'start', 'end')
)


arXiv_archives = Table(
    'arXiv_archives', metadata,
    Column('archive_id', String(16), primary_key=True, server_default=text("''")),
    Column('in_group', ForeignKey('arXiv_groups.group_id'), nullable=False, index=True, server_default=text("''")),
    Column('archive_name', String(255), nullable=False, server_default=text("''")),
    Column('start_date', String(4), nullable=False, server_default=text("''")),
    Column('end_date', String(4), nullable=False, server_default=text("''")),
    Column('subdivided', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_save_post_variables = Table(
    'tapir_save_post_variables', metadata,
    Column('presession_id', ForeignKey('tapir_presessions.presession_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('name', String(255)),
    Column('value',String, nullable=False),
    Column('seq', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_users = Table(
    'tapir_users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('first_name', String(50), index=True),
    Column('last_name', String(50), index=True),
    Column('suffix_name', String(50)),
    Column('share_first_name', Integer(), nullable=False, server_default=text("'1'")),
    Column('share_last_name', Integer(), nullable=False, server_default=text("'1'")),
    Column('email', String(255), nullable=False, unique=True, server_default=text("''")),
    Column('share_email', Integer(), nullable=False, server_default=text("'8'")),
    Column('email_bouncing', Integer(), nullable=False, server_default=text("'0'")),
    Column('policy_class', ForeignKey('tapir_policy_classes.class_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('joined_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('joined_ip_num', String(16), index=True),
    Column('joined_remote_host', String(255), nullable=False, server_default=text("''")),
    Column('flag_internal', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_edit_users', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_edit_system', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_email_verified', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_approved', Integer(), nullable=False, index=True, server_default=text("'1'")),
    Column('flag_deleted', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_banned', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_wants_email', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_html_email', Integer(), nullable=False, server_default=text("'0'")),
    Column('tracking_cookie', String(255), nullable=False, index=True, server_default=text("''")),
    Column('flag_allow_tex_produced', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_can_lock', Integer(), nullable=False, index=True, server_default=text("'0'"))
)


arXiv_author_ids = Table(
    'arXiv_author_ids', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True),
    Column('author_id', String(50), nullable=False, index=True),
    Column('updated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
)


arXiv_bad_pw = Table(
    'arXiv_bad_pw', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'"))
)


arXiv_categories = Table(
    'arXiv_categories', metadata,
    Column('archive', ForeignKey('arXiv_archives.archive_id'), primary_key=True, nullable=False, server_default=text("''")),
    Column('subject_class', String(16), primary_key=True, nullable=False, server_default=text("''")),
    Column('definitive', Integer(), nullable=False, server_default=text("'0'")),
    Column('active', Integer(), nullable=False, server_default=text("'0'")),
    Column('category_name', String(255)),
    Column('endorse_all', Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'")),
    Column('endorse_email', Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'")),
    Column('papers_to_endorse', Integer(), nullable=False, server_default=text("'0'")),
    Column('endorsement_domain', ForeignKey('arXiv_endorsement_domains.endorsement_domain'), index=True)
)


arXiv_control_holds = Table(
    'arXiv_control_holds', metadata,
    Column('hold_id', Integer(), primary_key=True),
    Column('control_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('hold_type', Enum('submission', 'cross', 'jref'), nullable=False, index=True, server_default=text("'submission'")),
    Column('hold_status', Enum('held', 'extended', 'accepted', 'rejected'), nullable=False, index=True, server_default=text("'held'")),
    Column('hold_reason', String(255), nullable=False, index=True, server_default=text("''")),
    Column('hold_data', String(255), nullable=False, server_default=text("''")),
    Column('origin', Enum('auto', 'user', 'admin', 'moderator'), nullable=False, index=True, server_default=text("'auto'")),
    Column('placed_by', ForeignKey('tapir_users.user_id'), index=True),
    Column('last_changed_by', ForeignKey('tapir_users.user_id'), index=True),
    Index('control_id', 'control_id', 'hold_type', unique=True)
)


arXiv_documents = Table(
    'arXiv_documents', metadata,
    Column('document_id', Integer(), primary_key=True),
    Column('paper_id', String(20), nullable=False, unique=True, server_default=text("''")),
    Column('title', String(255), nullable=False, index=True, server_default=text("''")),
    Column('authors', Text),
    Column('submitter_email', String(64), nullable=False, index=True, server_default=text("''")),
    Column('submitter_id', ForeignKey('tapir_users.user_id'), index=True),
    Column('dated', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('primary_subject_class', String(16)),
    Column('created', DateTime)
)


arXiv_duplicates = Table(
    'arXiv_duplicates', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('email', String(255)),
    Column('username', String(255))
)


arXiv_moderator_api_key = Table(
    'arXiv_moderator_api_key', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")),
    Column('valid', Integer(), nullable=False, server_default=text("'1'")),
    Column('issued_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('issued_to', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''"))
)


arXiv_orcid_ids = Table(
    'arXiv_orcid_ids', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True),
    Column('orcid', String(19), nullable=False, index=True),
    Column('authenticated', Integer(), nullable=False, server_default=text("'0'")),
    Column('updated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
)


arXiv_queue_view = Table(
    'arXiv_queue_view', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id', ondelete='CASCADE'), primary_key=True, server_default=text("'0'")),
    Column('last_view', DateTime),
    Column('second_last_view', DateTime),
    Column('total_views', Integer(), nullable=False, server_default=text("'0'"))
)


arXiv_suspicious_names = Table(
    'arXiv_suspicious_names', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, server_default=text("'0'")),
    Column('full_name', String(255), nullable=False, server_default=text("''"))
)


arXiv_sword_licenses = Table(
    'arXiv_sword_licenses', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True),
    Column('license', String(127)),
    Column('updated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
)


tapir_address = Table(
    'tapir_address', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('address_type', Integer(), primary_key=True, nullable=False, index=True, server_default=text("'0'")),
    Column('company', String(80), nullable=False, server_default=text("''")),
    Column('line1', String(80), nullable=False, server_default=text("''")),
    Column('line2', String(80), nullable=False, server_default=text("''")),
    Column('city', String(50), nullable=False, index=True, server_default=text("''")),
    Column('state', String(50), nullable=False, server_default=text("''")),
    Column('postal_code', String(16), nullable=False, index=True, server_default=text("''")),
    Column('country', ForeignKey('tapir_countries.digraph'), nullable=False, index=True, server_default=text("''")),
    Column('share_addr', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_demographics = Table(
    'tapir_demographics', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, server_default=text("'0'")),
    Column('gender', Integer(), nullable=False, server_default=text("'0'")),
    Column('share_gender', Integer(), nullable=False, server_default=text("'16'")),
    Column('birthday', Date, index=True),
    Column('share_birthday', Integer(), nullable=False, server_default=text("'16'")),
    Column('country', ForeignKey('tapir_countries.digraph'), nullable=False, index=True, server_default=text("''")),
    Column('share_country', Integer(), nullable=False, server_default=text("'16'")),
    Column('postal_code', String(16), nullable=False, index=True, server_default=text("''"))
)


tapir_email_change_tokens = Table(
    'tapir_email_change_tokens', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('old_email', String(50), nullable=False, server_default=text("''")),
    Column('new_email', String(50), nullable=False, server_default=text("''")),
    Column('secret', String(32), primary_key=True, nullable=False, index=True, server_default=text("''")),
    Column('tapir_dest', String(255), nullable=False, server_default=text("''")),
    Column('issued_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('issued_to', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(16), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('used', Integer(), nullable=False, server_default=text("'0'")),
    Column('session_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('consumed_when', Integer()),
    Column('consumed_from', String(16))
)


tapir_email_templates = Table(
    'tapir_email_templates', metadata,
    Column('template_id', Integer(), primary_key=True),
    Column('short_name', String(32), nullable=False, server_default=text("''")),
    Column('lang', String(2), nullable=False, server_default=text("'en'")),
    Column('long_name', String(255), nullable=False, server_default=text("''")),
    Column('data', Text, nullable=False),
    Column('sql_statement', Text, nullable=False),
    Column('update_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('created_by', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('updated_by', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('workflow_status', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_system', Integer(), nullable=False, server_default=text("'0'")),
    Index('short_name', 'short_name', 'lang', unique=True)
)


tapir_email_tokens = Table(
    'tapir_email_tokens', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), primary_key=True, nullable=False, index=True, server_default=text("''")),
    Column('tapir_dest', String(255), nullable=False, server_default=text("''")),
    Column('issued_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('issued_to', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('wants_perm_token', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_nicknames = Table(
    'tapir_nicknames', metadata,
    Column('nick_id', Integer(), primary_key=True),
    Column('nickname', String(20), nullable=False, unique=True, server_default=text("''")),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, server_default=text("'0'")),
    Column('user_seq', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_valid', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('role', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('policy', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_primary', Integer(), nullable=False, server_default=text("'0'")),
    Index('user_id', 'user_id', 'user_seq', unique=True)
)


tapir_phone = Table(
    'tapir_phone', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('phone_type', Integer(), primary_key=True, nullable=False, index=True, server_default=text("'0'")),
    Column('phone_number', String(32), index=True),
    Column('share_phone', Integer(), nullable=False, server_default=text("'16'"))
)


tapir_recovery_tokens = Table(
    'tapir_recovery_tokens', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), primary_key=True, nullable=False, index=True, server_default=text("''")),
    Column('valid', Integer(), nullable=False, server_default=text("'1'")),
    Column('tapir_dest', String(255), nullable=False, server_default=text("''")),
    Column('issued_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('issued_to', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''"))
)


tapir_sessions = Table(
    'tapir_sessions', metadata,
    Column('session_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('last_reissue', Integer(), nullable=False, server_default=text("'0'")),
    Column('start_time', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('end_time', Integer(), nullable=False, index=True, server_default=text("'0'"))
)


tapir_users_hot = Table(
    'tapir_users_hot', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, server_default=text("'0'")),
    Column('last_login', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('second_last_login', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('number_sessions', Integer(), nullable=False, index=True, server_default=text("'0'"))
)


tapir_users_password = Table(
    'tapir_users_password', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, server_default=text("'0'")),
    Column('password_storage', Integer(), nullable=False, server_default=text("'0'")),
    Column('password_enc', String(50), nullable=False, server_default=text("''"))
)


arXiv_admin_metadata = Table(
    'arXiv_admin_metadata', metadata,
    Column('metadata_id', Integer(), primary_key=True, index=True),
    Column('document_id', ForeignKey('arXiv_documents.document_id', ondelete='CASCADE'), index=True),
    Column('paper_id', String(64)),
    Column('created', DateTime),
    Column('updated', DateTime),
    Column('submitter_name', String(64)),
    Column('submitter_email', String(64)),
    Column('history', Text),
    Column('source_size', Integer()),
    Column('source_type', String(12)),
    Column('title', Text),
    Column('authors', Text),
    Column('category_string', String(255)),
    Column('comments', Text),
    Column('proxy', String(255)),
    Column('report_num', Text),
    Column('msc_class', String(255)),
    Column('acm_class', String(255)),
    Column('journal_ref', Text),
    Column('doi', String(255)),
    Column('abstract', Text),
    Column('license', String(255)),
    Column('version', Integer(), nullable=False, server_default=text("'1'")),
    Column('modtime', Integer()),
    Column('is_current', Integer(), server_default=text("'0'")),
    Index('pidv', 'paper_id', 'version', unique=True)
)


arXiv_bogus_subject_class = Table(
    'arXiv_bogus_subject_class', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('category_name', String(255), nullable=False, server_default=text("''"))
)


arXiv_cross_control = Table(
    'arXiv_cross_control', metadata,
    Column('control_id', Integer(), primary_key=True),
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, server_default=text("'0'")),
    Column('version', Integer(), nullable=False, server_default=text("'0'")),
    Column('desired_order', Integer(), nullable=False, server_default=text("'0'")),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('status', Enum('new', 'frozen', 'published', 'rejected'), nullable=False, index=True, server_default=text("'new'")),
    Column('flag_must_notify', Enum('0', '1'), server_default=text("'1'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('request_date', Integer(), nullable=False, server_default=text("'0'")),
    Column('freeze_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('publish_date', Integer(), nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class']),
    Index('document_id_cross_control', 'document_id', 'version'),
    Index('archive_cross_control', 'archive', 'subject_class')
)


arXiv_dblp = Table(
    'arXiv_dblp', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id'), primary_key=True, server_default=text("'0'")),
    Column('url', String(80))
)


arXiv_dblp_document_authors = Table(
    'arXiv_dblp_document_authors', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id'), primary_key=True, nullable=False, index=True),
    Column('author_id', ForeignKey('arXiv_dblp_authors.author_id'), primary_key=True, nullable=False, index=True, server_default=text("'0'")),
    Column('position', Integer(), nullable=False, server_default=text("'0'"))
)


arXiv_demographics = Table(
    'arXiv_demographics', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, server_default=text("'0'")),
    Column('country', String(2), nullable=False, index=True, server_default=text("''")),
    Column('affiliation', String(255), nullable=False, server_default=text("''")),
    Column('url', String(255), nullable=False, server_default=text("''")),
    Column('type', Integer(), index=True),
    Column('archive', String(16)),
    Column('subject_class', String(16)),
    Column('original_subject_classes', String(255), nullable=False, server_default=text("''")),
    Column('flag_group_physics', Integer(), index=True),
    Column('flag_group_math', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_group_cs', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_group_nlin', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_proxy', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_journal', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_xml', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('dirty', Integer(), nullable=False, server_default=text("'2'")),
    Column('flag_group_test', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_suspect', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_group_q_bio', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_group_q_fin', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_group_stat', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_group_eess', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_group_econ', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('veto_status', Enum('ok', 'no-endorse', 'no-upload', 'no-replace'), nullable=False, server_default=text("'ok'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class']),
    Index('archive', 'archive', 'subject_class')
)


arXiv_document_category = Table(
    'arXiv_document_category', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True, server_default=text("'0'")),
    Column('category', ForeignKey('arXiv_category_def.category'), primary_key=True, nullable=False, index=True),
    Column('is_primary', Integer(), nullable=False, server_default=text("'0'"))
)


arXiv_endorsement_requests = Table(
    'arXiv_endorsement_requests', metadata,
    Column('request_id', Integer(), primary_key=True),
    Column('endorsee_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('secret', String(16), nullable=False, unique=True, server_default=text("''")),
    Column('flag_valid', Integer(), nullable=False, server_default=text("'0'")),
    Column('issued_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('point_value', Integer(), nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class']),
    Index('endorsee_id_2', 'endorsee_id', 'archive', 'subject_class', unique=True),
    Index('archive_endorsement_req', 'archive', 'subject_class')
)


arXiv_in_category = Table(
    'arXiv_in_category', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('is_primary', Integer(), nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class']),
    Index('archive_in_category', 'archive', 'subject_class', 'document_id', unique=True),
    Index('arXiv_in_category_mp', 'archive', 'subject_class')
)


arXiv_jref_control = Table(
    'arXiv_jref_control', metadata,
    Column('control_id', Integer(), primary_key=True),
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, server_default=text("'0'")),
    Column('version', Integer(), nullable=False, server_default=text("'0'")),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('status', Enum('new', 'frozen', 'published', 'rejected'), nullable=False, index=True, server_default=text("'new'")),
    Column('flag_must_notify', Enum('0', '1'), server_default=text("'1'")),
    Column('jref', String(255), nullable=False, server_default=text("''")),
    Column('request_date', Integer(), nullable=False, server_default=text("'0'")),
    Column('freeze_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('publish_date', Integer(), nullable=False, server_default=text("'0'")),
    Index('document_id_jref_control', 'document_id', 'version', unique=True)
)


arXiv_metadata = Table(
    'arXiv_metadata', metadata,
    Column('metadata_id', Integer(), primary_key=True),
    Column('document_id', ForeignKey('arXiv_documents.document_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, server_default=text("'0'")),
    Column('paper_id', String(64), nullable=False),
    Column('created', DateTime),
    Column('updated', DateTime),
    Column('submitter_id', ForeignKey('tapir_users.user_id'), index=True),
    Column('submitter_name', String(64), nullable=False),
    Column('submitter_email', String(64), nullable=False),
    Column('source_size', Integer()),
    Column('source_format', String(12)),
    Column('source_flags', String(12)),
    Column('title', Text),
    Column('authors', Text),
    Column('abs_categories', String(255)),
    Column('comments', Text),
    Column('proxy', String(255)),
    Column('report_num', Text),
    Column('msc_class', String(255)),
    Column('acm_class', String(255)),
    Column('journal_ref', Text),
    Column('doi', String(255)),
    Column('abstract', Text),
    Column('license', ForeignKey('arXiv_licenses.name'), index=True),
    Column('version', Integer(), nullable=False, server_default=text("'1'")),
    Column('modtime', Integer()),
    Column('is_current', Integer(), server_default=text("'1'")),
    Column('is_withdrawn', Integer(), nullable=False, server_default=text("'0'")),
    Index('pidv_metadata', 'paper_id', 'version', unique=True)
)


arXiv_mirror_list = Table(
    'arXiv_mirror_list', metadata,
    Column('mirror_list_id', Integer(), primary_key=True),
    Column('created', DateTime),
    Column('updated', DateTime),
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('version', Integer(), nullable=False, server_default=text("'1'")),
    Column('write_source', Integer(), nullable=False, server_default=text("'0'")),
    Column('write_abs', Integer(), nullable=False, server_default=text("'0'")),
    Column('is_written', Integer(), nullable=False, server_default=text("'0'"))
)


arXiv_moderators = Table(
    'arXiv_moderators', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('archive', ForeignKey('arXiv_archive_group.archive_id'), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('is_public', Integer(), nullable=False, server_default=text("'0'")),
    Column('no_email', Integer(), index=True, server_default=text("'0'")),
    Column('no_web_email', Integer(), index=True, server_default=text("'0'")),
    Column('no_reply_to', Integer(), index=True, server_default=text("'0'")),
    Column('daily_update', Integer(), server_default=text("'0'")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class']),
    Index('arxiv_moderator_idx_user_id', 'archive', 'subject_class', 'user_id', unique=True)
)


arXiv_paper_owners = Table(
    'arXiv_paper_owners', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, server_default=text("'0'")),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('date', Integer(), nullable=False, server_default=text("'0'")),
    Column('added_by', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('remote_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(32), nullable=False, server_default=text("''")),
    Column('valid', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_author', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_auto', Integer(), nullable=False, server_default=text("'1'")),
    Index('document_id_paper_owners', 'document_id', 'user_id', unique=True)
)


arXiv_paper_pw = Table(
    'arXiv_paper_pw', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id'), primary_key=True, server_default=text("'0'")),
    Column('password_storage', Integer()),
    Column('password_enc', String(50))
)


arXiv_questionable_categories = Table(
    'arXiv_questionable_categories', metadata,
    Column('archive', String(16), primary_key=True, nullable=False, server_default=text("''")),
    Column('subject_class', String(16), primary_key=True, nullable=False, server_default=text("''")),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class'])
)


arXiv_show_email_requests = Table(
    'arXiv_show_email_requests', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, server_default=text("'0'")),
    Column('session_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('dated', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_allowed', Integer(), nullable=False, server_default=text("'0'")),
    Column('remote_addr', String(16), nullable=False, index=True, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('request_id', Integer(), primary_key=True),
    Index('user_id_show_email_req', 'user_id', 'dated')
)


arXiv_submission_control = Table(
    'arXiv_submission_control', metadata,
    Column('control_id', Integer(), primary_key=True),
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, server_default=text("'0'")),
    Column('version', Integer(), nullable=False, server_default=text("'0'")),
    Column('pending_paper_id', String(20), nullable=False, index=True, server_default=text("''")),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('status', Enum('new', 'frozen', 'published', 'rejected'), nullable=False, index=True, server_default=text("'new'")),
    Column('flag_must_notify', Enum('0', '1'), server_default=text("'1'")),
    Column('request_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('freeze_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('publish_date', Integer(), nullable=False, server_default=text("'0'")),
    Index('document_id_submission_control', 'document_id', 'version', unique=True)
)


arXiv_submissions = Table(
    'arXiv_submissions', metadata,
    Column('submission_id', Integer(), primary_key=True),
    Column('document_id', ForeignKey('arXiv_documents.document_id', ondelete='CASCADE', onupdate='CASCADE'), index=True),
    Column('doc_paper_id', String(20), index=True),
    Column('sword_id', ForeignKey('arXiv_tracking.sword_id'), index=True),
    Column('userinfo', Integer(), server_default=text("'0'")),
    Column('is_author', Integer(), nullable=False, server_default=text("'0'")),
    Column('agree_policy', Integer(), server_default=text("'0'")),
    Column('viewed', Integer(), server_default=text("'0'")),
    Column('stage', Integer(), server_default=text("'0'")),
    Column('submitter_id', ForeignKey('tapir_users.user_id', ondelete='CASCADE', onupdate='CASCADE'), index=True),
    Column('submitter_name', String(64)),
    Column('submitter_email', String(64)),
    Column('created', DateTime),
    Column('updated', DateTime),
    Column('status', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('sticky_status', Integer()),
    Column('must_process', Integer(), server_default=text("'1'")),
    Column('submit_time', DateTime),
    Column('release_time', DateTime),
    Column('source_size', Integer(), server_default=text("'0'")),
    Column('source_format', String(12)),
    Column('source_flags', String(12)),
    Column('has_pilot_data', Integer()),
    Column('is_withdrawn', Integer(), nullable=False, server_default=text("'0'")),
    Column('title', Text),
    Column('authors', Text),
    Column('comments', Text),
    Column('proxy', String(255)),
    Column('report_num', Text),
    Column('msc_class', String(255)),
    Column('acm_class', String(255)),
    Column('journal_ref', Text),
    Column('doi', String(255)),
    Column('abstract', Text),
    Column('license', ForeignKey('arXiv_licenses.name', onupdate='CASCADE'), index=True),
    Column('version', Integer(), nullable=False, server_default=text("'1'")),
    Column('type', String(8), index=True),
    Column('is_ok', Integer(), index=True),
    Column('admin_ok', Integer()),
    Column('allow_tex_produced', Integer(), server_default=text("'0'")),
    Column('is_oversize', Integer(), server_default=text("'0'")),
    Column('remote_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('package', String(255), nullable=False, server_default=text("''")),
    Column('rt_ticket_id', Integer(), index=True),
    Column('auto_hold', Integer(), server_default=text("'0'")),
    Column('is_locked', Integer(), nullable=False, index=True, server_default=text("'0'"))
)


arXiv_top_papers = Table(
    'arXiv_top_papers', metadata,
    Column('from_week', Date, primary_key=True, nullable=False, server_default=text("'1970-01-01'")),
    Column('class', String(1), primary_key=True, nullable=False, server_default=text("''")),
    Column('rank', Integer(), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('document_id', ForeignKey('arXiv_documents.document_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('viewers', Integer(), nullable=False, server_default=text("'0'"))
)


arXiv_versions = Table(
    'arXiv_versions', metadata,
    Column('document_id', ForeignKey('arXiv_documents.document_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('version', Integer(), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('request_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('freeze_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('publish_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('flag_current', Integer(), nullable=False, server_default=text("'0'"))
)


tapir_admin_audit = Table(
    'tapir_admin_audit', metadata,
    Column('log_date', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('session_id', ForeignKey('tapir_sessions.session_id'), index=True),
    Column('ip_addr', String(16), nullable=False, index=True, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('admin_user', ForeignKey('tapir_users.user_id'), index=True),
    Column('affected_user', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('action', String(32), nullable=False, server_default=text("''")),
    Column('data', Text, nullable=False,
           # E   sqlalchemy.exc.InternalError: (pymysql.err.InternalError) (1170, "BLOB/TEXT column 'data' used in key specification without a key length")
           # index=True
           ),
    Column('comment', Text, nullable=False),
    Column('entry_id', Integer(), primary_key=True)
)


tapir_email_change_tokens_used = Table(
    'tapir_email_change_tokens_used', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('used_from', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', ForeignKey('tapir_sessions.session_id'), nullable=False, index=True, server_default=text("'0'"))
)


tapir_email_headers = Table(
    'tapir_email_headers', metadata,
    Column('template_id', ForeignKey('tapir_email_templates.template_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('header_name', String(32), primary_key=True, nullable=False, server_default=text("''")),
    Column('header_content', String(255), nullable=False, server_default=text("''"))
)


tapir_email_mailings = Table(
    'tapir_email_mailings', metadata,
    Column('mailing_id', Integer(), primary_key=True),
    Column('template_id', ForeignKey('tapir_email_templates.template_id'), index=True),
    Column('created_by', ForeignKey('tapir_users.user_id'), index=True),
    Column('sent_by', ForeignKey('tapir_users.user_id'), index=True),
    Column('created_date', Integer()),
    Column('sent_date', Integer()),
    Column('complete_date', Integer()),
    Column('mailing_name', String(255)),
    Column('comment', Text)
)


tapir_email_tokens_used = Table(
    'tapir_email_tokens_used', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('used_from', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', ForeignKey('tapir_sessions.session_id'), nullable=False, index=True, server_default=text("'0'"))
)


tapir_permanent_tokens = Table(
    'tapir_permanent_tokens', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")),
    Column('valid', Integer(), nullable=False, server_default=text("'1'")),
    Column('issued_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('issued_to', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', ForeignKey('tapir_sessions.session_id'), nullable=False, index=True, server_default=text("'0'"))
)


tapir_permanent_tokens_used = Table(
    'tapir_permanent_tokens_used', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), index=True),
    Column('secret', String(32), nullable=False, server_default=text("''")),
    Column('used_when', Integer()),
    Column('used_from', String(16)),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', ForeignKey('tapir_sessions.session_id'), nullable=False, index=True, server_default=text("'0'"))
)


tapir_recovery_tokens_used = Table(
    'tapir_recovery_tokens_used', metadata,
    Column('user_id', ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('secret', String(32), primary_key=True, nullable=False, server_default=text("''")),
    Column('used_when', Integer()),
    Column('used_from', String(16)),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('session_id', ForeignKey('tapir_sessions.session_id'), index=True)
)


tapir_sessions_audit = Table(
    'tapir_sessions_audit', metadata,
    Column('session_id', ForeignKey('tapir_sessions.session_id'), primary_key=True, server_default=text("'0'")),
    Column('ip_addr', String(16), nullable=False, index=True, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, index=True, server_default=text("''"))
)


arXiv_endorsement_requests_audit = Table(
    'arXiv_endorsement_requests_audit', metadata,
    Column('request_id', ForeignKey('arXiv_endorsement_requests.request_id'), primary_key=True, server_default=text("'0'")),
    Column('session_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('remote_addr', String(16)),
    Column('remote_host', String(255)),
    Column('tracking_cookie', String(255))
)


arXiv_endorsements = Table(
    'arXiv_endorsements', metadata,
    Column('endorsement_id', Integer(), primary_key=True),
    Column('endorser_id', ForeignKey('tapir_users.user_id'), index=True),
    Column('endorsee_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('archive', String(16), nullable=False, server_default=text("''")),
    Column('subject_class', String(16), nullable=False, server_default=text("''")),
    Column('flag_valid', Integer(), nullable=False, server_default=text("'0'")),
    Column('type', Enum('user', 'admin', 'auto')),
    Column('point_value', Integer(), nullable=False, server_default=text("'0'")),
    Column('issued_when', Integer(), nullable=False, server_default=text("'0'")),
    Column('request_id', ForeignKey('arXiv_endorsement_requests.request_id'), index=True),
    ForeignKeyConstraint(['archive', 'subject_class'], ['arXiv_categories.archive', 'arXiv_categories.subject_class']),
    Index('endorser_id_2', 'endorser_id', 'endorsee_id', 'archive', 'subject_class', unique=True),
    Index('archive_endorsement', 'archive', 'subject_class')
)


arXiv_ownership_requests = Table(
    'arXiv_ownership_requests', metadata,
    Column('request_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True, server_default=text("'0'")),
    Column('endorsement_request_id', ForeignKey('arXiv_endorsement_requests.request_id'), index=True),
    Column('workflow_status', Enum('pending', 'accepted', 'rejected'), nullable=False, server_default=text("'pending'"))
)


arXiv_pilot_datasets = Table(
    'arXiv_pilot_datasets', metadata,
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id'), primary_key=True),
    Column('numfiles', Integer(), server_default=text("'0'")),
    Column('feed_url', String(256)),
    Column('manifestation', String(256)),
    Column('published', Integer(), server_default=text("'0'")),
    Column('created', DateTime, nullable=False),
    Column('last_checked', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
)


arXiv_pilot_files = Table(
    'arXiv_pilot_files', metadata,
    Column('file_id', Integer(), primary_key=True),
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id'), nullable=False, index=True),
    Column('filename', String(256), server_default=text("''")),
    Column('entity_url', String(256)),
    Column('description', String(80)),
    Column('byRef', Integer(), server_default=text("'1'"))
)


arXiv_submission_abs_classifier_data = Table(
    'arXiv_submission_abs_classifier_data', metadata,
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE'), primary_key=True, server_default=text("'0'")),
    Column('json', Text),
    Column('last_update', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")),
    Column('status', Enum('processing', 'success', 'failed', 'no connection')),
    Column('message', Text),
    Column('is_oversize', Integer(), server_default=text("'0'")),
    Column('suggested_primary', Text),
    Column('suggested_reason', Text),
    Column('autoproposal_primary', Text),
    Column('autoproposal_reason', Text),
    Column('classifier_service_version', Text),
    Column('classifier_model_version', Text)
)


arXiv_submission_category = Table(
    'arXiv_submission_category', metadata,
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('category', ForeignKey('arXiv_category_def.category'), primary_key=True, nullable=False, index=True, server_default=text("''")),
    Column('is_primary', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('is_published', Integer(), index=True, server_default=text("'0'"))
)


arXiv_submission_category_proposal = Table(
    'arXiv_submission_category_proposal', metadata,
    Column('proposal_id', Integer(), primary_key=True, nullable=False, index=True, autoincrement=True),
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
    Column('category', ForeignKey('arXiv_category_def.category'), nullable=False, index=True),
    Column('is_primary', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('proposal_status', Integer(), server_default=text("'0'")),
    Column('user_id', ForeignKey('tapir_users.user_id'), nullable=False, index=True),
    Column('updated', DateTime),
    Column('proposal_comment_id', ForeignKey('arXiv_admin_log.id'), index=True),
    Column('response_comment_id', ForeignKey('arXiv_admin_log.id'), index=True)
)


arXiv_submission_classifier_data = Table(
    'arXiv_submission_classifier_data', metadata,
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE'), primary_key=True, server_default=text("'0'")),
    Column('json', Text),
    Column('last_update', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")),
    Column('status', Enum('processing', 'success', 'failed', 'no connection')),
    Column('message', Text),
    Column('is_oversize', Integer(), server_default=text("'0'"))
)


arXiv_submission_near_duplicates = Table(
    'arXiv_submission_near_duplicates', metadata,
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE'), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('matching_id', Integer(), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('similarity', Numeric(2, 1), nullable=False),
    Column('last_update', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")),
    Index('match', 'submission_id', 'matching_id', unique=True)
)


arXiv_submission_view_flag = Table(
    'arXiv_submission_view_flag', metadata,
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE'), primary_key=True, nullable=False),
    Column('flag', Integer(), server_default=text("'0'")),
    Column('user_id', ForeignKey('tapir_users.user_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('updated', DateTime)
)


arXiv_versions_checksum = Table(
    'arXiv_versions_checksum', metadata,
    Column('document_id', Integer(), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('version', Integer(), primary_key=True, nullable=False, server_default=text("'0'")),
    Column('flag_abs_present', Integer(), nullable=False, server_default=text("'0'")),
    Column('abs_size', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('abs_md5sum', BINARY(16), index=True),
    Column('flag_src_present', Integer(), nullable=False, server_default=text("'0'")),
    Column('src_size', Integer(), nullable=False, index=True, server_default=text("'0'")),
    Column('src_md5sum', BINARY(16), index=True),
    ForeignKeyConstraint(['document_id', 'version'], ['arXiv_versions.document_id', 'arXiv_versions.version'])
)


arXiv_endorsements_audit = Table(
    'arXiv_endorsements_audit', metadata,
    Column('endorsement_id', ForeignKey('arXiv_endorsements.endorsement_id'), primary_key=True, server_default=text("'0'")),
    Column('session_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('remote_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('flag_knows_personally', Integer(), nullable=False, server_default=text("'0'")),
    Column('flag_seen_paper', Integer(), nullable=False, server_default=text("'0'")),
    Column('comment', Text)
)


arXiv_ownership_requests_audit = Table(
    'arXiv_ownership_requests_audit', metadata,
    Column('request_id', ForeignKey('arXiv_ownership_requests.request_id'), primary_key=True, server_default=text("'0'")),
    Column('session_id', Integer(), nullable=False, server_default=text("'0'")),
    Column('remote_addr', String(16), nullable=False, server_default=text("''")),
    Column('remote_host', String(255), nullable=False, server_default=text("''")),
    Column('tracking_cookie', String(255), nullable=False, server_default=text("''")),
    Column('date', Integer(), nullable=False, server_default=text("'0'"))
)


arXiv_submission_mod_hold = Table(
    'arXiv_submission_mod_hold', metadata,
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE'), primary_key=True),
    Column('user_id', ForeignKey('tapir_users.user_id', ondelete='CASCADE'), primary_key=True, nullable=False),
    Column('reason', String(30)),
    Column('type', String(30)),
    Column('comment_id', ForeignKey('arXiv_admin_log.id'), nullable=False),
)


arXiv_submission_hold_reason = Table(
    'arXiv_submission_hold_reason', metadata,
    Column('reason_id', Integer(), primary_key=True, nullable=False, autoincrement=True),
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE'),nullable=False),
    Column('user_id', ForeignKey('tapir_users.user_id', ondelete='CASCADE'), nullable=False),
    Column('reason', String(30)),
    Column('type', String(30)),
    Column('comment_id', ForeignKey('arXiv_admin_log.id')),
)


arXiv_submission_flag = Table(
    'arXiv_submission_flag', metadata,
    Column('flag_id', Integer(), primary_key=True, nullable=False, autoincrement=True),
    Column('user_id', ForeignKey('tapir_users.user_id', ondelete='CASCADE'), nullable=False, server_default=text("'0'")),
    Column('submission_id', ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE'), nullable=False),
    Column('flag', Integer(), server_default=text("'0'")),
    Column('updated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")),
    UniqueConstraint('submission_id', 'user_id', name='uniq_one_flag_per_mod')
)

submission_mod_flag_create="""
CREATE TABLE `arXiv_submission_mod_flag` (
  `mod_flag_id` int(11) NOT NULL AUTO_INCREMENT,
  `flag` tinyint not null default '0',
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `submission_id` int(11) NOT NULL,
  `user_id` int(4) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`mod_flag_id`),
  KEY `submission_id` (`submission_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `arXiv_submission_mod_flag_ibfk_1` FOREIGN KEY (`submission_id`) REFERENCES `arXiv_submissions` (`submission_id`) ON DELETE CASCADE,
  CONSTRAINT `arXiv_submission_mod_flag_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `tapir_users` (`user_id`),
  UNIQUE( submission_id, user_id )
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""

# Allow for null because some of the inactive cats don't need relations.
alter_cat_def="""
ALTER TABLE arXiv_category_def
  ADD COLUMN archive String(16),
  ADD COLUMN subject_class String(16),
  ADD CONSTRAINT FOREIGN KEY archive_subject_class_idx (archive, subject_class) REFERENCES arXiv_categories
"""

submission_mod_hold_reasons_create="""
CREATE TABLE `arXiv_submission_hold_reason` (
    reason_id Integer  NULL AUTO_INCREMENT,
    submission_id Integer() NOT NULL,
    `user_id` int(4) unsigned NOT NULL DEFAULT '0',
    reason String(30),
    type String(30),
    comment_id Integer(),
    PRIMARY KEY (reason_id),
    FOREIGN KEY(submission_id) REFERENCES arXiv_submissions (submission_id) ON DELETE CASCADE,
    FOREIGN KEY (`user_id`) REFERENCES `tapir_users` (`user_id`) ON DELETE CASCADE,
    FOREIGN KEY(comment_id) REFERENCES `arXiv_admin_log` (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""

'''
a = await db.fetch_all( sql.select([
    t.arXiv_submissions.c.submission_id,
    t.arXiv_submissions.c.status,
    t.arXiv_submission_category.c.category,
    t.arXiv_submission_category.c.is_primary]
).select_from( t.tapir_users.join(
                            t.arXiv_moderators.join(
                                t.arXiv_categories.join(
                                    t.arXiv_category_def.join(
                                        t.arXiv_submission_category.join( t.arXiv_submissions )
                                    )
                                )
                            ),
                            t.tapir_users.c.user_id == t.arXiv_moderators.c.user_id) )
                        .where( sql.and_(
                            t.tapir_users.c.user_id == 55594,
                            t.arXiv_submissions.c.status in [2, 1]
                        ))
                    )
'''
