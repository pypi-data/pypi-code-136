import sys

import six

from scrapy.utils.misc import load_object

from . import defaults


# Shortcut maps 'setting name' -> 'parmater name'.
# 快速映射settings配置文件中redis的基础配置字典
SETTINGS_PARAMS_MAP = {
    'REDIS_URL': 'url',
    'REDIS_HOST': 'host',
    'REDIS_PORT': 'port',
    'REDIS_DB': 'db',
    'REDIS_ENCODING': 'encoding',
}

if sys.version_info > (3,):
    SETTINGS_PARAMS_MAP['REDIS_DECODE_RESPONSES'] = 'decode_responses'


# 根据scrapy中settings配置文件信息返回一个redis客户端实例对象
def get_redis_from_settings(settings):
    """
        Returns a redis client instance from given Scrapy settings object.
        This function uses ``get_client`` to instantiate the client and uses
        ``defaults.REDIS_PARAMS`` global as defaults values for the parameters.
        You can override them using the ``REDIS_PARAMS`` setting.
    Parameters
        settings : Settings  A scrapy settings object. See the supported settings below.

    Returns
        server
            Redis client instance.

    Other Parameters
        REDIS_URL : str, optional  Server connection URL.
        REDIS_HOST : str, optional Server host.
        REDIS_PORT : str, optional Server port.
        REDIS_DB : int, optional Server database
        REDIS_ENCODING : str, optional Data encoding.
        REDIS_PARAMS : dict, optional Additional client parameters.

    Python 3 Only
    ----------------
    REDIS_DECODE_RESPONSES : bool, optional
        Sets the `decode_responses` kwarg in Redis cls ctor

    """
    params = defaults.REDIS_PARAMS.copy()
    params.update(settings.getdict('REDIS_PARAMS'))
    # XXX: Deprecate REDIS_* settings.
    for source, dest in SETTINGS_PARAMS_MAP.items():
        val = settings.get(source)
        if val:
            params[dest] = val

    # Allow ``redis_cls`` to be a path to a class.
    if isinstance(params.get('redis_cls'), six.string_types):
        params['redis_cls'] = load_object(params['redis_cls'])

    return get_redis(**params)


# Backwards compatible alias.
from_settings = get_redis_from_settings


# 返回一个redis的Strictredis实例对象
def get_redis(**kwargs):
    """
    Returns redis客户端实例.
    Parameters
        redis_cls : class, optional    默认值 ``redis.StrictRedis``.
        url : str, optional            If given, ``redis_cls.from_url`` is used to instantiate the class.
        **kwargs                       redis需要的参数 Extra parameters to be passed to the ``redis_cls`` class.
    Returns
        server
            Redis client instance.
    """
    # import redis
    # pool = redis.ConnectionPool(**kwargs)
    # self.rd = redis.Redis(connection_pool=pool)
    # 返回 redis.StrictRedis 类
    redis_cls = kwargs.pop('redis_cls', defaults.REDIS_CLS)
    # 取出 url
    url = kwargs.pop('url', None)
    if url:
        return redis_cls.from_url(url, **kwargs)
    else:
        return redis_cls(**kwargs)



