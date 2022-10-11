"""
Provides a way to cache values.
"""
from datetime import date, datetime, timedelta


class CachedValue:
    """
    Represents a cached value with a time to live.
    """

    def __init__(self, ttl: timedelta):
        self._ttl = ttl
        self._value_expiration: date = None
        self._value = None

    def get_value(self, default=None):
        """
        Returns the cached value.
        """
        if self._value_expiration and self._value_expiration > datetime.utcnow():
            return self._value
        return default

    def set_value(self, value):
        """
        Sets the cached value.
        """
        self._value = value
        self._value_expiration = datetime.utcnow() + self._ttl

    def reset(self):
        """
        Resets the cached value.
        """
        self._value = None
        self._value_expiration = None
