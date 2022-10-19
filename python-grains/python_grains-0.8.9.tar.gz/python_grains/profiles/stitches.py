import json
import datetime
import pytz

DEFAULT_DOMAIN = None
DEFAULT_REDIS_CLIENT = None
DEFAULT_DJANGO_STITCH_POOL_MODEL = None
DEFAULT_DJANGO_STITCH_MODEL = None
DEFAULT_DJANGO_CONNECTION_TUPLE = (None, None)
DEFAULT_USER_TTL = 6 * 24 * 60 * 60
DEFAULT_USER_DATA_TTL_MARGIN = 2
DEFAULT_MAX_STITCH_KEYS = 50

class StitchPool(object):

    recently_checked_db_postfix = ':rc'
    domain = DEFAULT_DOMAIN
    redis_client = DEFAULT_REDIS_CLIENT
    django_stitch_pool_model = DEFAULT_DJANGO_STITCH_POOL_MODEL
    user_ttl = DEFAULT_USER_TTL
    user_data_ttl_margin = DEFAULT_USER_DATA_TTL_MARGIN
    django_connection_tuple = DEFAULT_DJANGO_CONNECTION_TUPLE

    def __init__(self,
                 user_id,
                 stitch_keys=None,
                 recently_checked_db=None):

        self.user_id = user_id
        self.stitch_keys = set()
        self._recently_checked_db = recently_checked_db

        if stitch_keys:
            self.add_stitch_keys(stitch_keys)

        if self.domain is None:
            raise ValueError('domain should not be None')

        if self.redis_client is None:
            raise ValueError('redis_client should not be None')

    def add_stitch_keys(self,
                        stitch_keys):

        assert isinstance(stitch_keys, (list, set)), 'stitch_keys needs to be a list or set'
        self.stitch_keys = self.stitch_keys.union(set(stitch_keys))

    def to_cache(self):

        now = pytz.utc.localize(datetime.datetime.utcnow()).timestamp()
        pipe = self.redis_client.pipeline()
        pipe.zadd(self.key, {s: now for s in self.stitch_keys})
        pipe.expire(self.key, self.user_ttl + self.user_data_ttl_margin)
        pipe.execute()

    def get(self):

        stitch_keys = [s.decode() for s in self.redis_client.zrangebyscore(self.key, min='-inf', max='+inf')]
        self.add_stitch_keys(stitch_keys)
        if not self.recently_checked_db:
            self.complement_from_db()

    def complement_from_db(self):

        try:
            stitch_pool_model = self.django_stitch_pool_model.objects.get(user_id=self.user_id)
            stitches_keys = [str(s) for s in stitch_pool_model.stitch_keys]
            self.add_stitch_keys(stitches_keys)
            if len(stitches_keys) > 0:
                self.to_cache()
            self.set_recent_db_check()
        except self.django_stitch_pool_model.DoesNotExist:
            self.set_recent_db_check()
            return []

    @property
    def recently_checked_db(self):
        if self._recently_checked_db is None:
            self._recently_checked_db = bool(self.redis_client.get(self.recently_checked_db_key))
        return self._recently_checked_db

    @property
    def key(self):
        return self._key(user_id=self.user_id)

    @classmethod
    def _key(cls,
             user_id):
        # this is also defined on the profile class in python-grains!
        return f'st:u:p:{cls.domain}:{user_id}'

    @property
    def recently_checked_db_key(self):
        return self._recently_checked_db_key(user_id=self.user_id)

    @classmethod
    def _recently_checked_db_key(cls,
                                 user_id):
        return cls._key(user_id=user_id) + cls.recently_checked_db_postfix

    def set_recent_db_check(self):
        self.redis_client.set(self.recently_checked_db_key, "1", ex=self.user_ttl)

