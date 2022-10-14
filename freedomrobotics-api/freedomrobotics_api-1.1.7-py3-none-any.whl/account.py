import os
import json
import platform

from .alert import get_alert, get_alerts
from .device import Device
from .entity import Entity
from .zone import Zone
from .token import Token
from .api_handler import NotFoundError
from .op_deployment import get_opdeployment


class Account(Entity):
    """An account within the Freedom Robotics API. Normally fetched from a :obj:`FreedomClient`
    and not intended to be manually instantiated by the user of the API.

    Args:
        _id (str): Account ID.
        _data (`dict`): Account data.
    """
    pk = 'account'

    @property
    def url_base(self):
        return "/accounts/{}".format(self._id)

    @property
    def company(self):
        """str: The company or organization of the account.
        """
        return self._data.get("company")

    def find_device(self, name=""):
        """:obj:`Device`: Finds a device by its name (i.e. the name set in the Freedom web app).
        Case-insensitive.
        If there are no matches, or there is more than one match, an exception will be thrown.

        Args:
            name (str): The name of the device.
        """

        devices = [device for device in self.get_devices() if device.name.lower() == name.lower()]

        if len(devices) == 0:
            raise Exception("No device found")

        if len(devices) > 1:
            raise Exception("Multiple devices found")

        return devices[0]

    def create_device(
            self,
            name="default",
            description="",
            device_type="",
            location="",
            platform="ros",
            api_call_kwargs={},
            ):
        """:obj:`Device`: Creates a new device.

        Args:
            name (str): Device name.
            description (str): Device description.
            device_type (str): Device type.
            location (str): Device location.
            platform (str): Device platform.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        response = self.api.call(
            "POST",
            "/accounts/{}/devices".format(self._id),
            data={
                "name": name,
                "description": description,
                "type": device_type,
                "location": location,
                "platform": platform,
            },
            **api_call_kwargs
        )

        if response and response.get("status") != "success":
            raise Exception("create device error: {}".format(response))

        return self.get_device(response.get("device"))

    def get_device(self, device_id, params=None, raw=False, api_call_kwargs={}, **kwargs):
        """:obj:`Device`: Fetch an device by its device ID (Dxxxxxxxxxxxx).

        Args:
            device_id (str): Device ID.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
            **kwargs (dict): Extra attributes for Device object.
        """

        device_data = self.api.call(
            "GET",
            "/accounts/{}/devices/{}".format(self._id, device_id),
            params=params,
            **api_call_kwargs
        )
        if not device_data:
            return None

        if raw:
            device = device_data
        else:
            device = Device(device_data["device"], device_data, api=self.api, **kwargs)
        return device

    def get_devices(
            self,
            attributes=None,
            zones=None,
            include_subzones=None,
            params=None,
            raw=False,
            api_call_kwargs={},
            **kwargs
            ):
        """:obj:`list` of :obj:`Device`: Fetch a list of all devices in the account.

        Args:
            device_id (str): Device ID.
            attributes (list): Optional list of device attributes to return.
            attributes (zones): Optional list of zones to filter.
            include_subzones (bool): Flag to indicate if should include subzone devices in result.
                This will only work when `zones` are passed.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
            **kwargs (dict): Extra attributes for Device objects.
        """

        if params is None:
            params = {}
        if attributes is not None:
            params["attributes"] = json.dumps(attributes)
        if zones is not None:
            params["zones"] = json.dumps(zones)
        if include_subzones is not None:
            params["include_subzones"] = json.dumps(include_subzones)

        result = self.api.call("GET", "/accounts/{}/devices".format(self._id), params=params, **api_call_kwargs)
        if not isinstance(result, list):
            raise ValueError("API returned incorrect type")
        if raw:
            return result
        else:
            return [
                Device(device_data["device"], device_data, api=self.api, **kwargs)
                for device_data in result
            ]

    def get_zones(self, params=None, raw=False, api_call_kwargs={}, **kwargs):
        """:obj:`list` of :obj:`Zone`: Fetch a list of all zones in the account.

        Args:
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
            **kwargs (dict): Extra attributes for Zone objects.
        """
        result = self.api.call(
            "GET",
            "/accounts/{}/zones".format(self._id),
            params=params,
            **api_call_kwargs,
        )
        if not result:
            return []
        if raw:
            return result
        else:
            return [
                Zone(data['id'], data, api=self.api, **kwargs)
                for data in result
            ]

    def get_zone(self, zone_id, params=None, raw=False, api_call_kwargs={}, **kwargs):
        """:obj:`Zone`: Fetch the zone with specified id in the account.

        Args:
            zone_id
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
            **kwargs (dict): Extra attributes for Zone objects.
        """
        result = self.api.call(
            "GET",
            "/accounts/{}/zones/{}".format(self._id, zone_id),
            params=params,
            **api_call_kwargs,
        )
        if raw:
            return result
        else:
            return Zone(result['id'], result, api=self.api, **kwargs)

    def get_opdeployment(self, opdeployment_id, params=None, raw=False, api_call_kwargs={}):
        """:obj:`Zone`: Fetch the on prem deployment with specified id in the account.

        Args:
            opdeployment_id (str): on prem deployment ID.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        return get_opdeployment(self.api, self._id, opdeployment_id, params=params, raw=raw,
                                api_call_kwargs=api_call_kwargs)

    def get_alert(self, alert_id, attributes=None, raw=False, params=None, api_call_kwargs={}):
        """:obj:`Alert`: Fetch an Alert by its ID

        Args:
            alert_id (str): Alert ID.
            attributes (list): Optional list of attributes to request.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        alert = get_alert(
            self.api,
            self._id,
            alert_id,
            attributes=attributes,
            params=params,
            raw=raw,
            account_name=self.name,
            api_call_kwargs=api_call_kwargs,
        )
        return alert

    def get_alerts(self, attributes=None, params=None, raw=False, api_call_kwargs={}):
        """:obj:`list` of :obj:`Alert`: Fetch a list of alerts for the account, according to the used params

        Args:
            attributes (list): Optional list of attributes to request.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        alerts = get_alerts(
            self.api,
            self._id,
            attributes=attributes,
            params=params,
            raw=raw,
            account_name=self.name,
            api_call_kwargs=api_call_kwargs,
        )
        return alerts

    def get_zone_alerts(self, zone_id, attributes=None, params=None, raw=False, api_call_kwargs={}):
        """:obj:`list` of :obj:`Alert`: Fetch a list of alerts for the zone, according to the used params

        Args:
            zone_id (str): Zone ID.
            attributes (list): Optional list of attributes to request.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        alerts = get_alerts(
            self.api,
            self._id,
            zone_id=zone_id,
            attributes=attributes,
            params=params,
            raw=raw,
            account_name=self.name,
            api_call_kwargs=api_call_kwargs,
        )
        return alerts

    def get_device_alerts(self, device_id, attributes=None, params=None, raw=False, api_call_kwargs={}):
        """:obj:`list` of :obj:`Alert`: Fetch a list of alerts for the device, according to the used params

        Args:
            device_id (str): Device ID.
            attributes (list): Optional list of attributes to request.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        alerts = get_alerts(
            self.api,
            self._id,
            device_id=device_id,
            attributes=attributes,
            params=params,
            raw=raw,
            account_name=self.name,
            api_call_kwargs=api_call_kwargs,
        )
        return alerts

    def get_setting(self, setting_name, params=None, raw=True, api_call_kwargs={}):
        """:obj:`Setting`: Finds a setting by its name.

        Args:
            setting_name (string): name of the setting. Has to be a root level entry
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. True by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        if not raw:
            raise NotImplementedError("Not implemented object version of Setting yet")
        return self.api.call(
            "GET",
            "/accounts/{}/settings/{}".format(self._id, setting_name),
            params=params,
            **api_call_kwargs
        )

    def get_settings(self, params=None, raw=True, api_call_kwargs={}):
        """:obj:`dict`: Fetch a all settings in the account.

        Args:
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. True by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        if not raw:
            raise NotImplementedError("Not implemented object version of Setting yet")
        return self.api.call(
            "GET",
            "/accounts/{}/settings".format(self._id),
            params=params,
            **api_call_kwargs
        )

    @property
    def email(self):
        """str: Account e-mail address.
        """
        return self._data.get("email")

    @property
    def features(self):
        """str: Account features.
        """
        return self._data.get("features")

    @property
    def last_seen(self):
        """float: Unix time the account was last seen.
        """
        return self._data.get("last_seen")

    @property
    def max_devices(self):
        """int: Maximum number of devices in the account.
        """
        return self._data.get("max_devices")

    @property
    def name(self):
        """str: Account name.
        """
        return self._data.get("name")

    def get_statistics_csv(self, utc_start=None, utc_end=None, params=None, api_call_kwargs={}):
        """Gets all the statistics for an account in a CSV format.

        Args:
            utc_start (float): Returns statistics starting from the specified timestamp.
                If null, returns the API default range (1 day).
            utc_end (float): Returns statistics until the specified timestamp (inclusive).
                If null, returns the statistics until current hour.
            params (dict): Extra parameters that could be included in the request.
            api_call_kwargs (dict): Optional keyword arguments for api call.

        Returns:
            String object with the CSV content.
        """
        if params is None:
            params = {}
        if utc_start is not None:
            params['utc_start'] = utc_start
        if utc_end is not None:
            params['utc_end'] = utc_end

        data = self.api.call(
            "GET",
            "/accounts/{}/statistics/csv".format(self._id),
            raw=True,
            params=params,
            **api_call_kwargs
        )
        return data

    def put_monitoring(self, service, data, instance=None, pid=None, params=None, api_call_kwargs={}):
        """Puts monitoring data such as heartbeats to the API

        Args:
            service (str): The service name, usually the application that is being monitored.
            data (dict): A dictionary with any details that wanted to be included to
                         create metrics later.
            instance (str)*: Optional. By default will use the computer's name.
            pid (str)*: Optional. By default will use the current pid.
            params (dict): Extra parameters that could be included in the request.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        body = {
            'service': service,
            'instance': instance or platform.uname().node,
            'pid': pid or os.getpid(),
            'data': data
        }
        self.api.call(
            'PUT',
            "/accounts/{}/monitoring".format(self._id),
            data=body,
            params=params,
            **api_call_kwargs
        )

    def set_setting(self, setting_name, setting_value, params=None, api_call_kwargs={}):
        """:obj:`Setting`: Sets a setting by its name.

        Args:
            setting_name (string): name of the setting. Has to be a root level entry
            setting_value: any JSON-serializable structure.
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        try:
            self.put_setting(setting_name, setting_value, params=params, api_call_kwargs=api_call_kwargs)
        except NotFoundError as e:
            self.post_setting(setting_name, setting_value, params=params, api_call_kwargs=api_call_kwargs)

    def post_setting(self, setting_name, setting_value, params=None, api_call_kwargs={}):
        """:obj:`Setting`: Sets a setting by its name, POST version.

        Args:
            setting_name (string): name of the setting. Has to be a root level entry
            setting_value: any JSON-serializable structure.
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        return self.api.call(
            "POST",
            "/accounts/{}/settings".format(self._id),
            data={
                "type": setting_name,
                "value": setting_value,
            },
            params=params,
            **api_call_kwargs
        )

    def put_setting(self, setting_name, setting_value, params=None, api_call_kwargs={}):
        """:obj:`Setting`: Sets a setting by its name, PUT version.

        Args:
            setting_name (string): name of the setting. Has to be a root level entry
            setting_value: any JSON-serializable structure.
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        return self.api.call(
            "PUT",
            "/accounts/{}/settings/{}".format(self._id, setting_name),
            data={
                "type": setting_name,
                "value": setting_value,
            },
            params=params,
            **api_call_kwargs
        )

    def get_token(self, token_id, params=None, raw=False, api_call_kwargs={}):
        """:obj:`list` of :obj:`dict`: Fetch a list of tokens.

        Args:
            token_id (str): Token ID.
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        data = self.api.call(
            "GET",
            "/accounts/{}/tokens/{}".format(self._id, token_id),
            params=params,
            **api_call_kwargs
        )
        if raw:
            return data
        else:
            return Token(data['token'], data, account_id=self._id, api=self.api, **api_call_kwargs)

    def get_tokens(self, params=None, raw=False, api_call_kwargs={}):
        """:obj:`list` of :obj:`dict`: Fetch a list of tokens.

        Args:
            params (dict): Optional query parameters.
            raw (bool): Will return the raw JSON if True. False by default.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        result = self.api.call(
            "GET",
            "/accounts/{}/tokens".format(self._id),
            params=params,
            **api_call_kwargs
        )
        if not result:
            return []
        if raw:
            return result
        else:
            return [
                Token(token_data['token'], token_data, account_id=self._id, api=self.api)
                for token_data in result
            ]
