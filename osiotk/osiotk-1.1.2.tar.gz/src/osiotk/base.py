import os as _os
from typing import Callable


def system(__command: str):
    return _os.system(command=__command)


def join_paths(__name, branch):
    return _os.path.join(__name, branch)


def abspath(__name: str, is_abspath: bool = False):
    return __name if is_abspath else _os.path.abspath(__name)


def basename(__name: str):
    return __name.split("/")[-1] if "/" in __name else __name


def scandir(__name: str, is_abspath: bool, where: Callable[[object], bool] = None):
    result = _os.scandir(__name, is_abspath=is_abspath)
    if where is not None:
        result = (file for file in result if where(file))
    return result


def parent_dir(__name: str, is_abspath: bool = False):
    path = abspath(__name, is_abspath=is_abspath)
    if "/" in path:
        path = "/".join(path.split("/")[:-1])
    return path
