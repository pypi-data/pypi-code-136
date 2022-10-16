from django.test import SimpleTestCase, override_settings
from django.apps import apps


@override_settings(INSTALLED_APPS=['drf_versioned_schemas.apps.DrfVersionedModelsConfig'])
class AppConfigTestCase(SimpleTestCase):
    def test_install_app(self):
        self.assertTrue(apps.is_installed('drf_versioned_schemas'))
        app_config = apps.get_app_config('drf_versioned_schemas')
        self.assertEqual('drf_versioned_schemas', app_config.name)
