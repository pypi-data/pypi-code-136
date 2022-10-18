from pathlib import Path
from typing import Any


def dict_to_sphinxconf(config: dict[str, Any]):
    ...


def toml_to_sphinxconf(tomlfile: Path):
    data = toml_to_doc(tomlfile)
    return dict_to_sphinxconf(data)
