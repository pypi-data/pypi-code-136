import base64

from time import time

class SomfyConnectedThermostatOAuth:
    """Implements Authorization Code Flow for SomfyConnectedThermostat's OAuth implementation."""

    OAUTH_TOKEN_URL = 'https://accounts.somfy.com/oauth/oauth/v2/token'

    def __init__(self, username, password, websession):
        """Create a SomfyConnectedThermostatOAuth object."""
        self.client_id = base64.b64decode(
          'MWUyZDgzMGYtNGM2NS0xMWU3LWJkMGMtMDJkZDU5YmQzMDQxXzVuNzhyNW5ud2F3NHdjMGtza2tnMGNzb2drazhjd29jc3dnODRjMGdvd2Nnb3Nzb2d3'
        ).decode("utf-8")
        self.client_secret = base64.b64decode(
          'NHR4dWN3c3YyOWE4bzBjbzhzOGt3OGdnc3dra3M4b3NzY2NvY2tnY2Nrb2t3OGNrMDA='
        ).decode("utf-8")
        self.username = username
        self.password = password
        self.websession = websession

    async def get_tokens(self):
        """Get the access token for the app."""
        payload = {'client_id': self.client_id,
                   'client_secret': self.client_secret,
                   'username': self.username,
                   'password': self.password,
                   'grant_type': 'password'}

        response = await self.websession.post(self.OAUTH_TOKEN_URL,
                                              data=payload,
                                              allow_redirects=True)
        if response.status != 200:
            raise SomfyConnectedThermostatOauthError(response.status)
        tokens = await response.json()
        update_expires_at(tokens)
        return tokens

    async def refresh_tokens(self, tokens):
        """Refresh access token."""
        if tokens is None:
            return tokens
        if not is_token_expired(tokens):
            return tokens

        payload = {'client_id': self.client_id,
                   'refresh_token': tokens['refresh_token'],
                   'client_secret': self.client_secret,
                   'grant_type': 'refresh_token'}

        response = await self.websession.post(self.OAUTH_TOKEN_URL,
                                              data=payload)
        if response.status != 200:
            return None
        tokens = await response.json()
        update_expires_at(tokens)

        return tokens

class SomfyConnectedThermostatOauthError(Exception):
    """SomfyConnectedThermostatOauthError."""

def update_expires_at(tokens):
  tokens['expires_at'] = int(time()) + tokens['expires_in']

def is_token_expired(tokens):
    """Check if token is expired."""
    return tokens['expires_at'] - int(time()) < 60