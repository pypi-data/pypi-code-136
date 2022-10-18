
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

PostgreSQL can throw a LOT of exceptions.

When interacting with the database from our own code, we would usually like to catch ANY
of these PostgreSQL exceptions that the asyncpg library may throw, but we don't want to Except
a bare Exception.  To facilitate this, we create the DB_EXCEPTIONS tuple here, which contains
all of these exceptions.  When needed, just import DB_EXCEPTIONS from this module and use it
in the try/except block.
"""

from asyncpg import exceptions


def _get_db_exceptions():
    """
    The try/except block will only capture exceptions that derive from Python's BaseException class.
    Some classes from asyncpg.exceptions DO NOT derive from BaseException, so we need to weed these
    out here.
    """
    asyncpg_base_exceptions = []

    for ex_name in exceptions.__all__:
        ex_class = getattr(exceptions, ex_name)
        if issubclass(ex_class, BaseException):
            asyncpg_base_exceptions.append(ex_class)

    return tuple(asyncpg_base_exceptions)


DB_EXCEPTIONS = _get_db_exceptions()
