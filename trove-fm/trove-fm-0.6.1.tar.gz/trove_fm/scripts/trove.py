
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


import asyncio
import os

from loguru import logger

from trove_fm.app.db.tasks import close_db_connection, connect_to_db
from trove_fm.app.db.repositories.person import PersonRepository
from trove_fm.app.main import app
from trove_fm.app.models.person import AppRole, PersonCreate


username = os.getenv("TROVE_ADMIN_USER")
username = input('Please enter the email address that you will use for the admin user: ') if not username else username

password = os.getenv("TROVE_ADMIN_PASSWORD")
password = input('Please enter the password that you will use for the admin user: ') if not password else password


admin_user = PersonCreate(
    app_role=AppRole.ADMIN,
    name_first="Admin",
    email_label='admin',
    username=username,
    password=password
)


async def main():
    await connect_to_db(app)
    db = app.state._db
    person_repo = PersonRepository(db)
    new_admin = await person_repo.create_new_person(admin_user)
    confirmation = f"Admin account created for {new_admin.username}"
    await close_db_connection(app)
    logger.info(confirmation)


asyncio.run(main())
