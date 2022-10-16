"""AppConfig for relaydomains."""

from django.apps import AppConfig


class AdminRelayDomainsConfig(AppConfig):

    """App configuration."""

    name = "kalabash_admin_relaydomains"
    verbose_name = "Kalabash relay domains"

    def ready(self):
        from . import handlers
