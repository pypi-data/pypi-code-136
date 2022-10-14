# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Iterable

import pydantic

from .authorizedscope import AuthorizedScope
from .types import AccessType
from .types import AuthorizationIdentifier
from .types import IAuthorization
from .types import RefreshToken
from .types import TokenException


IGNORED_SCOPES: set[str] = {"openid"}


class Authorization(pydantic.BaseModel, IAuthorization):
    """Represents to permission given to a Client by a Resource Owner."""
    id: int | None = pydantic.Field(
        default=None
    )

    version: int = pydantic.Field(
        default=0
    )

    client_id: str = pydantic.Field(
        default=...
    )

    sub: int | str = pydantic.Field(
        default=...
    )

    access_type: AccessType = pydantic.Field(
        default=AccessType.online
    )

    created: datetime.datetime = pydantic.Field(
        default_factory=datetime.datetime.utcnow
    )

    scope: dict[str, AuthorizedScope] = pydantic.Field(
        default={}
    )

    @classmethod
    def fromkey(
        cls,
        key: AuthorizationIdentifier
    ) -> 'Authorization':
        """Create a new :class:`Authorization` using the given key."""
        return cls(
            client_id=key.client_id,
            sub=key.sub
        )

    @property
    def key(self) -> AuthorizationIdentifier:
        return AuthorizationIdentifier(
            client_id=self.client_id,
            sub=self.sub
        )

    def allows_refresh(self) -> bool:
        """Return a boolean indicating if the :class:`Authorization` allows
        the issue of a refresh token.
        """
        return self.access_type == AccessType.offline

    def authorize(
        self,
        scope: str,
        now: datetime.datetime,
        expires: datetime.datetime | None = None
    ) -> None:
        """Authorizes the given scope `scope` for the Resource Owner
        and Client.
        """
        if self.is_authorized(scope) or scope in IGNORED_SCOPES:
            return
        self.scope[scope] = AuthorizedScope(
            name=scope,
            authorized=now,
            expires=expires
        )

    def create_refresh_token(
        self,
        scope: Iterable[str],
        include_granted: bool = False
    ) -> RefreshToken:
        """Create a *new* refresh token for the authorization."""
        assert self.id is not None # nosec
        if not self.allows_refresh():
            raise TokenException(
                code='invalid_grant',
                description=(
                    "The issue of refresh tokens is disabled by the Client or "
                    "was not authorized by the Resource Owner."
                )
            )
        if not self.is_authorized(scope):
            raise TokenException(
                code='invalid_scope',
                description=(
                    "The requested scope exceeds the scope that was granted by "
                    "the Resource Owner."
                )
            )
        scope = set(scope)
        if include_granted:
            scope |= self.get_active_scope()
        return RefreshToken.new(
            authorization_id=self.id,
            client_id=self.client_id,
            sub=self.sub,
            scope=list(sorted(scope))
        )

    def enable_refresh(self) -> None:
        """Enables the issue of refresh tokens."""
        self.access_type = AccessType.offline

    def expire_scope(self, now: datetime.datetime | None = None) -> None:
        """Expire authorized scopes that have an expiration date."""
        for scope in list(self.scope.values()):
            if not scope.is_expired(now):
                continue
            self.scope.pop(scope.name)

    def get_active_scope(self, now: datetime.datetime | None = None) -> set[str]:
        """Return the set of scopes that are currently active."""
        now = now or datetime.datetime.utcnow()
        return {
            scope.name
            for scope in self.scope.values()
            if not scope.is_expired()
        } | {"openid"}

    def is_authorized(self, scope: str | Iterable[str]) -> bool:
        """Return a boolean indicating if authorization was granted previously
        to the given scope.
        """
        if isinstance(scope, str):
            scope = {scope}
        return set(scope) <= self.get_active_scope()