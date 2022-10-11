# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from threading import Lock
from urllib.parse import urlparse

import redis

from trytond.cache import BaseCache, MemoryCache
from trytond.cache_serializer import pack, unpack
from trytond.config import config
from trytond.transaction import Transaction


class RedisCache(BaseCache):
    _client = None
    _client_check_lock = Lock()
    _ttl = config.getint('cache', 'redis_ttl') or 60 * 60 * 12

    def __init__(self, name, size_limit=1024, duration=_ttl, context=True):
        super().__init__(
            name, size_limit=size_limit, duration=duration, context=context)
        self.ensure_client()

    @classmethod
    def ensure_client(cls):
        with cls._client_check_lock:
            if cls._client is None:
                redis_uri = config.get('cache', 'redis_uri')
                assert redis_uri, 'redis uri not set'
                url = urlparse(redis_uri)
                assert url.scheme == 'redis', 'invalid redis url'
                host = url.hostname
                port = url.port
                db = url.path.strip('/')
                cls._client = redis.StrictRedis(host=host, port=port, db=db)

    def _namespace(self, dbname=None):
        if dbname is None:
            dbname = Transaction().database.name
        return '%s:%s' % (dbname, self._name)

    def _key(self, key):
        k = super(RedisCache, self)._key(key)
        return '%x' % hash(k)

    def get(self, key, default=None):
        namespace = self._namespace()
        key = self._key(key)
        result = self._client.get('%s:%s' % (namespace, key))
        inst = self._instances[self._name]
        if result is None:
            inst.miss += 1
            return default
        else:
            inst.hit += 1
            return unpack(result)

    def set(self, key, value, ttl=None):
        if ttl:
            assert isinstance(ttl, int)
        if self.duration:
            ttl = self.duration.seconds
        namespace = self._namespace()
        key = self._key(key)
        value = pack(value)
        self._client.setex(name='%s:%s' % (namespace, key), value=value,
            time=ttl or self._ttl)

    def clear(self):
        dbname = Transaction().database.name
        namespace = self._namespace(dbname)
        keys = self._client.keys('%s:*' % (namespace))
        if keys:
            self._client.delete(*keys)

    # TODO: Transactional Cache
    # https://discuss.tryton.org/t/transactional-cache/1012
    @classmethod
    def sync(cls, transaction):
        pass

    # redis cache is synced immediately
    # https://github.com/tryton/trytond/commit/9c7f4753221d8f5a8252b36d080e49bc54b9ef1d
    def sync_since(self, value):
        return False

    @classmethod
    def commit(cls, transaction):
        pass

    @classmethod
    def rollback(cls, transaction):
        pass

    @classmethod
    def drop(cls, dbname):
        keys = cls._client.keys('%s:*' % (dbname))
        if keys:
            cls._client.delete(*keys)

    @classmethod
    def refresh_pool(cls, transaction):
        '''
        Use the method from MemoryCache
        '''
        MemoryCache.refresh_pool(transaction)

    #@classmethod
    #def _listen(cls, dbname):
    #    '''
    #    Use the method from MemoryCache
    #    '''
    #    MemoryCache._listen(dbname)
