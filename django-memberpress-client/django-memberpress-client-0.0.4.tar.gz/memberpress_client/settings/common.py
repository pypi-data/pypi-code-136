"""
Common Pluggable Django App settings

Handling of environment variables, see: https://django-environ.readthedocs.io/en/latest/
to convert .env to yml see: https://django-environ.readthedocs.io/en/latest/tips.html#docker-style-file-based-variables
"""
from path import Path as path
import environ
import os

# path to this file.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


APP_ROOT = path(__file__).abspath().dirname().dirname()  # /blah/blah/blah/.../stepwise_grades
REPO_ROOT = APP_ROOT.dirname()  # /blah/blah/blah/.../memberpress-digital-learning-openedx
TEMPLATES_DIR = APP_ROOT / "templates"


def plugin_settings(settings):
    """
    Injects local settings into django settings

    see: https://stackoverflow.com/questions/56129708/how-to-force-redirect-uri-to-use-https-with-python-social-app
    """

    settings.MEMBERPRESS_API_KEY_NAME = "MEMBERPRESS-API-KEY"  # noqa: F841
    settings.MEMBERPRESS_CACHE_EXPIRATION = 300  # noqa: F841
    settings.MEMBERPRESS_SENSITIVE_KEYS = [  # noqa: F841
        "password",
        "token",
        "client_id",
        "client_secret",
        "Authorization",
        "secret",
    ]

    settings.MAKO_TEMPLATE_DIRS_BASE.extend([TEMPLATES_DIR])
    settings.INSTALLED_APPS.append("django_extensions")
    settings.INSTALLED_APPS.append("django-environ")
