# bootstrap the test environment
from memberpress_client.settings import test as test_settings
from django.conf import settings

settings.configure(default_settings=test_settings)
