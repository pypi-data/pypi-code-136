from typing import Optional

import strawberry


@strawberry.input
class OAuthConfigurationInput:
    clientID: str
    clientSecret: str
    authorizationEndpoint: str
    tokenEndpoint: str
    userInfoEndpoint: str
    revocationEndpoint: Optional[str] = None
    scopes: Optional[str] = None


__all__ = [
    'OAuthConfigurationInput'
]
