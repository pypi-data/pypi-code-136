"""
"""
import copy
import dotted
import random
from join import base


class DB:
    db = {}
    def get(self, path):
        n = self.db
        for p in path:
            n = n.get(p)
            if not isinstance(n, dict):
                return None
        return copy.deepcopy(n)
    def put(self, path, obj):
        n = self.db
        for p in path[:-1]:
            n = n.setdefault(p, {})
        n[path[-1]] = copy.deepcopy(obj)
    def delete(self, path):
        n = self.db
        for p in path[:-1]:
            n = n.get(p)
            if not isinstance(p, dict):
                return
        del n[path[-1]]


db = DB()


class Key:
    MAX_INT_ID = 1 << 32
    def __init__(self, kind, id=None, parent=None):
        self.kind = kind
        self.id = id
        self.parent = parent
    def raw_path(self):
        p = ()
        if self.parent is not None:
            p += self.parent.raw_path()
        p += (self.kind, self.id)
        return p
    def __repr__(self):
        s = ', '.join(repr(p) for p in self.raw_path())
        return f'<{s}>'
    def is_partial(self):
        return self.id is None or (self.parent is not None and self.parent.is_partial())
    @property
    def path(self):
        assert not self.is_partial(), 'Partial key'
        return self.raw_path()
    def __hash__(self):
        return hash(self.path)
    def __eq__(self, other):
        return self.path == other.path
    def allocate(self):
        while True:
            self.id = random.randint(1, self.MAX_INT_ID)
            if db.get(self.path) is None:
                break
    def precommit(self):
        if self.parent is not None:
            self.parent.precommit()
        if self.id is None:
            self.allocate()
        return self


class Entity(dict):
    def __init__(self, key):
        self.key = key
    def __repr__(self):
        return f'{self.key}' + super().__repr__()


class Client:
    def get(self, key):
        return db.get(key.path)
    def get_multi(self, keys):
        items = (self.get(k) for k in keys)
        return [o for o in items if o is not None]
    def put(self, obj):
        key = obj.key.precommit()
        return db.put(key.path, obj)
    def put_multi(self, objs):
        for obj in objs:
            self.put(obj)


class MemDB(base.Join):
    GROUPSIZE = 500
    def is_key(self, obj):
        return isinstance(obj, Key)
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
        return client.get_multi(keys)


join = MemDB()


def test_join():
    client = Client()

    obj1 = Entity(Key('Test', 1))
    obj2 = Entity(Key('Test', 2))
    obj3 = Entity(Key('Test', 3))

    obj1['foo'] = 'root'
    obj1['ref'] = obj2.key

    obj2['foo'] = 'mid'
    obj2['ref'] = obj3.key

    obj3['foo'] = 'leaf'

    client.put(obj3)
    client.put(obj2)
    client.put(obj1)

    # this will find obj2 at obj1 ref
    obj = client.get(Key('Test', 1))
    found = next(join(client, [obj], ('ref',)))
    assert found['ref'].key == Key('Test', 2)

    # this will replace obj with obj3
    obj = client.get(Key('Test', 1))
    found = next(join(client, [obj], ('!ref',)))
    assert found.key == Key('Test', 3)

    # this will recursively chain obj1 to have all linked refs
    obj = client.get(Key('Test', 1))
    found = next(join(client, [obj], ('+ref',)))
    assert found.key == Key('Test', 1)
    assert found['ref'].key == Key('Test', 2)
    assert found['ref']['ref'].key == Key('Test', 3)
    assert found['ref']['ref']['foo'] == 'leaf'


def test_no_key():
    client = Client()

    obj1 = Entity(Key('Test', 1))
    client.put(obj1)

    # test no-keyed objs
    found = list(join(client, [{'ref': Key('Test', 1)}], 'ref'))
    assert found[0]['ref'] == obj1


def test_limit():
    client = Client()

    objs = [Entity(Key('Test', 1)), Entity(Key('Test', 2)), Entity(Key('Test', 3))]
    client.put_multi(objs)

    objs = join(client, objs, (), limit=2)
    assert len(list(objs)) == 2


def test_filter():
    client = Client()

    objs = [Entity(Key('Test', 1)), Entity(Key('Test', 2)), Entity(Key('Test', 3))]
    client.put_multi(objs)

    def _filter(obj):
        return obj.key != Key('Test', 2)

    objs = join(client, objs, (), filter=_filter)
    assert len(list(objs)) == 2
