import time

from .api_handler import default_api


class Entity(object):
    """Base entity abstraction with common methods to update and push data the the API
    """
    pk = None

    def __init__(self, _id, _data=None, api=None, update_threshold=30):
        """Base entity initialization

        Args:
            _id (str): Entity ID.
            _data (dict): Entity's data.
            api (APIHandler): API object for performing requests.
            update_threshold (int): Update threshold to auto-update data when accessing _data
                object. By default is 30, which means that data retrieved by the object won't
                be older than 30 secs. If set to None, then auto-update functionality is disabled,
                returning always the same data when the object was created.
        """
        self._id = _id
        self._data = _data
        self._last_updated = None
        self._update_threshold = update_threshold
        if api is None:
            api = default_api
        self.api = api
        if _data is None:
            self.update()
        else:
            self._last_updated = time.time()

    @property
    def url_base(self):
        """Makes the base url for each entity and uses it for api requests.
        This URL will be used for GET (entities listings) and POST requests.
        Needs to be overwritten on each subclass.

        E.g for devices: /accounts/A1234/devices
        """
        raise NotImplementedError()

    @property
    def url_id(self):
        """Makes the url with the Entity id for each entity and uses it for api requests.
        This URL will be used for GET (entity attributes) and PUT requests.
        Needs to be overwritten on each subclass

        E.g for devices: /accounts/A1234/devices/D1234
        """
        return '{}/{}'.format(self.url_base, self._id)

    def should_update(self):
        if self._update_threshold is None:
            return False
        return (
            self._last_updated is None or
            time.time() - self._last_updated > self._update_threshold
        )

    def __getitem__(self, key):
        if self.should_update():
            self.update()
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value
        self.push({key: value})

    def get(self, key, default=None):
        """Gets an attribute by key, and returns the default if not present
        """
        if self.should_update():
            self.update()
        return self._data.get(key, default)

    def push(self, data=None, api_call_kwargs={}):
        """Push current data to the API. For updating only specific fields, use data argument.

        Args:
            data (dict): Optional data to push, otherwise will use current data.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        if data is None:
            data = self._data
        self.api.call("PUT", self.url_id, data=data, **api_call_kwargs)

    def update(self, api_call_kwargs={}):
        """Synchronizes device properties with the Freedom API server.

        Args:
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """
        self._data = self.api.call("GET", self.url_id, **api_call_kwargs)
        self._last_updated = time.time()

    def __repr__(self):
        return "<{}: {} {}>".format(
            self.__class__.__name__,
            self._id,
            self._data.get("name", "")
        )

    def __eq__(self, obj):
        return isinstance(obj, self.__class__) and obj._id == self._id
