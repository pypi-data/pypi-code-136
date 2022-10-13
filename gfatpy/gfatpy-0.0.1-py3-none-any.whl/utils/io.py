from pathlib import Path
from typing import Any

import yaml


def read_yaml(path: Path | str) -> Any:
    """
    Reads a yaml file and returns the data as a dictionary.
    """
    with open(path, "r") as stream:
        return yaml.safe_load(stream)
