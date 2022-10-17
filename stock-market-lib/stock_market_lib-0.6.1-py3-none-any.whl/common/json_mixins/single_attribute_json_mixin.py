import json


class SingleAttributeJsonMixin:
    def to_json(self):
        return json.dumps(getattr(self, self.JSON_ATTRIBUTE_NAME))

    @classmethod
    def from_json(cls, json_str):
        return cls(json.loads(json_str))

    @classmethod
    def json_schema(cls):
        return {"type": cls.JSON_ATTRIBUTE_TYPE}
