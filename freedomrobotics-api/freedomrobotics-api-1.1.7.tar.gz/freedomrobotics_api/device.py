import json
import time
import logging

from .alert import Alert, get_alerts
from .entity import Entity
from .helpers import to_time_query_param

logger = logging.getLogger(__name__)


class Device(Entity):
    pk = 'device'

    @property
    def url_base(self):
        return '/accounts/{}/devices'.format(self.account)

    def command(self, topic=None, topic_type=None, data=None, expiration_secs=10, platform="ros"):
        cmd = {
            "topic": topic,
            "type": topic_type,
            "data": data,
            "expiration_secs": expiration_secs,
            "platform": platform,
        }
        return self.api.call(
            "PUT",
            "/accounts/{}/devices/{}/commands".format(self.account, self._id),
            data=cmd
        )

    @property
    def cloned_from(self):
        """Where the device was cloned from.
        """
        return self._data.get("clonedFrom")

    @property
    def compute_architecture(self):
        """str: Compute architecture.
        """
        return self._data.get("compute_architecture")

    def create_token(self, params=None, api_call_kwargs={}):
        """dict: Creates a token and returns the response.

        Args:
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        response = self.api.call(
            "POST",
            "/tokens?create_secret=true",
            data={
                "allowed_actions": {
                    "install_script": ["get"],
                    "download": ["get"],
                    "device": ["get", "put"],
                    "device_data": ["put"],
                    "device_commands": ["get"],
                },
                "accounts": [self.account],
                "devices": [self._id],
            },
            params=params,
        )

        if response.get("status") == "success":
            return response
        else:
            return None

    @property
    def account(self):
        return self._data.get('account')

    @property
    def description(self):
        """str: Description of the device.
        """
        return self._data.get("description")

    @property
    def name(self):
        """str: Name of the device.
        """
        return self._data.get("name")

    @property
    def features(self):
        """:obj:`list` of `str`: features of the device.
        """
        return self._data.get("features")

    def get_attr(self, key):
        """Fetches a custom attribute."""

        return self.get(key)

    def set_attr(self, key, value):
        """Sets a custom attribute."""
        self[key] = value

    def set_attrs(self, attrs):
        """Sets multiple custom attributes."""
        self.push(attrs)

    @property
    def platform(self):
        """str: Platform of the device.
        """
        return self._data.get("platform")

    @property
    def device_type(self):
        """str: Device type.
        """
        return self._data.get("type")

    @property
    def mc_alerts_enabled(self):
        """`list`: Alerts enabled for the device.
        """
        return self._data.get("mc.alerts.enabled")

    @property
    def mc_alerts_triggers(self):
        """`list`: Alert triggers.
        """
        return self._data.get("mc.alerts.triggers")

    @property
    def mc_alerts_triggered(self):
        """`list` of :obj:`Alert`: List of alerts that are triggered.
        """
        result = self._data.get("mc.alerts.triggered")
        if not result:
            return []

        alerts = [
            Alert(alert_data["alert_id"], alert_data, device_name=self.name)
            for alert_data in result
        ]
        return alerts

    @property
    def mc_instrumentation_remote_ssh(self):
        """`dict`: Information about currently active SSH reverse port forward.
        Use enable_remote_ssh() to enable ssh.
        """
        return self._data.get("mc.instrumentation.remote_ssh")

    def enable_remote_ssh(self, params=None, api_call_kwargs={}):
        """Enables remote SSH on the device. Following this method,
        periodically .update() the device and check for updates in
        .mc_instrumentation_remote_ssh() for the connection information.

        Args:
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        data = [
            {
                "command": "enable_remote_ssh",
                "platform": "mission_control_controller",
                "expiration_secs": 100,
                "data": {"enable": True},
                "uid": "AEFF321AEF56ECD"
            },
        ]

        response = self.api.call(
            "PUT",
            "/accounts/%s/devices/%s/commands" % (
                self._data.get("account"),
                self._id
            ),
            data=data,
            params=params,
            **api_call_kwargs
        )

        return response

    def data(self, start=None, end=None, topics=None, direction="forward", loop=False, api_call_kwargs={}, **params):
        """iter: Fetches data from the robot for a specified interval and returns an iterator
        to page through the data. Each next() call to the iterator will return 1 message, and
        data will be fetched from the server as necessary until the end has been reached.

        Args:
            start (float): UNIX time of the start of the desired data interval.
            end (float): UNIX time of the end of the desired data interval.
            topics (`list` of `str`): List of topics of interest (in most cases, ROS topics).
            direction (str): "forward" or "backward".
            loop (bool): If True, will keep fetching data forever between the selected `start` and `end`
                filters. If you want to loop for live data, then you should remove the end argument.
            api_call_kwargs (dict): Optional keyword arguments for api call.
            **params (dict): Optional query parameters.
        """
        utc_start = utc_end = None
        if start is not None:
            utc_start = to_time_query_param(start)
            if end is None:
                # If is not a string, set 1 minute for the end
                if not isinstance(utc_start, str):
                    utc_end = to_time_query_param(start) + 60.0
            else:
                utc_end = to_time_query_param(end)

        if utc_start is not None:
            params['utc_start'] = utc_start

        if utc_end is not None:
            params['utc_end'] = utc_end

        if topics is not None:
            params["topics"] = json.dumps(topics)

        params["pagination"] = True
        params["pagination_direction"] = direction

        def _choose_utc_time(a, b):
            if not a or isinstance(a, str):
                return b
            else:
                return a

        while True:
            result = self.api.call(
                "GET",
                "/accounts/{}/devices/{}/data/".format(self.account, self._id),
                params=params,
                **api_call_kwargs
            )

            # sort messages in case server returns messages in wrong order
            # (not sure if necessary but API doc doesn't seem to guarantee it)
            if direction == "forward":
                result["messages"].sort(key=lambda item: item.get("utc_time", 0.0))
            else:
                result["messages"].sort(key=lambda item: item.get("utc_time", 0.0), reverse=True)

            if result is None or len(result["messages"]) == 0:
                if loop:
                    # If no results and we are looping, we should start over
                    params['utc_start'] = _choose_utc_time(utc_start, result['requested_utc_start'])
                    params['utc_end'] = _choose_utc_time(utc_end, result['requested_utc_end'])
                    continue
                else:
                    return

            logger.debug("fetched %d of %d messages" % (
                result.get("returned_num_messages", -1), result.get("requested_num_messages", -1)
            ))

            for item in result.get("messages", {}):
                logger.debug("item: ", item)
                yield item

            returned_period = result["returned_utc_end"] - result["returned_utc_start"]

            if direction == "forward":
                params["utc_start"] = result["returned_utc_end"]
                params["utc_end"] = min(
                    params['utc_start'] + 1.1 * returned_period,
                    _choose_utc_time(utc_end, result['requested_utc_end'])
                )
            elif direction == "backward":
                params["utc_end"] = result["returned_utc_start"]
                params["utc_start"] = max(
                    params['utc_end'] - 1.1 * returned_period,
                    _choose_utc_time(utc_start, result['requested_utc_start'])
                )
            # if start reaches end value, we finish (or start over if loop)
            if params['utc_start'] == params['utc_end']:
                if loop:
                    # if we have set an end, start over, otherwise continue asking
                    # for new data
                    if utc_end:
                        params['utc_start'] = utc_start
                        params['utc_end'] = utc_end
                    else:
                        params.pop('utc_end', None)
                else:
                    return

    def data_last(self, topics=None, params=None, api_call_kwargs={}):
        """Returns the last message published by the device, as long as it is within the past 1 minute.

        Args:
            topics (`list` of `str`): Topics of interest.
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        if params is None:
            params = {}
        params["one_message_per_topic"] = "true"
        params["utc_start"] = to_unix_time(time.time() - 60.0)
        params["utc_end"] = to_unix_time(time.time())

        if topics is not None:
            params["topics"] = json.dumps(topics)

        result = self.api.call(
            "GET",
            "/accounts/{}/devices/{}/statistics/".format(self.account, self._id),
            params=params,
            **api_call_kwargs
        )

        if result is None or len(result) == 0:
            return None

        # sort messages in case server returns messages in wrong order
        # (not sure if necessary but API doc doesn't seem to guarantee it)
        result.sort(key=lambda item: item.get("utc_time", 0.0))

        return result[-1]

    def get_alerts(self, attributes=None, params=None, api_call_kwargs={}):
        """:obj:`list` of :obj:`Alert`: Fetch a list of alerts for the device, according to the used params

        Args:
            attributes (list): Optional list of attributes to request.
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        alerts = get_alerts(
            self.api,
            self.account,
            device_id=self._id,
            attributes=attributes,
            params=params,
            device_name=self.name,
            api_call_kwargs=api_call_kwargs,
        )
        return alerts

    def get_statistics(self, utc_start=None, utc_end=None, params=None, api_call_kwargs={}):
        """GET statistics endpoint abstraction.

        Args:
            utc_start (float): Returns statistics starting from the specified timestamp.
                       If null, returns the API default range (1 day).
            utc_end (float): Returns statistics until the specified timestamp (inclusive).
                       If null, returns the statistics until current hour.
            params (dict): Extra parameters that could be included in the request.
            api_call_kwargs (dict): Optional keyword arguments for api call.

        Returns:
            Dictionary with utc timestamp hourly rounded as keys, and the calculated statistics
            for each hour.
            Note: The current hour will always return a partial result that might have a couple of
                  minutes of delay depending on the statistic type.
        """

        if params is None:
            params = {}
        if utc_start is not None:
            params["utc_start"] = utc_start
        if utc_end is not None:
            params["utc_end"] = utc_end

        result = self.api.call(
            "GET",
            "/accounts/{}/devices/{}/statistics/".format(self.account, self._id),
            params=params,
            **api_call_kwargs
        )
        return result

    def put_statistics(self, data, params=None, api_call_kwargs={}):
        """PUT statistics endpoint abstraction

        Args:
            data (list): List with dictionaries with statistics values per hour.
            More info about the object format can be found on API docs:
            https://docs.freedomrobotics.ai/reference#rest-api
            params (dict): Extra parameters that could be included in the request.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        self.api.call(
            "PUT",
            "/accounts/{}/devices/{}/statistics/".format(self.account, self._id),
            data=data,
            params=params,
            **api_call_kwargs
        )
