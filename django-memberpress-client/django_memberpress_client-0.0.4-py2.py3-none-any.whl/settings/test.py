import os
from dotenv import load_dotenv

load_dotenv()

# your local dev & test settings go here
# -----------------------------------------------------------------------------
MEMBERPRESS_API_KEY = os.getenv("MEMBERPRESS_API_KEY")
MEMBERPRESS_API_BASE_URL = "https://stepwisemath.ai/"

# common local dev & test settings
# -----------------------------------------------------------------------------
MEMBERPRESS_CACHE_EXPIRATION = 300
MEMBERPRESS_API_KEY_NAME = "MEMBERPRESS-API-KEY"
MEMBERPRESS_SENSITIVE_KEYS = [
    "password",
    "token",
    "client_id",
    "client_secret",
    "Authorization",
    "secret",
]

# generic required Django settings
# -----------------------------------------------------------------------------
DEBUG = True
LOGGING_CONFIG = None
LOGGING = None
FORCE_SCRIPT_NAME = None
INSTALLED_APPS = []
ALLOWED_HOSTS = []
EMAIL_BACKEND = None
USE_I18N = False
CACHES = CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": ".//django_cache",
    }
}
