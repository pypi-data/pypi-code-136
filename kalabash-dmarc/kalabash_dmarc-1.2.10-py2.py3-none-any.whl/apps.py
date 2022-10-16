"""AppConfig for dmarc."""

from django.apps import AppConfig


class DmarcConfig(AppConfig):

    """App configuration."""

    name = "kalabash_dmarc"
    verbose_name = "Kalabash DMARC tools"

    def ready(self):
        from . import handlers
