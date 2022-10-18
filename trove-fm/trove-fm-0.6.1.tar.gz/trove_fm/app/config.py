
"""
TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""


from importlib.metadata import version, PackageNotFoundError

from databases import DatabaseURL
from pydantic import EmailStr
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

PROJECT_NAME = "TroveFM"
try:
    VERSION = version("trove-fm")
except PackageNotFoundError:
    # package is not installed
    VERSION = "0.0.1"

BASE_URL = config("BASE_URL", cast=str)
API_PREFIX = "/api"

SECRET_KEY = config("SECRET_KEY", cast=Secret)
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int)
JWT_ALGORITHM = config("JWT_ALGORITHM", cast=str)
JWT_AUDIENCE = config("JWT_AUDIENCE", cast=str)
JWT_TOKEN_PREFIX = config("JWT_TOKEN_PREFIX", cast=str)

BROWSER_LIST = config("BROWSER_LIST", cast=str)

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)

DATABASE_URL = config(
    "DATABASE_URL",
    cast=DatabaseURL,
    default=(
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
)

MAIL_USERNAME = config("MAIL_USERNAME", cast=str)
MAIL_PASSWORD = config("MAIL_PASSWORD", cast=str)
MAIL_FROM = config("MAIL_FROM", cast=EmailStr)
MAIL_PORT = config("MAIL_PORT", cast=int)
MAIL_SERVER = config("MAIL_SERVER", cast=str)
MAIL_FROM_NAME = config("MAIL_FROM_NAME", cast=str)
MAIL_TLS = config("MAIL_TLS", cast=bool)
MAIL_SSL = config("MAIL_SSL", cast=bool)
MAIL_USE_CREDENTIALS = config("MAIL_USE_CREDENTIALS", cast=bool)
MAIL_VALIDATE_CERTS = config("MAIL_VALIDATE_CERTS", cast=bool)
MAIL_LINK_EXPIRES = config("MAIL_LINK_EXPIRES", cast=int)

CELERY_BROKER_URL = config("CELERY_BROKER_URL", cast=str)
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", cast=str)
