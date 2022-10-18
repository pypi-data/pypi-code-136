import os as _os
from . import base as _base
from . import is_ as _is


def node(__name: str, is_abspath: bool = False):
    path = _base.abspath(__name, is_abspath)
    return _os.path.exists(path)


def file(__name: str, is_abspath: bool = False):
    path = _base.abspath(__name, is_abspath)
    return node(path, is_abspath=True) and _is.file(path, is_abspath=True)


def dir(__name: str, is_abspath: bool = False):
    path = _base.abspath(__name, is_abspath)
    return node(path, is_abspath=True) and _is.dir(path, is_abspath=True)
