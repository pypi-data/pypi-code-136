"""Core app config"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Core config"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
