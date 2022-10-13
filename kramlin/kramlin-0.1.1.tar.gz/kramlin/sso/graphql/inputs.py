import strawberry
from typing import Optional

from kramlin.oauth.graphql.inputs import OAuthConfigurationInput


@strawberry.input
class SSOConfigurationInput:
    oAuthEnabled: Optional[bool] = None
    oAuth: Optional[OAuthConfigurationInput] = None


__all__ = [
    'SSOConfigurationInput'
]
