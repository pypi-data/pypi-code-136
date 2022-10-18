
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


from itsdangerous.url_safe import URLSafeTimedSerializer
from pydantic import HttpUrl
from loguru import logger
from starlette.datastructures import Secret

from trove_fm.app.config import SECRET_KEY, MAIL_LINK_EXPIRES


"""
From the `itsdangerous documentation <https://itsdangerous.palletsprojects.com/en/2.1.x/concepts/>`_ :

Signatures are secured by the secret_key. Typically one secret key is used with all signers, and the salt is
used to distinguish different contexts. Changing the secret key will invalidate existing tokens.

It should be a long random string of bytes. This value must be kept secret and should not be saved in
source code or committed to version control. If an attacker learns the secret key, they can change and
resign data to look valid. If you suspect this happened, change the secret key to invalidate existing tokens.
"""

# TODO: Implement key rotation, as described here:
# - https://itsdangerous.palletsprojects.com/en/2.1.x/concepts/#key-rotation

confirmation_token_salt = b'confirmation_token:salt'


class NewAccountVerificationService(object):
    """docstring for NewAccountVerificationService"""

    def __init__(self, secret_key: Secret = SECRET_KEY, salt: str = confirmation_token_salt):
        self.secret_key = secret_key
        self.salt = salt
        self.secure_serializer = URLSafeTimedSerializer(str(self.secret_key), self.salt)

    def get_urlsafe_timed_token(self, username):
        token = self.secure_serializer.dumps(username)

        return token

    def get_verification_url(self, username: str, base_url: HttpUrl) -> HttpUrl:
        token = self.get_urlsafe_timed_token(username)

        url = f"{base_url}{token}"

        return url

    def verify_token(self, token, expiration=MAIL_LINK_EXPIRES):
        logger.info(f"token: {token}")
        username = self.secure_serializer.loads(
            token,
            salt=self.salt,
            max_age=expiration
        )
        logger.info(f"username: {username}")

        return username