class Stitch(object):

    default_type = 'default'
    recently_checked_db_postfix = ':rc'
    domain = DEFAULT_DOMAIN
    redis_client = DEFAULT_REDIS_CLIENT
    user_ttl = DEFAULT_USER_TTL
    user_data_ttl_margin = DEFAULT_USER_DATA_TTL_MARGIN
    django_stitch_model = DEFAULT_DJANGO_STITCH_MODEL
    django_connection_tuple = DEFAULT_DJANGO_CONNECTION_TUPLE
    max_stitch_keys = DEFAULT_MAX_STITCH_KEYS

    def __init__(self,
                 value,
                 type,
                 user_ids=None,
                 recently_checked_db=None):

        self.type = (type or self.default_type).lower()
        self.value = value
        self.user_ids = set()
        self._recently_checked_db = recently_checked_db

        if user_ids:
            self.add_user_ids(user_ids)

        if self.domain is None:
            raise ValueError('domain should not be None')

        if self.redis_client is None:
            raise ValueError('redis_client should not be None')

    def add_user_ids(self,
                     user_ids):

        assert isinstance(user_ids, (list, set)), 'user_ids needs to be a list or set'
        self.user_ids = self.user_ids.union(set(user_ids))

    def to_cache(self):
        now = pytz.utc.localize(datetime.datetime.utcnow()).timestamp()
        pipe = self.redis_client.pipeline()
        pipe.zadd(self.key, {u: now for u in self.user_ids})
        pipe.expire(self.key, self.user_ttl + self.user_data_ttl_margin)
        pipe.execute()

    def get(self):
        user_ids = [u.decode() for u in self.redis_client.zrangebyscore(self.key, min='-inf', max='+inf')]
        self.add_user_ids(user_ids)
        if not self.recently_checked_db:
            self.complement_from_db()

    def remove_user_ids(self,
                        user_ids):

        assert isinstance(user_ids, (list, set)), 'user_ids needs to be a list or set'
        self.redis_client.zrem(*user_ids)
        self.user_ids = self.user_ids - set(user_ids)

    def set_recent_db_check(self):

        self.redis_client.set(self.recently_checked_db_key, "1", ex=self.user_ttl)

    @property
    def recently_checked_db(self):

        if self._recently_checked_db is None:
            self._recently_checked_db = bool(self.redis_client.get(self.recently_checked_db_key))
        return self._recently_checked_db

    @classmethod
    def get_multiple(cls,
                     keys):

        data = cls.redis_client.get_multiple_stitches(
            keys=[],
            args=[
                json.dumps(list(set(keys))),
                cls.recently_checked_db_postfix
            ]
        )
        data_dict = {k.decode(): cls.from_redis_data(key=k, data=dict(zip(v[::2], v[1::2])))
                     for k,v in dict(zip(data[::2], data[1::2])).items()}
        should_check_db = {k: v for k,v in data_dict.items() if not v.recently_checked_db}
        checked_in_db = cls.complement_multiple_from_db(should_check_db)
        data_dict.update(checked_in_db)

        return list(data_dict.values())


    @classmethod
    def complement_multiple_from_db(cls, should_check_dict):

        stitch_models = list(cls.django_stitch_model.objects.filter(key__in=list(should_check_dict.keys())))
        for stitch_model in stitch_models:
            should_check_dict[stitch_model.key] = should_check_dict[stitch_model.key].add_user_ids(
                [str(u) for u in stitch_model.user_ids]
            )
            should_check_dict[stitch_model.key].to_cache()
            should_check_dict[stitch_model.key].set_recent_db_check()

        return should_check_dict

    def complement_from_db(self):
        try:
            stitch_model = self.django_stitch_model.objects.get(key=self.key)
            user_ids = [str(u) for u in stitch_model.user_ids]
            self.add_user_ids(user_ids)
            if len(user_ids) > 0:
                self.to_cache()
            self.set_recent_db_check()
        except self.django_stitch_model.DoesNotExist:
            self.set_recent_db_check()
            return []

    def as_dict(self):
        return {
            'value': self.value,
            'type': self.type
        }

    @classmethod
    def from_redis_data(cls,
                        key,
                        data):

        type, value, domain = cls.parse_key(key)
        user_ids = [u.decode() for u in (data[b'user_ids'] or [])]
        checked_db = bool(data[b'recent_check'])
        return cls(value=value, type=type, user_ids=user_ids, recently_checked_db=checked_db)


    @classmethod
    def parse_key(cls, key):

        key = key.decode() if isinstance(key, bytes) else key
        split_key = key.split(':')
        type, value, domain = split_key[2], ':'.join(split_key[3:-1]), split_key[-1]
        return type, value, domain

    @property
    def key(self):
        return self._key(type=self.type, value=self.value)

    @classmethod
    def _key(cls, type, value):
        return f'st:u:{type}:{value}:{cls.domain}'

    @property
    def recently_checked_db_key(self):
        return self._recently_checked_db_key(type=self.type, value=self.value)

    @classmethod
    def _recently_checked_db_key(cls, type, value):
        return cls._key(type=type, value=value) + cls.recently_checked_db_postfix