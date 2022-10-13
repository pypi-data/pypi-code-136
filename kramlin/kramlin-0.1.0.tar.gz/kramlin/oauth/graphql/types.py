import strawberry

from typing import Optional


@strawberry.type
class OAuthProvider:
    name: Optional[str] = None
    authorizationEndpoint: Optional[str] = None
    tokenEndpoint: Optional[str] = None
    revocationEndpoint: Optional[str] = None
    userInfoEndpoint: Optional[str] = None
    redirectURL: Optional[str] = None
    scopes: Optional[str] = None


@strawberry.type
class OAuthConfiguration(OAuthProvider):
    clientID: Optional[str] = None
    clientSecret: Optional[str] = None


@strawberry.type
class SSOConfiguration:
    oAuthEnabled: Optional[bool] = None
    oAuth: Optional[OAuthConfiguration] = None


__all__ = [
    "OAuthConfiguration",
    "SSOConfiguration",
]
