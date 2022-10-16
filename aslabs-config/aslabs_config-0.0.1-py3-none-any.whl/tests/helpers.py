import os
import json
from contextlib import contextmanager
from unittest.mock import patch
from tempfile import TemporaryDirectory


@contextmanager
def mocked_env_variables(env_vars: dict):
    with patch.dict(os.environ, env_vars):
        yield


@contextmanager
def mocked_config_file(config_file_values: dict):
    with TemporaryDirectory() as tmpdir:

        config_path = os.path.join(tmpdir, "config.json")
        with open(config_path, "w") as f:
            json.dump(config_file_values, f)

        yield config_path

@contextmanager
def mocked_dotenv_file(config_file_values: dict):
    with TemporaryDirectory() as tmpdir:

        config_path = os.path.join(tmpdir, ".env")
        with open(config_path, "w") as f:
            for key, value in config_file_values.items():
                f.write(f"{key.upper()}=\"{value}\"\n")

        yield config_path