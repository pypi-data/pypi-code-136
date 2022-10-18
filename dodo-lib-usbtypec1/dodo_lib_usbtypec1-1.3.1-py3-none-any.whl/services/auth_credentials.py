from .base import BaseHTTPService
from .. import models
from ..utils import exceptions

__all__ = (
    'AuthClient',
)


class AuthClient(BaseHTTPService):
    service_name = 'AUTH_SERVICE'

    async def get_cookies(self, account_name: str) -> models.AuthCookies:
        response = await self._client.get('/auth/cookies/', params={'account_name': account_name}, timeout=30)
        if response.status_code == 404:
            raise exceptions.NoCookiesError(account_name=account_name)
        return models.AuthCookies.parse_obj(response.json())

    async def get_tokens(self, account_name: str) -> models.AuthToken:
        response = await self._client.get('/auth/token/', params={'account_name': account_name}, timeout=30)
        if response.status_code == 404:
            raise exceptions.NoTokenError(account_name=account_name)
        return models.AuthToken.parse_obj(response.json())

    async def update_cookies(self, account_name: str, cookies: models.Cookies):
        body = {'account_name': account_name, 'cookies': cookies}
        await self._client.patch('/auth/cookies/', json=body)

    async def update_tokens(self, account_name: str, access_token: str, refresh_token: str):
        body = {'account_name': account_name, 'access_token': access_token, 'refresh_token': refresh_token}
        await self._client.patch('/auth/token/', json=body)
