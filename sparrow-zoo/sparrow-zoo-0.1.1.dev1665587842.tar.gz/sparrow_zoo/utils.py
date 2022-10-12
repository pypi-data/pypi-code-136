"""Model utilities."""
from pathlib import Path
from typing import Union

SUFFIXES: tuple[str, ...] = (".json.gz", ".json", ".jpg", ".jpeg", ".png")


def get_slug(path: Union[str, Path], suffixes: tuple[str, ...] = SUFFIXES) -> str:
    """Get the slug (filename without extension suffix) for a path."""
    path = Path(path)
    filename = path.name
    for suffix in suffixes:
        filename = filename.removesuffix(suffix)
    return filename
