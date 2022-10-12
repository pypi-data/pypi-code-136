from dataclasses import dataclass
from functools import cached_property, lru_cache
from typing import cast
from urllib.parse import urljoin

from atoti_core import keyword_only_dataclass

from ._fetch_json import fetch_json
from ._http import HttpHeaders
from .auth import Auth
from .token_authentication import TokenAuthentication


@lru_cache
def _fetch_token_endpoint_url(*, issuer_url: str) -> str:
    configuration_url = urljoin(issuer_url, ".well-known/openid-configuration")
    body = fetch_json(configuration_url)
    return cast(str, body["token_endpoint"])


@keyword_only_dataclass
@dataclass(frozen=True)
class OAuth2ResourceOwnerPasswordAuthentication(Auth):
    """This :class:`atoti_query.Auth` relies on OAuth 2's `Resource Owner Password Credentials Grant <https://datatracker.ietf.org/doc/html/rfc6749#section-4.3>`__.

    See also:
        :attr:`atoti.OidcConfig.access_token_format`.
    """

    username: str
    password: str
    issuer_url: str
    client_id: str
    client_secret: str

    def __call__(self, url: str) -> HttpHeaders:
        return self._token_authentication(url)

    @cached_property
    def _token_authentication(self) -> TokenAuthentication:
        body = fetch_json(
            _fetch_token_endpoint_url(issuer_url=self.issuer_url),
            body={
                "grant_type": "password",
                "username": self.username,
                "password": self.password,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        )
        return TokenAuthentication(
            token=body["access_token"], token_type=body["token_type"]
        )
