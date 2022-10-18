
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


import os

from databases import Database
from fastapi import FastAPI
from loguru import logger

from trove_fm.app.config import DATABASE_URL


async def connect_to_db(app: FastAPI) -> None:
    DB_URL = f"{DATABASE_URL}_test" if os.environ.get("TESTING") else DATABASE_URL
    database = Database(DB_URL, min_size=2, max_size=10)  # these can be configured in config as well
    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warning("---------- DB CONNECTION ERROR ----------")
        logger.warning(e)
        logger.warning("---------- DB CONNECTION ERROR ----------")


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warning("---------- DB DISCONNECT ERROR ----------")
        logger.warning(e)
        logger.warning("---------- DB DISCONNECT ERROR ----------")
