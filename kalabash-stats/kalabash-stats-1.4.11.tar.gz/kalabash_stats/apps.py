"""AppConfig for stats."""

from django.apps import AppConfig


class StatsConfig(AppConfig):
    """App configuration."""

    name = "kalabash_stats"
    verbose_name = "Kalabash graphical statistics"

    def ready(self):
        from . import handlers
