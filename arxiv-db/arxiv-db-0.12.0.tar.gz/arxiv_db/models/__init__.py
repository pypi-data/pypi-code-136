"""arXiv database SQLAlchemy models.

## Process to create:
This was generated with sqlacodegen on 2022-09-29 with the declarative
generator against a copy of the production database.

Some of the tables are represented with sqlalchemy tables since the
lack primary keys.

The class names were changed to remove the 'ArXiv' prefix.

Moved tables to associative_tables.py

Split out classes to individual files.

Added some needed imports.
"""

import importlib
import sys

from .admin_log import AdminLog
from .admin_metadata import AdminMetadata
from .archive_category import ArchiveCategory
from .archive_def import ArchiveDef
from .archive_group import ArchiveGroup
from .archives import Archives
from .author_ids import AuthorIds
from .aws_config import AwsConfig
from .aws_files import AwsFiles
from .bib_feeds import BibFeeds
from .bib_updates import BibUpdates
from .bogus_countries import BogusCountries
from .categories import Categories
from .category_def import CategoryDef
from .control_holds import ControlHolds
from .cross_control import CrossControl
from .datacite_dois import DataciteDois
from .dbix_class_schema_versions import DbixClassSchemaVersions
from .dblp_authors import DblpAuthors
from .dblp_document_authors import DblpDocumentAuthors
from .dblp import Dblp
from .demographics import Demographics
from .document_category import DocumentCategory
from .documents import Documents
from .endorsement_domains import EndorsementDomains
from .endorsement_requests_audit import EndorsementRequestsAudit
from .endorsement_requests import EndorsementRequests
from .endorsements_audit import EndorsementsAudit
from .endorsements import Endorsements
from .freeze_log import FreezeLog
from .group_def import GroupDef
from .groups import Groups
from .jref_control import JrefControl
from .licenses import Licenses
from .log_positions import LogPositions
from .metadata import Metadata
from .mirror_list import MirrorList
from .moderator_api_key import ModeratorApiKey
from .monitor_klog import MonitorKlog
from .monitor_mailq import MonitorMailq
from .monitor_mailsent import MonitorMailsent
from .next_mail import NextMail
from .orcid_config import OrcidConfig
from .orcid_ids import OrcidIds
from .ownership_requests_audit import OwnershipRequestsAudit
from .ownership_requests import OwnershipRequests
from .paper_pw import PaperPw
from .paper_sessions import PaperSessions
from .pilot_datasets import PilotDatasets
from .pilot_files import PilotFiles
from .publish_log import PublishLog
from .questionable_categories import QuestionableCategories
from .queue_view import QueueView
from .reject_session_usernames import RejectSessionUsernames
from .sciencewise_pings import SciencewisePings
from .sessions import Sessions
from .show_email_requests import ShowEmailRequests
from .state import State
from .stats_monthly_downloads import StatsMonthlyDownloads
from .stats_monthly_submissions import StatsMonthlySubmissions
from .submission_abs_classifier_data import SubmissionAbsClassifierData
from .submission_agreements import SubmissionAgreements
from .submission_category_proposal import SubmissionCategoryProposal
from .submission_category import SubmissionCategory
from .submission_classifier_data import SubmissionClassifierData
from .submission_control import SubmissionControl
from .submission_flag import SubmissionFlag
from .submission_hold_reason import SubmissionHoldReason
from .submission_near_duplicates import SubmissionNearDuplicates
from .submission_qa_reports import SubmissionQaReports
from .submissions import Submissions
from .submission_view_flag import SubmissionViewFlag
from .submitter_flags import SubmitterFlags
from .Subscription_UniversalInstitutionContact import SubscriptionUniversalInstitutionContact
from .Subscription_UniversalInstitutionIP import SubscriptionUniversalInstitutionIP
from .Subscription_UniversalInstitution import SubscriptionUniversalInstitution
from .suspect_emails import SuspectEmails
from .suspicious_names import SuspiciousNames
from .sword_licenses import SwordLicenses
from .tapir_address import TapirAddress
from .tapir_admin_audit import TapirAdminAudit
from .tapir_countries import TapirCountries
from .tapir_demographics import TapirDemographics
from .tapir_email_change_tokens import TapirEmailChangeTokens
from .tapir_email_headers import TapirEmailHeaders
from .tapir_email_log import TapirEmailLog
from .tapir_email_mailings import TapirEmailMailings
from .tapir_email_templates import TapirEmailTemplates
from .tapir_email_tokens import TapirEmailTokens
from .tapir_integer_variables import TapirIntegerVariables
from .tapir_nicknames_audit import TapirNicknamesAudit
from .tapir_nicknames import TapirNicknames
from .tapir_permanent_tokens import TapirPermanentTokens
from .tapir_phone import TapirPhone
from .tapir_policy_classes import TapirPolicyClasses
from .tapir_presessions import TapirPresessions
from .tapir_recovery_tokens import TapirRecoveryTokens
from .tapir_recovery_tokens_used import TapirRecoveryTokensUsed
from .tapir_sessions_audit import TapirSessionsAudit
from .tapir_sessions import TapirSessions
from .tapir_strings import TapirStrings
from .tapir_string_variables import TapirStringVariables
from .tapir_users_hot import TapirUsersHot
from .tapir_users_password import TapirUsersPassword
from .tapir_users import TapirUsers
from .titles import Titles
from .top_papers import TopPapers
from .trackback_pings import TrackbackPings
from .trackback_sites import TrackbackSites
from .tracking import Tracking
from .versions_checksum import VersionsChecksum
from .versions import Versions
from .paper_owners import PaperOwners


def add_all_models_to_sqlalchemy():
    """Loads all modules in this pacakge.

    For SQLAlchemy ORM to work the model definitions need to be
    defined on the Base. This does that."""

    this_pkg = sys.modules[__name__]
    print(f"This is name {__name__} and pkg {this_pkg}")
    for mod in this_pkg.__loader__.get_resource_reader().contents():
        importlib.import_module(f'arxiv_db.models.{mod.removesuffix(".py")}')
