"""Extension definition."""

from django.utils.translation import ugettext as _, ugettext_lazy

from kalabash.core.extensions import KalmonakExtension, exts_pool
from kalabash.parameters import tools as param_tools

from . import __version__
from . import forms


class ImapMigration(KalmonakExtension):
    """The ImapMigration extension class."""

    name = "kalabash_imap_migration"
    label = ugettext_lazy("IMAP migration using OfflineIMAP")
    version = __version__
    description = ugettext_lazy(
        "Migrate existing mailboxes using IMAP and OfflineIMAP"
    )

    def load(self):
        """Load extension."""
        param_tools.registry.add(
            "global", forms.ParametersForm, _("IMAP migration"))

exts_pool.register_extension(ImapMigration)
