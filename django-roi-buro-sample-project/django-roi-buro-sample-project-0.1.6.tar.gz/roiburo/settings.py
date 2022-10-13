"""
Settings for test project
"""

from split_settings.tools import include

include(
    "conf/api.py",
    "conf/auth.py",
    "conf/boilerplate.py",
    "conf/db.py",
    "conf/environ.py",
    "conf/http.py",
    "conf/i18n.py",
    "conf/installed_apps.py",
    "conf/log.py",
    "conf/media.py",
    "conf/middleware.py",
    "conf/spectacular.py",
    "conf/static.py",
    "conf/storage.py",
    "conf/templates.py",
    "conf/timezone.py",
)
