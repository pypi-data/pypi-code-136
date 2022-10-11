import json

from jsonschema import validate


class Factory:
    def __init__(self):
        self.creator_map = {}

    def register(self, name, creator, schema):
        assert name not in self.creator_map, str((self.creator_map, name))
        self.creator_map[name] = (creator, schema)
        return self

    def create(self, name, config):
        assert name in self.creator_map, str((self.creator_map, name))
        creator, schema = self.creator_map[name]
        validate(instance=json.loads(config), schema=schema)

        return creator(config)

    def get_registered_names(self):
        return self.creator_map.keys()

    def get_schema(self, name):
        assert name in self.creator_map, str((self.creator_map, name))
        return self.creator_map[name][1]
