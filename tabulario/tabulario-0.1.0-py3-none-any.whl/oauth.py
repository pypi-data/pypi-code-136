# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from dataclasses import dataclass
from typing import (
    Any,
    Dict,
    Optional,
    Set,
    Type,
    TypeVar,
)

import requests
from requests import HTTPError

TOKEN_ACCESS_TYPE = "urn:ietf:params:oauth:token-type:access_token"
TOKEN_REFRESH_TYPE = "urn:ietf:params:oauth:token-type:refresh_token"
TOKEN_ID_TYPE = "urn:ietf:params:oauth:token-type:id_token"
TOKEN_SAML1_TYPE = "urn:ietf:params:oauth:token-type:saml1"
TOKEN_SAML2_TYPE = "urn:ietf:params:oauth:token-type:saml2"
TOKEN_JWT_TYPE = "urn:ietf:params:oauth:token-type:jwt"

GRANT_TYPE = "grant_type"
SCOPE = "scope"
SUBJECT_TOKEN = "subject_token"
SUBJECT_TOKEN_TYPE = "subject_token_type"
ACTOR_TOKEN = "actor_token"
ACTOR_TOKEN_TYPE = "actor_token_type"
TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"

CATALOG_SCOPE = "catalog"

CLIENT_CREDENTIALS = "client_credentials"
CLIENT_ID = "client_id"

CLIENT_SECRET = "client_secret"


SEMICOLON = ":"


VALID_TOKEN_TYPES = {TOKEN_ACCESS_TYPE, TOKEN_REFRESH_TYPE, TOKEN_ID_TYPE, TOKEN_SAML1_TYPE, TOKEN_SAML2_TYPE, TOKEN_JWT_TYPE}


@dataclass(frozen=True)
class OAuthTokenResponse:
    access_token: str
    issued_token_type: str
    token_type: str
    expires_in: Optional[int]
    scope: Optional[str]


@dataclass(frozen=True)
class ClientOauthTokenResponse(OAuthTokenResponse):
    warehouse_id: str
    region: str


def _parse_scopes(scopes: Any) -> Set[str]:
    if scopes:
        if isinstance(scopes, str):
            return {scopes}
        else:
            # Assume that it is some kind of iterable
            return set(scopes)

    return {CATALOG_SCOPE}


def _join_scopes(scopes: Set[str]) -> str:
    return " ".join(scopes)


T = TypeVar("T")


def _do_request(url: str, payload: Dict[str, str], response_type: Type[T]) -> T:
    response = requests.post(url, data=payload)
    try:
        response.raise_for_status()
    except HTTPError as e:
        raise ValueError(f"Request failed {response.text}") from e

    return response_type(**{**{"scope": None, "expires_in": None}, **response.json()})


ENVIRONMENT_URLS = {
    "prod": "https://api.tabulardata.io/ws/v1/oauth/tokens",
    "test": "https://api.test.tabulardata.io/ws/v1/oauth/tokens",
    "dev": "https://api.dev.tabulardata.io/ws/v1/oauth/tokens",
}


class TabularOAuth:
    base_url: str

    def __init__(self, environment: str):
        self.base_url = ENVIRONMENT_URLS[environment]

    def request_token(self, credential: str, scopes: Optional[Any] = None) -> ClientOauthTokenResponse:
        if SEMICOLON in credential:
            client_id, client_secret = credential.split(SEMICOLON)
        else:
            client_id, client_secret = None, credential

        payload = {GRANT_TYPE: CLIENT_CREDENTIALS, CLIENT_SECRET: client_secret, SCOPE: _join_scopes(_parse_scopes(scopes))}

        if client_id is not None:
            payload[CLIENT_ID] = client_id

        return _do_request(self.base_url, payload, ClientOauthTokenResponse)

    def request_user_token(
        self,
        service_token: str,
        id_token: str,
        service_token_type: str = TOKEN_ID_TYPE,
        id_token_type: str = TOKEN_ACCESS_TYPE,
        scopes: Optional[Any] = None,
    ):
        if service_token_type not in VALID_TOKEN_TYPES:
            raise ValueError(f"Invalid subject token type: {service_token_type}")

        if id_token_type not in VALID_TOKEN_TYPES:
            raise ValueError(f"Invalid actor token type: {id_token_type}")

        payload = {
            GRANT_TYPE: TOKEN_EXCHANGE,
            SCOPE: _join_scopes(scopes or {CATALOG_SCOPE}),
            SUBJECT_TOKEN: service_token,
            SUBJECT_TOKEN_TYPE: service_token_type,
            ACTOR_TOKEN: id_token,
            ACTOR_TOKEN_TYPE: id_token_type,
        }

        return _do_request(self.base_url, payload, OAuthTokenResponse)

    def refresh_token(
        self,
        token: str,
        token_type: str,
        scopes: Optional[Any] = None,
    ) -> OAuthTokenResponse:
        if token_type not in VALID_TOKEN_TYPES:
            raise ValueError(f"Invalid token type: {token_type}")

        payload = {
            GRANT_TYPE: TOKEN_EXCHANGE,
            SCOPE: _join_scopes(scopes or {CATALOG_SCOPE}),
            SUBJECT_TOKEN: token,
            SUBJECT_TOKEN_TYPE: token_type,
        }

        return _do_request(self.base_url, payload, OAuthTokenResponse)
