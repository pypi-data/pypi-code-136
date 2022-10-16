
"""Library to handle connection with SomfyConnectedThermostat API."""
from aiohttp import ClientSession
from somfy_connected_thermostat.auth import SomfyConnectedThermostatOAuth, SomfyConnectedThermostatOauthError, is_token_expired

from somfy_connected_thermostat.models import Principal, Smartphone, Thermostat, ThermostatCommand, ThermostatInfo

API_ENDPOINT = 'https://th1.somfy.com/rest-api'

class SomfyConnectedThermostatApi:
    """Class to comunicate with the SomfyConnectedThermostat api."""

    def __init__(self, oauth: SomfyConnectedThermostatOAuth, websession: ClientSession):
        """Initialize the SomfyConnectedThermostatApi."""
        self.oauth = oauth
        self.websession = websession

    async def login(self):
        """Get access token."""
        self.tokens = await self.oauth.get_tokens()

    async def get_principal(self):
        """Get authenticated user"""

        headers = {
          'user-agent': 'okhttp/4.9.0',
          'authorization': 'bearer' + await self.__get_access_token(),
        }

        url = f'{API_ENDPOINT}/api/user/me'

        res = await self.websession.get(url, headers=headers)
        data = await res.json()
        return Principal(data.get('id'), data.get('first_name'), data.get('last_name'), data.get('email'))

    async def get_thermostats(self):
        headers = {
          'user-agent': 'okhttp/4.9.0',
          'authorization': 'bearer' + await self.__get_access_token(),
        }

        url = f'{API_ENDPOINT}/api/thermostats'

        res = await self.websession.get(url, headers=headers)
        data = await res.json()

        return list(
          map(
            lambda item: Thermostat(item.get('id'), item.get('name')),
            data.get('results')
          )
        )

    async def get_smartphones(self, thermostat_id: str):
        headers = {
          'user-agent': 'okhttp/4.9.0',
          'authorization': 'bearer' + await self.__get_access_token(),
        }

        url = f'{API_ENDPOINT}/api/thermostats/{thermostat_id}/smartphones'

        res = await self.websession.get(url, headers=headers)
        data = await res.json()

        return list(
          map(
            lambda item: Smartphone(item.get('id'), item.get('vendor_id'), item.get('push_token')),
            data
          )
        )

    async def get_thermostat_info(self, thermostat_id: str, smartphone_vendor_id: str, only_changes: bool = False):
        headers = {
          'user-agent': 'okhttp/4.9.0',
          'authorization': 'bearer' + await self.__get_access_token(),
        }

        url = f'{API_ENDPOINT}/api/smartphones/{smartphone_vendor_id}/thermostats/{thermostat_id}/all_informations?timestamp={1 if only_changes else 0 }'

        res = await self.websession.get(url, headers=headers)
        data = await res.json()

        temperature_consigne = data.get('temperature_consigne')
        derogation = data.get('latest_derogation')

        if derogation:
          temperature_override = derogation.get('temperature')
          if temperature_override:
            temperature_consigne = temperature_override

        return ThermostatInfo(
          data.get('temperature'),
          temperature_consigne,
          data.get('battery'),
          data.get('mode')
        )

    async def put_thermostat_command(self, thermostat_id: str, command: ThermostatCommand):
        headers = {
          'user-agent': 'okhttp/4.9.0',
          'authorization': 'bearer' + await self.__get_access_token(),
        }

        url = f'{API_ENDPOINT}/api/thermostats/{thermostat_id}/target_temperature'

        res = await self.websession.put(url, json=command.__dict__, headers=headers)

        if res.status >= 300:
            raise SomfyConnectedSendCommandError(res.status)

    async def __get_access_token(self):
        if not is_token_expired(self.tokens):
            return self.tokens.get('access_token')

        try:
            self.tokens = await self.oauth.refresh_tokens(self.tokens)
        except SomfyConnectedThermostatOauthError:
            self.tokens = None

        if self.tokens is None:
            self.tokens = await self.oauth.get_tokens()

        return self.tokens.get('access_token')

class SomfyConnectedSendCommandError(Exception):
    """SomfyConnectedSendCommandError."""