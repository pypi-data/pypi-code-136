"""AppConfig for admin."""

from django.apps import AppConfig


class AdminConfig(AppConfig):

    """App configuration."""

    name = "kalabash_admin"
    verbose_name = "Kalabash admin console"

    def ready(self):
        from . import handlers
