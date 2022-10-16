from django.apps import AppConfig


class LdapsyncConfig(AppConfig):
    name = 'kalabash.ldapsync'

    def ready(self):
        from . import handlers  # noqa
