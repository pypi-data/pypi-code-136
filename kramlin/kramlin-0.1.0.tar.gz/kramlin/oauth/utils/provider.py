from typing import Optional


class OAuthProviderConfiguration:

    def __init__(
        self,
        name: str,
        authorizationEndpoint: str,
        tokenEndpoint: str,
        userInfoEndpoint: str,
        revocationEndpoint: str = None,
        authVar: Optional[str] = "Bearer"
    ):
        self.name = name
        self.authorizationEndpoint = authorizationEndpoint
        self.tokenEndpoint = tokenEndpoint
        self.userInfoEndpoint = userInfoEndpoint
        self.revocationEndpoint = revocationEndpoint
        self.authVar = authVar


GOOGLE_OAUTH_CONFIG = OAuthProviderConfiguration(
    name='google',
    tokenEndpoint='https://oauth2.googleapis.com/token',
    userInfoEndpoint='https://www.googleapis.com/oauth2/v1/userinfo?alt=json',
    authVar='Bearer'
)

TWITTER_OAUTH_CONFIG = OAuthProviderConfiguration(
    name='twitter',
    tokenEndpoint='https://api.twitter.com/oauth2/token',
    userInfoEndpoint='https://api.twitter.com/2/users/me',
    authVar='Bearer'
)


__all__ = [
    'OAuthProviderConfiguration',
    'GOOGLE_OAUTH_CONFIG',
    'TWITTER_OAUTH_CONFIG',
]

