import json
import os


def read_json(path: str):
    with open(path, "r") as f:
        return json.load(f)


def write_json(path: str, data):
    with open(path, "w") as f:
        f.write(json.dumps(data, default=str, indent=4))


def append_json(path: str, item: dict):
    if not os.path.exists(path):
        write_json(path, [item])
    else:
        items = read_json(path)
        assert type(items) == list
        items.append(item)
        write_json(path, items)
