from django.apps import AppConfig


class BaasObjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nosql_objects'

    def ready(self):
        # Bootstrap signals
        from . import signals
