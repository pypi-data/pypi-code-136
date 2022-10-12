"""Declares :class:`TokenRequest`."""
import typing

import pydantic

from .authorizationcodegrant import AuthorizationCodeGrant
from .basegrant import BaseGrant
from .clientcredentialsgrant import ClientCredentialsGrant
from .jwtbearerassertiongrant import JWTBearerAssertionGrant
from .refreshtokengrant import RefreshTokenGrant
from .sessiongrant import SessionGrant


class TokenRequestParameters(pydantic.BaseModel):
    """The parameters available for requests to the **Token Endpoint**."""
    __module__: str = 'cbra.ext.oauth2'
    __root__: typing.Union[
        AuthorizationCodeGrant,
        ClientCredentialsGrant,
        JWTBearerAssertionGrant,
        RefreshTokenGrant,
        SessionGrant
    ]

    def get_root(self) -> BaseGrant:
        return self.__root__