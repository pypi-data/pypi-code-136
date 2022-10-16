"""AppConfig for PDF credentials."""

from django.apps import AppConfig


class PDFCredentialsConfig(AppConfig):
    """App configuration."""

    name = "kalabash_pdfcredentials"
    verbose_name = "PDF credentials for Kalabash"

    def ready(self):
        from . import handlers
