from pathlib import Path
from typing import Union

PathLike = Union[str, Path]


def local_to_absolute_path(path: PathLike) -> str:
    return str(Path(path).resolve().absolute())
