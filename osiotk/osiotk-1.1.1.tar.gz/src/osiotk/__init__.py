from typing import Callable
from . import base as _base
from . import is_ as _is
from . import make as _mk
from . import read as _read
from . import exists_ as _exists
from . import write as _write


def system(__command: str):
    return _base.system(__command)


def join_paths(__base, branch):
    return _base.join_paths(__base, branch)


def abspath(__name: str, is_abspath: bool = False):
    return _base.abspath(__name, is_abspath=is_abspath)


def basename(__name: str):
    return _base.basename(__name)


def scandir(__name: str, is_abspath: bool, where: Callable[[object], bool] = None):
    return _base.scandir(__name, is_abspath=is_abspath, where=where)


def isfile(__name: str, is_abspath: bool = False):
    return _is.file(__name, is_abspath=is_abspath)


def isdir(__name: str, is_abspath: bool = False):
    return _is.dir(__name, is_abspath)


def exists(__name: str, is_abspath: bool = False):
    return _exists.node(__name, is_abspath)


def file_exists(__name: str, is_abspath: bool = False):
    return _exists.file(__name, is_abspath)


def dir_exists(__name: str, is_abspath: bool = False):
    return _exists.dir(__name, is_abspath)


def mkdir(__name: str, is_abspath: bool = False, exist_ok: bool = True):
    return _mk.dir(__name, is_abspath=is_abspath, exist_ok=exist_ok)


def mkfile(__name: str, is_abspath: bool = False):
    return _mk.file(__name, is_abspath)


def reads(__name: str, is_abspath: bool = False):
    return _read.string(__name, is_abspath)


def readb(__name: str, is_abspath: bool = False):
    return _read.bytes(__name, is_abspath)


def readjson(__name: str, is_abspath: bool = False):
    return _read.json(__name, is_abspath)


def readlines(
    __name: str,
    is_abspath: bool = False,
    keepends: bool = False,
    where: Callable[[str], bool] = None,
):
    return _read.lines(__name, is_abspath=is_abspath, keepends=keepends, where=where)


def writes(
    __name: str,
    content: str,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    return _write.string(
        __name, content=content, is_abspath=is_abspath, errors=errors, encoding=encoding
    )


def writeb(
    __name: str,
    content: bytes,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    return _write.bytes(
        __name, content=content, is_abspath=is_abspath, errors=errors, encoding=encoding
    )


def writejson(__name: str, content, indent: int = 4, is_abspath: bool = False):
    return _write.json(__name, content=content, indent=indent, is_abspath=is_abspath)


def mk_filetree(__ft: str, overwrite_if_exists: bool = False,indent:int=4):
    return _mk.filetree(__ft, overwrite_if_exists=overwrite_if_exists,indent=indent)
