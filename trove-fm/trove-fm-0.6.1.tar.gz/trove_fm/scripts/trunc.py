#!/usr/bin/env python

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

# from psycopg2 import DatabaseError
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from trove_fm.app.config import DATABASE_URL

engine = create_engine(str(DATABASE_URL), isolation_level="AUTOCOMMIT")

target_tables = ['person', 'email_address']

# delete all table data (but keep tables)
with engine.connect() as con:
    for table in target_tables:
        statement = text(f"""DELETE FROM {table};""")
        con.execute(statement)
