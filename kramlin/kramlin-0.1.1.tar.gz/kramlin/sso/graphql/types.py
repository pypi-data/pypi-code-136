import strawberry
from typing import Optional

from kramlin.oauth.graphql.types import OAuthConfiguration, OAuthPublicConfiguration


@strawberry.type
class SSOConfiguration:
    oAuthEnabled: Optional[bool] = None
    oAuth: Optional[OAuthConfiguration] = None


@strawberry.type
class PublicSSOConfiguration:
    oAuth: Optional[OAuthPublicConfiguration] = None


__all__ = [
    'SSOConfiguration',
    'PublicSSOConfiguration'
]
