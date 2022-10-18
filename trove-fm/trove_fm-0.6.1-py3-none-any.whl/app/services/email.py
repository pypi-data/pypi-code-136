
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

from datetime import datetime, timedelta

from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from loguru import logger
from pydantic import HttpUrl

from trove_fm.app.config import (
    MAIL_USERNAME,
    MAIL_PASSWORD,
    MAIL_FROM,
    MAIL_PORT,
    MAIL_SERVER,
    MAIL_FROM_NAME,
    MAIL_TLS,
    MAIL_SSL,
    MAIL_USE_CREDENTIALS,
    MAIL_VALIDATE_CERTS,
    MAIL_LINK_EXPIRES
)
from trove_fm.app.models.person import PersonInDB, PersonUnverified


class EmailService(object):
    """docstring for EmailService"""

    def __init__(self):
        self.mail_config = ConnectionConfig(
            MAIL_USERNAME=MAIL_USERNAME,
            MAIL_PASSWORD=MAIL_PASSWORD,
            MAIL_FROM=MAIL_FROM,
            MAIL_PORT=MAIL_PORT,
            MAIL_SERVER=MAIL_SERVER,
            MAIL_FROM_NAME=MAIL_FROM_NAME,
            MAIL_TLS=MAIL_TLS,
            MAIL_SSL=MAIL_SSL,
            USE_CREDENTIALS=MAIL_USE_CREDENTIALS,
            VALIDATE_CERTS=MAIL_VALIDATE_CERTS
        )

        self.fm = FastMail(self.mail_config)

    async def send_verification(
        self, person: PersonInDB, verification_url: HttpUrl, background_tasks: BackgroundTasks
    ) -> PersonUnverified:
        body = f"""
        <p>
        Hello {person.name_first if person.name_first else "There"}!
        </p>
        <p>
        Please click the link below to verfiy your new account at TroveFM:
        </p>
        <p><a href={verification_url}>{verification_url}</a></p>
        """

        message = MessageSchema(
            subject="Account Verification",
            recipients=[person.username],
            html=body,
        )

        background_tasks.add_task(self.fm.send_message, message)
        logger.info(f"Verification email for {person.username} added to background_tasks")

        link_expiration = datetime.now() + timedelta(seconds=MAIL_LINK_EXPIRES)

        return link_expiration
