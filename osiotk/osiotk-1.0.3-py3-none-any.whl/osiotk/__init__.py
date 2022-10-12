import os as _os
import json as _json
from typing import Callable


def __join_paths(__name, branch):
    return _os.path.join(__name, branch)


def __abspath(__name: str, is_abspath: bool = False):
    return __name if is_abspath else _os.path.abspath(__name)

def __scandir(__name: str, is_abspath: bool, where: Callable[[object], bool] = None):
    path = __abspath(__name, is_abspath)
    result = _os.scandir(path=path)
    if where is not None:
        result = (file for file in result if where(file))
    return result


def join_paths(__base, branch):
    return __join_paths(__base, branch)


def abspath(__name: str,is_abspath:bool=False):
    return __abspath(__name,is_abspath=is_abspath)


def scandir(__name: str, is_abspath: bool, where: Callable[[object], bool] = None):
    return __scandir(__name, is_abspath=is_abspath, where=where)


def isfile(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return _os.path.isfile(path)


def isdir(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return _os.path.isdir(path)


def exists(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return _os.path.exists(path)


def file_exists(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return exists(path, is_abspath=True) and isfile(path, is_abspath=True)


def dir_exists(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return exists(path, is_abspath=True) and isdir(path, is_abspath=True)


def mkdir(__name: str, is_abspath: bool = False, exist_ok: bool = True):
    path = __abspath(__name, is_abspath)
    if not dir_exists(path, is_abspath=True):
        _os.makedirs(path, exist_ok=exist_ok)


def reads(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    with open(path, mode="r") as file:
        result = file.read()
    return result


def readb(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    with open(path, mode="rb") as file:
        result = file.read()
    return result


def readjson(__name: str, is_abspath: bool = False):
    return _json.loads(reads(__name, is_abspath=is_abspath))


def writes(
    __name: str,
    content: str,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    path = __abspath(__name, is_abspath)
    with open(path, "w+", errors=errors, encoding=encoding) as file:
        file.write(content)
        file.close()


def writeb(
    __name: str,
    content: bytes,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    path = __abspath(__name, is_abspath)
    with open(path, "w+", errors=errors, encoding=encoding) as file:
        file.write(content)
        file.close()


def writejson(__name: str, content, indent: int = 4, is_abspath: bool = False):
    s = _json.dumps(content, indent=indent)
    return writes(__name, content=s,is_abspath=is_abspath)
