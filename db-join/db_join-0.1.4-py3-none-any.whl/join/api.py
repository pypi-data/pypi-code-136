"""
Join api
"""
import dotted
from . import base


#
# datastore-specific join
#
class DatastoreJoin(base.Join):
    GROUPSIZE = 500

    def is_key(self, obj):
        from google.cloud import datastore
        return isinstance(obj, datastore.Key)

    def obj2key(self, obj):
        return getattr(obj, 'key', None)

    def is_expandable(self, obj, scopes):
        key = getattr(obj, 'key', obj)
        if not self.is_key(key):
            return False
        if not scopes:
            return True
        pattern = '.'.join(reversed(scopes))
        path = '.'.join(reversed(key.flat_path[::2]))
        return dotted.match(pattern, path)

    def get_multi(self, client, keys, **kwargs):
        return client.get_multi(keys, **kwargs)
