"""AppConfig for relaydomains."""

from django.apps import AppConfig


class RelayDomainsConfig(AppConfig):
    """App configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "kalabash.relaydomains"
    verbose_name = "Kalabash relay domains"

    def ready(self):
        from . import handlers  # NOQA:F401
        from . import transport  # NOQA:F401
