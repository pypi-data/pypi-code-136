"""AppConfig for policyd."""

from django.apps import AppConfig


class PolicydConfig(AppConfig):
    """App configuration."""

    name = "kalabash.policyd"
    verbose_name = "Kalabash policy daemon"

    def ready(self):
        from . import handlers  # NOQA:F401
