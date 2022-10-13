from typing import Optional, Union
from django.conf import settings

from kramlin.oauth.graphql.inputs import OAuthConfigurationInput
from kramlin.oauth.graphql.types import SSOConfiguration, OAuthConfiguration
from kramlin.oauth.utils import OAuthClientConfiguration, OAuthHandler, OAuthProviderConfiguration


class OAuthAuthenticateResponse:
    def __init__(self, user_info: dict, user=None):
        self.user_info = user_info
        self.user = user


class SSOManager:

    def __init__(
        self,
        oAuthEnabled: Optional[bool] = False,
        oAuth: Optional[Union[OAuthConfigurationInput, dict]] = None,
    ):
        self.oAuthEnabled: bool = oAuthEnabled
        self.oAuth: Optional[OAuthClientConfiguration] = None
        if oAuth:
            if type(oAuth) == dict:
                oAuth = OAuthConfigurationInput(**oAuth)
            self.oAuth = OAuthClientConfiguration(
                clientID=oAuth.clientID,
                clientSecret=oAuth.clientSecret,
                scopes=oAuth.scopes,
                redirectURI=(
                    settings.SSO_OAUTH_REDIRECT_URL if settings.SSO_OAUTH_REDIRECT_URL
                    else "http://localhost/oauth-callback"
                ),
                provider=OAuthProviderConfiguration(
                    name='SSO',
                    authorizationEndpoint=oAuth.authorizationEndpoint,
                    tokenEndpoint=oAuth.tokenEndpoint,
                    revocationEndpoint=oAuth.revocationEndpoint,
                    userInfoEndpoint=oAuth.userInfoEndpoint,
                )
            )

    def authenticate_user(self, code) -> Optional[OAuthAuthenticateResponse]:
        if not (self.oAuthEnabled and self.oAuth):
            return None
        handler = OAuthHandler(client=self.oAuth)
        data = handler.perform_login(code=code)

        from django.contrib.auth import get_user_model
        User = get_user_model()

        try:
            # If the user with the OAuth'ed email already has an account
            user = User.objects.get(email__iexact=data.user_info['email'])
            if hasattr(User, 'ssoData'):
                user.ssoData = data.user_info
                user.save()
            return OAuthAuthenticateResponse(
                user_info=data.user_info,
                user=user,
            )
        except User.DoesNotExist:
            return OAuthAuthenticateResponse(
                user_info=data.user_info,
            )

    def graphql(self) -> SSOConfiguration:
        return SSOConfiguration(
            oAuthEnabled=self.oAuthEnabled,
            oAuth=OAuthConfiguration(
                redirectURL=self.oAuth.redirectURI,
                clientID=self.oAuth.clientID,
                clientSecret=self.oAuth.clientSecret,
                scopes=self.oAuth.scopes,
                authorizationEndpoint=self.oAuth.provider.authorizationEndpoint,
                tokenEndpoint=self.oAuth.provider.tokenEndpoint,
                userInfoEndpoint=self.oAuth.provider.userInfoEndpoint,
                revocationEndpoint=self.oAuth.provider.revocationEndpoint
            ) if self.oAuth else None,
        )

    def dict(self) -> dict:
        return {
            'oAuthEnabled': self.oAuthEnabled,
            'oAuth': {
                'clientID': self.oAuth.clientID,
                'clientSecret': self.oAuth.clientSecret,
                'scopes': self.oAuth.scopes,
                'authorizationEndpoint': self.oAuth.provider.authorizationEndpoint,
                'tokenEndpoint': self.oAuth.provider.tokenEndpoint,
                'userInfoEndpoint': self.oAuth.provider.userInfoEndpoint,
                'revocationEndpoint': self.oAuth.provider.revocationEndpoint
            } if self.oAuth else None,
        }


__all__ = [
    'SSOManager',
]
