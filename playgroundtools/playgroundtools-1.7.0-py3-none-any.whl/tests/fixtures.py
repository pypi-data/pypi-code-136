import json

import pytest

from ..playgroundtools.resources import load_file_resource, load_text_resource


@pytest.fixture
def raw_config():
    """Represents the JSON-decoded config.json file."""
    result = load_text_resource("config.json")
    yield json.loads(result)

    with load_file_resource("config.json") as config_path:
        with open(config_path, "w") as f:
            f.write(result)
