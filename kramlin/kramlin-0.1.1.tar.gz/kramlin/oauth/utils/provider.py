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
    authorizationEndpoint='https://accounts.google.com/o/oauth2/v2/auth',
    tokenEndpoint='https://oauth2.googleapis.com/token',
    userInfoEndpoint='https://www.googleapis.com/oauth2/v1/userinfo?alt=json',
    authVar='Bearer'
)

GITHUB_OAUTH_CONFIG = OAuthProviderConfiguration(
    name='github',
    authorizationEndpoint='https://github.com/login/oauth/authorize',
    tokenEndpoint='https://github.com/login/oauth/access_token',
    userInfoEndpoint='https://api.github.com/user',
    authVar='token'
)

TWITTER_OAUTH_CONFIG = OAuthProviderConfiguration(
    name='twitter',
    authorizationEndpoint='https://twitter.com/i/oauth2/authorize',
    tokenEndpoint='https://api.twitter.com/oauth2/token',
    userInfoEndpoint='https://api.twitter.com/2/users/me',
    authVar='Bearer'
)


__all__ = [
    'OAuthProviderConfiguration',
    'GOOGLE_OAUTH_CONFIG',
    'TWITTER_OAUTH_CONFIG',
]

