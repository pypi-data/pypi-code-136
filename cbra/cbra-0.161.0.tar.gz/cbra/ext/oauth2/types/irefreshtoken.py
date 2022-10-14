# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Iterable

from .iclient import IClient
from .isubject import ISubject


class IRefreshToken:
    __module__: str = 'cbra.ext.oauth2.types'

    def allows_scope(self, scope: str | Iterable[str] | None) -> bool:
        """Return a boolean indicating if the Refresh Token allows the given
        scope.
        """
        raise NotImplementedError

    async def generate(
        self,
        client: IClient,
        subject: ISubject,
        rotate: bool = False
    ) -> str | None:
        """Generate a new refresh token for the given `client`."""
        raise NotImplementedError

    async def verify(self, token: str) -> bool:
        """Return a boolean indicating if the given refresh token has a valid
        signature.
        """
        raise NotImplementedError