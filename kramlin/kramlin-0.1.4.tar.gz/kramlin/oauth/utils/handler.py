from typing import Optional

from requests import post, get
from kramlin.exceptions import APIError

from .client import OAuthClientConfiguration
from .provider import OAuthProviderConfiguration


class OAuthTokenResponse:
    def __init__(self, access_token: str, token_type: str = 'Bearer', refresh_token: str = None):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_type = token_type

    def __repr__(self):
        return f"<OAuthTokenResponse {self.access_token}>"


class OAuthLoginResponse:
    def __init__(self, token: OAuthTokenResponse, user_info: dict):
        self.token = token
        self.user_info = user_info

    def __repr__(self):
        return f"<OAuthLoginResponse {self.token} {self.user_info}>"


class OAuthHandler:

    def __init__(self, client: OAuthClientConfiguration):
        self.clientID = client.clientID
        self.clientSecret = client.clientSecret
        self.redirect_uri = client.redirectURI
        self.authVar = client.provider.authVar
        self.provider: OAuthProviderConfiguration = client.provider

    def get_token_from_auth_code(self, code: str) -> Optional[OAuthTokenResponse]:
        resp = post(
            url=self.provider.tokenEndpoint,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": self.redirect_uri,
                "client_id": self.clientID,
                "client_secret": self.clientSecret,
            }
        )
        if resp.status_code != 200:
            print("Failed to verify authorization code.")
            print(resp.text)
            raise APIError(
                code="OAUTH_FAILED", message="Failed to verify authorizationCode."
            )
        resp_type = resp.headers.get("Content-Type")
        refresh_token = None
        if "application/json" in resp_type:
            data = resp.json()
            access_token = data["access_token"]
            if 'refreshToken' in data and len(data['refreshToken']) > 0:
                refresh_token = data['refresh_token']
            if "token_type" in data and data["token_type"]:
                self.authVar = data["token_type"]
        elif "application/x-www-form-urlencoded" in resp_type:
            from urllib.parse import parse_qs
            data = parse_qs(resp.text)
            if "token_type" in data and data["token_type"]:
                self.authVar = data["token_type"][0]
            access_token = data["access_token"][0]
            if 'refreshToken' in data and len(data['refreshToken']) > 0:
                refresh_token = data["refresh_token"][0]
        else:
            raise APIError(
                code="OAUTH_FAILED",
                message="Failed to verify authorization code. Unknown response type.",
            )
        return OAuthTokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type=self.authVar
        )

    def get_user_info_with_token(self, access_token: str) -> dict:
        resp = get(
            url=self.provider.userInfoEndpoint,
            headers={
                "Authorization": f"{self.authVar} {access_token}",
            },
        )
        if resp.status_code != 200:
            print("Failed to retrieve user info.")
            print(resp.text)
            raise APIError(code="OAUTH_FAILED", message="Failed to retrieve User Info.")
        resp_type = resp.headers.get("Content-Type")
        if "application/json" in resp_type:
            return resp.json()
        raise APIError(
            code="OAUTH_FAILED",
            message="Failed to retrieve User Info. Unknown response type.",
        )

    def perform_login(self, code: str) -> OAuthLoginResponse:
        # Give authorization code got from frontend with ClientSecret to generate access token
        token_data = self.get_token_from_auth_code(code=code)
        # Use the generated access token to fetch the details about the user, especially their email
        user_info = self.get_user_info_with_token(access_token=token_data.access_token)
        # email is required to create or login to a user account
        if "email" not in user_info or len(user_info["email"]) < 1:
            raise APIError(
                code="OAUTH_FAILED",
                message="Unable to obtain email address from OAuth provider.",
            )
        return OAuthLoginResponse(
            token=token_data,
            user_info=user_info,
        )


__all__ = [
    "OAuthHandler",
    "OAuthLoginResponse"
]
