from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Protocol

from infiniaml_idp_client._common.constants import IDP_URL
from infiniaml_idp_client._common.token import Token

from ._http_client_mixin import HttpClientMixin

__all__ = "AsyncTokenCredential", "TokenGetter", "AccessKeyCredentials"


class AsyncTokenCredential(Protocol):
    async def get_token(self) -> str:
        ...


class TokenGetter(HttpClientMixin, ABC):
    def __init__(
        self,
        token_url: str,
    ) -> None:
        self._token_url = token_url
        self._access_token: Optional[Token] = None

    @abstractmethod
    def _auth_form(self) -> Dict[str, Any]:
        raise NotImplementedError

    def _get_access_token_if_not_expired(self) -> Optional[Token]:
        if self._access_token is not None and not self._access_token.is_expired:
            return self._access_token
        return None

    async def get_token(self) -> str:
        """Get IDP access token"""

        if access_token := self._get_access_token_if_not_expired():
            return access_token.value
        r = await self._http_client.post(self._token_url, data=self._auth_form())
        r.raise_for_status()
        json = r.json()
        self._access_token = Token(
            value=json["access_token"],
            expires_in=json["expires_in"],
        )
        return self._access_token.value


class AccessKeyCredentials(TokenGetter):
    def __init__(self, access_key_id: str, access_key_secret: str, *, idp_url: str = IDP_URL) -> None:
        self._access_key_id = access_key_id
        self._access_key_secret = access_key_secret
        super().__init__(f"{idp_url}/token")

    def _auth_form(self):
        return {
            "grant_type": "client_credentials",
            "client_id": self._access_key_id,
            "client_secret": self._access_key_secret,
        }
