# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import secrets
from typing import Any
from typing import Iterable

import pydantic
from ckms.core import Keychain
from ckms.jose import PayloadCodec
from ckms.types import InvalidSignature
from ckms.utils import b64decode

from .iclient import IClient
from .irefreshtoken import IRefreshToken
from .isubject import ISubject


KEY_LENGTH: int = 64


class RefreshToken(pydantic.BaseModel, IRefreshToken):
    authorization_id: int
    id: int | None = None
    sub: int | str
    client_id: str
    secret: str
    created: datetime.datetime
    exchanged: datetime.datetime
    expires: datetime.datetime | None = None
    generation: int = 0
    scope: list[str]

    @pydantic.root_validator(pre=True)
    def preprocess(
        cls,
        values: dict[str, Any]
    ) -> dict[str, Any]:
        values.setdefault('secret', secrets.token_urlsafe(KEY_LENGTH))
        return values

    @classmethod
    def new(
        cls,
        authorization_id: int,
        client_id: int | str,
        sub: int | str,
        scope: list[str] | set[str]
    ) -> 'RefreshToken':
        now = datetime.datetime.utcnow()
        return cls.parse_obj({
            'authorization_id': authorization_id,
            'client_id': client_id,
            'sub': sub,
            'secret': secrets.token_urlsafe(KEY_LENGTH),
            'created': now,
            'exchanged': now,
            'scope': scope
        })

    def allows_scope(self, scope: str | Iterable[str] | None) -> bool:
        """Return a boolean indicating if the Refresh Token allows the given
        scope.
        """
        scope = scope or self.scope
        if isinstance(scope, str):
            scope = {scope}
        return set(scope) <= set(self.scope)

    async def get_codec(self) -> PayloadCodec:
        keychain = Keychain()
        keychain.configure({
            'refresh_token': {
                'provider': 'local',
                'kty': 'oct',
                'alg': 'HS384',
                'use': 'sig',
                'key': {'cek': b64decode(self.secret)}   
            }
        })
        return PayloadCodec(
            verifier=await keychain,
            signing_keys=[keychain.get('refresh_token')]
        )

    async def generate(
        self,
        client: IClient,
        subject: ISubject,
        rotate: bool = False
    ) -> str | None:
        assert self.authorization_id is not None # nosec
        assert self.id is not None # nosec
        self.exchanged = datetime.datetime.utcnow()
        self.generation += 1
        if rotate:
            self.secret = secrets.token_urlsafe(KEY_LENGTH)
        return await client.create_refresh_token(
            codec=await self.get_codec(),
            subject=subject,
            authorization_id=self.authorization_id,
            token_id=self.id,
            expires=self.expires
        )

    async def verify(self, token: str) -> bool:
        """Return a boolean indicating if the given refresh token has a valid
        signature.
        """
        codec = await self.get_codec()
        try:
            await codec.decode(token, accept={"rt+jwt"})
            return True
        except InvalidSignature:
            return False