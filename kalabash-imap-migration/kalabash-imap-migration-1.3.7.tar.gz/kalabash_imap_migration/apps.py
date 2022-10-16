"""AppConfig for IMAP migration."""

from django.apps import AppConfig


class IMAPMigrationConfig(AppConfig):
    """App configuration."""

    name = "kalabash_imap_migration"
    verbose_name = "Migration through IMAP for Kalabash"

    def ready(self):
        from . import checks  # noqa
        from . import handlers  # noqa
