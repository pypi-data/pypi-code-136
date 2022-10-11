import json


class EmptyJsonMixin:
    def to_json(self):
        return json.dumps("")

    @classmethod
    def from_json(cls, json_str):
        return cls()

    @classmethod
    def json_schema(cls):
        return {"type": "string"}
