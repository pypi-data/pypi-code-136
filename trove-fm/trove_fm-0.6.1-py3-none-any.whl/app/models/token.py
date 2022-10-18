
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

from enum import Enum
from typing import Optional

from pydantic import EmailStr, root_validator

from trove_fm.app.models.core import CoreModel


class TokenLocation(str, Enum):
    cookie = "cookie"        # set in http-only cookie
    json = "json"  # json response


class JWTMeta(CoreModel):
    iss: str
    aud: str
    iat: float
    exp: float


class JWTCreds(CoreModel):
    """How we'll identify users"""
    sub: EmailStr
    person_id: int


class JWTPayload(JWTMeta, JWTCreds):
    """
    JWT Payload right before it's encoded - combine meta and username
    """
    pass


class AccessToken(CoreModel):
    access_token: Optional[str] = None
    token_type: str
    token_location: TokenLocation

    @root_validator(pre=True)
    def check_token(cls, values) -> str:
        access_token, token_location = values.get("access_token"), values.get("token_location")

        if token_location == TokenLocation.cookie.value and access_token is not None:
            raise TypeError(f"Cannot set access_token value when token_location is {TokenLocation.cookie.value}")
        if token_location == TokenLocation.json.value and access_token is None:
            raise TypeError(f"Must set access_token value when token_location is {TokenLocation.json.value}.")
        return values
