import strawberry

from typing import Optional


@strawberry.type
class OAuthPublicConfiguration:
    clientId: Optional[str] = None
    authorizationUrl: Optional[str] = None
    scopes: Optional[str] = None
    redirectUrl: Optional[str] = None


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


__all__ = [
    "OAuthProvider",
    "OAuthConfiguration",
    "OAuthPublicConfiguration",
]
