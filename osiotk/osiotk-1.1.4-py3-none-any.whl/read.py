from . import base as _base
from typing import Callable
from json import loads as _loads


def string(__name: str, is_abspath: bool = False):
    path = _base.abspath(__name, is_abspath)
    with open(path, mode="r") as file:
        result = file.read()
    return result


def bytes(__name: str, is_abspath: bool = False):
    path = _base.abspath(__name, is_abspath)
    with open(path, mode="rb") as file:
        result = file.read()
    return result


def json(__name: str, is_abspath: bool = False):
    return _loads(string(__name, is_abspath=is_abspath))


def lines(
    __name: str,
    is_abspath: bool = False,
    keepends: bool = False,
    where: Callable[[str], bool] = None,
):
    s = string(__name, is_abspath)
    result = s.splitlines(keepends=keepends)
    if where is not None:
        result = [line for line in result if where(line)]
    return result
