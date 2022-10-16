"""AppConfig for radicale."""

from django.apps import AppConfig


class RadicaleConfig(AppConfig):
    """App configuration."""

    name = "kalabash_radicale"
    verbose_name = "Kalabash Radicale frontend"

    def ready(self):
        from . import handlers
