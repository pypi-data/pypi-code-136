
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
from typing import Optional, Type

import bcrypt
from fastapi import HTTPException, status
import jwt
from passlib.context import CryptContext
from pydantic import ValidationError
from starlette.datastructures import Secret

from trove_fm.app.config import ACCESS_TOKEN_EXPIRE_MINUTES, BASE_URL, JWT_ALGORITHM, JWT_AUDIENCE, SECRET_KEY
from trove_fm.app.models.token import JWTMeta, JWTCreds, JWTPayload
from trove_fm.app.models.person import PersonBase, PersonPasswordUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthException(BaseException):
    """
    Custom auth exception that can be modified later on.
    """
    pass


class AuthService:
    def create_salt_and_hashed_password(self, *, plaintext_password: str) -> PersonPasswordUpdate:
        salt = self.generate_salt()
        hashed_password = self.hash_password(password=plaintext_password, salt=salt)

        return PersonPasswordUpdate(salt=salt, password=hashed_password)

    def generate_salt(self) -> str:
        return bcrypt.gensalt().decode()

    def hash_password(self, *, password: str, salt: str) -> str:
        return pwd_context.hash(password + salt)

    def verify_password(self, *, password: str, salt: str, hashed_pw: str) -> bool:
        return pwd_context.verify(password + salt, hashed_pw)

    def create_access_token_for_person(
        self,
        *,
        person: Type[PersonBase],
        secret_key: Secret = SECRET_KEY,
        issuer: str = BASE_URL,
        audience: str = JWT_AUDIENCE,
        expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES,
    ) -> str:
        if not person or not isinstance(person, PersonBase):
            return None
        jwt_meta = JWTMeta(
            iss=issuer,
            aud=audience,
            iat=datetime.timestamp(datetime.utcnow()),
            exp=datetime.timestamp(datetime.utcnow() + timedelta(minutes=expires_in)),
        )
        jwt_creds = JWTCreds(sub=person.username, person_id=person.id)
        token_payload = JWTPayload(
            **jwt_meta.dict(),
            **jwt_creds.dict(),
        )
        access_token = jwt.encode(token_payload.dict(), str(secret_key), algorithm=JWT_ALGORITHM)
        return access_token

    def get_person_id_from_token(self, *, token: str, secret_key: Secret) -> Optional[int]:
        try:
            decoded_token = jwt.decode(
                token, str(secret_key), audience=JWT_AUDIENCE, algorithms=[JWT_ALGORITHM]
            )
            payload = JWTPayload(**decoded_token)
        except (jwt.PyJWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate token credentials.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return payload.person_id
