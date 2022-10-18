import os as _os
from . import base as _base


def file(__name: str, is_abspath: bool = False):
    path = _base.abspath(__name, is_abspath)
    return _os.path.isfile(path)


def dir(__name: str, is_abspath: bool = False):
    path = _base.abspath(__name, is_abspath)
    return _os.path.isdir(path)
