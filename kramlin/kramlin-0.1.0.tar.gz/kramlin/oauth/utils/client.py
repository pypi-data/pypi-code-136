from .provider import OAuthProviderConfiguration


class OAuthClientConfiguration:

    def __init__(
        self,
        clientID: str,
        clientSecret: str,
        redirectURI: str,
        provider: OAuthProviderConfiguration,
        scopes: str = None
    ):
        self.clientID = clientID
        self.clientSecret = clientSecret
        self.redirectURI = redirectURI
        self.scopes = scopes
        self.provider = provider


__all__ = [
    'OAuthClientConfiguration'
]
