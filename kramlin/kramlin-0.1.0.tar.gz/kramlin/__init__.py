from django.conf import settings
from django.core.cache import caches

MANAGER_CACHE_NAME = (
    settings.PLATFORM_MANAGE_CACHE_NAME if hasattr(settings, 'PLATFORM_MANAGE_CACHE_NAME') else 'platform_settings'
)


class BasePlatformManager:

    def __init__(self):
        pass

    @staticmethod
    def get_config():
        cache = caches["default"].get(MANAGER_CACHE_NAME)
        if cache:
            return cache

    @staticmethod
    def set_config(obj):
        caches["default"].set(MANAGER_CACHE_NAME, obj, timeout=None)

    @staticmethod
    def get_val(obj, key, default=None):
        if (
            obj and (
                (type(obj) == dict and key in obj)
                or (type(obj) == object and hasattr(obj, key))
            ) and obj[key] is not None
        ):
            return obj[key]
        return default

    @staticmethod
    def get_if_val(val):
        if val and len(val) > 0:
            return val
        return None


__all__ = [
    'BasePlatformManager',
]
