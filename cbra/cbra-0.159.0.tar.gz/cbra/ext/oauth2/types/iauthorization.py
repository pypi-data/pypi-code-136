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

from .refreshtoken import RefreshToken


class IAuthorization:
    __module__: str = 'cbra.ext.oauth2.types'

    def authorize(
        self,
        scope: str,
        now: datetime.datetime,
        expires: datetime.datetime | None = None
    ) -> None:
        """Authorizes the given scope `scope` for the Resource Owner
        and Client.
        """
        raise NotImplementedError

    def allows_refresh(self) -> bool:
        """Return a boolean indicating if the :class:`Authorization` allows
        the issue of a refresh token.
        """
        raise NotImplementedError

    def create_refresh_token(
        self,
        scope: Iterable[str]
    ) -> RefreshToken:
        """Create a *new* refresh token for the authorization."""
        raise NotImplementedError

    def enable_refresh(self) -> None:
        """Enables the issue of refresh tokens."""
        raise NotImplementedError

    def expire_scope(self, now: datetime.datetime | None = None) -> None:
        """Expire authorized scopes that have an expiration date."""
        raise NotImplementedError

    def get_active_scope(self, now: datetime.datetime | None = None) -> set[str]:
        """Return the set of scopes that are currently active."""
        raise NotImplementedError

    def is_authorized(self, scope: str | set[str]) -> bool:
        """Return a boolean indicating if authorization was granted previously
        to the given scope.
        """
        raise NotImplementedError