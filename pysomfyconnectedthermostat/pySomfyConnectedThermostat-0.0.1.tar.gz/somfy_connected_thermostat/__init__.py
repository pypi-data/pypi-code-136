
"""Library to handle connection with SomfyConnectedThermostat API."""
import json
import logging
from aiohttp import ClientSession
from somfy_connected_thermostat.auth import SomfyConnectedThermostatOAuth, SomfyConnectedThermostatOauthError, __is_token_expired

from somfy_connected_thermostat.models import Principal, Smartphone, Thermostat, ThermostatCommand, ThermostatInfo

API_ENDPOINT = 'https://th1.somfy.com/rest-api'

_LOGGER = logging.getLogger(__name__)

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

        return ThermostatInfo(
          data.get('temperature'),
          data.get('temperature_consigne'),
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
        if not __is_token_expired(self.tokens):
            return self.tokens.get('access_token')

        try:
            self.tokens = await self.oauth.refresh_tokens(self.tokens)
        except SomfyConnectedThermostatOauthError:
            self.tokens = None

        if self.tokens is None:
            self.tokens = await self.oauth.get_tokens()

        return self.tokens.get('access_token')

class SomfyConnectedThermostatDevice:
    """Instance of SomfyConnectedThermostat device."""

    def __init__(self, room_name, location_name, device_id):
        """Initialize the SomfyConnectedThermostat device class."""
        self._room_name = room_name
        self._location_name = location_name
        self._device_id = device_id
        self._mode = None

    @property
    def device_id(self):
        """Return a device ID."""
        return self._device_id

    @property
    def name(self):
        """Return a device name."""
        return self._room_name

    async def request(self, command, params, retry=3, get=True):
        """Request data."""
        if 'multiple' in params:
            params['multiple'] = 'True' if params['multiple'] else 'False'
        params['room_name'] = self._room_name
        params['location_name'] = self._location_name
        res = await self.control.request(command, params, retry, get)
        try:
            res = json.loads(res)
            if isinstance(res, dict) and res.get('error'):
                _LOGGER.error(res.get('error'))
            return res
        except TypeError:
            if isinstance(res, dict):
                status = res.get('status')
                if status is not None:
                    if status == 'ok':
                        return True
                    return False
        return None

    async def set_power_off(self, multiple=False):
        """Power off your AC."""
        return await self.request('device/power/off', {'multiple': multiple})

    async def set_comfort_mode(self, multiple=False):
        """Enable Comfort mode on your AC."""
        return await self.request('device/mode/comfort', {'multiple': multiple})

    async def set_comfort_feedback(self, value):
        """Send feedback for Comfort mode."""
        valid_comfort_feedback = ['too_hot', 'too_warm', 'bit_warm', 'comfortable',
                                  'bit_cold', 'too_cold', 'freezing']
        if value not in valid_comfort_feedback:
            _LOGGER.error("Invalid comfort feedback")
            return
        return await self.request('user/feedback', {'value': value})

    async def set_away_mode_temperature_lower(self, value, multiple=False):
        """Enable Away mode and set an lower bound for temperature."""
        return await self.request('device/mode/away_temperature_lower',
                                  {'multiple': multiple, 'value': value})

    async def set_away_mode_temperature_upper(self, value, multiple=False):
        """Enable Away mode and set an upper bound for temperature."""
        return await self.request('device/mode/away_temperature_upper',
                                  {'multiple': multiple, 'value': value})

    async def set_away_humidity_upper(self, value, multiple=False):
        """Enable Away mode and set an upper bound for humidity."""
        return await self.request('device/mode/away_humidity_upper',
                                  {'multiple': multiple, 'value': value})

    async def set_temperature_mode(self, value, multiple=False):
        """Enable Temperature mode on your AC."""
        return await self.request('device/mode/temperature',
                                  {'multiple': multiple, 'value': value})

    async def get_sensor_temperature(self):
        """Get latest sensor temperature data."""
        res = await self.request('device/sensor/temperature', {})
        if res is None:
            return None
        return res[0].get('value')

    async def get_sensor_humidity(self):
        """Get latest sensor humidity data."""
        res = await self.request('device/sensor/humidity', {})
        val = res[0].get('value')
        if val is None:
            return None
        return round(val, 1)

    async def get_mode(self):
        """Get Ambi Climate's current working mode."""
        res = await self.request('device/mode', {})
        if res is None:
            return None
        return res.get('mode', '')

    async def get_ir_feature(self):
        """Get Ambi Climate's appliance IR feature."""
        return await self.request('device/ir_feature', {})

    async def get_appliance_states(self, limit=1, offset=0):
        """Get Ambi Climate's last N appliance states."""
        return await self.request('device/appliance_states',
                                  {'limit': limit, 'offset': offset})

    async def set_target_temperature(self, temperature):
        """Set target temperature."""
        if self._mode and self._mode.lower() != 'manual':
            _LOGGER.error("Mode has to be sat to manual in the "
                          "SomfyConnectedThermostat app. Current mode is %s.", self._mode)
            return

        data = self.ac_data[0]
        params = {"mode": data['mode'].lower(),
                  "power": data['power'].lower(),
                  "feature": {
                      "temperature": str(int(temperature)),
                      "fan": data['fan'].lower(),
                      "louver": data.get('louver', "auto").lower() if data.get('louver') else 'auto',
                      'swing': data.get('swing', "auto").lower() if data.get('swing') else 'oscillate',
                  }}
        return await self.request('device/deployments', params, get=False)

    async def turn_off(self):
        """Turn off."""
        return await self.set_power_off()

    async def turn_on(self):
        """Turn on."""
        data = self.ac_data[0]
        feature = {}
        feature["temperature"] = str(data.get('target_temperature', data.get('temperature', 20)))
        feature['fan'] = data['fan'].lower() if data.get('fan') else 'med-high'
        feature['louver'] = data['louver'].lower() if data.get('louver') else 'auto'
        feature['swing'] = data['swing'].lower() if data.get('swing') else 'oscillate'
        params = {"mode": data.get('mode', 'Heat').lower(),
                  "power": 'on',
                  "feature": feature}
        return await self.request('device/deployments', params, get=False)

    def get_min_temp(self):
        """Get min temperature."""
        res = 1000
        data = self.ir_features['data'][self.ac_data[0].get('mode').lower()]['temperature']['value']
        for temp in data:
            if float(temp) < res:
                res = float(temp)
        return res

    def get_max_temp(self):
        """Get max temperature."""
        res = -1000
        data = self.ir_features['data'][self.ac_data[0].get('mode').lower()]['temperature']['value']
        for temp in data:
            if float(temp) > res:
                res = float(temp)
        return res

    async def update_device_info(self):
        """Update device info."""
        self.ir_features = await self.get_ir_feature()

    async def update_device(self):
        """Update device."""
        data = dict()
        data['target_temperature'] = None
        states = await self.get_appliance_states()
        if states:
            self.ac_data = states.get('data', [{}])
            data['target_temperature'] = self.ac_data[0].get('temperature')
            data['power'] = self.ac_data[0].get('power')
        temp = await self.get_sensor_temperature()
        data['temperature'] = round(temp, 1) if temp else None
        humidity = await self.get_sensor_humidity()
        data['humidity'] = round(humidity, 1) if humidity else None
        self._mode = await self.get_mode()
        return data

class SomfyConnectedSendCommandError(Exception):
    """SomfyConnectedSendCommandError."""