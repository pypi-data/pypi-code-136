from . import base as _base
from json import dumps as _dumps


def string(
    __name: str,
    content: str,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    path = _base.abspath(__name, is_abspath)
    with open(path, "w+", errors=errors, encoding=encoding) as file:
        file.write(content)
        file.close()


def bytes(
    __name: str,
    content: bytes,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    path = _base.abspath(__name, is_abspath)
    with open(path, "w+", errors=errors, encoding=encoding) as file:
        file.write(content)
        file.close()


def json(__name: str, content, indent: int = 4, is_abspath: bool = False):
    s = _dumps(content, indent=indent)
    return string(__name, content=s, is_abspath=is_abspath)


def data(
    __name: str,
    content,
    indent: int = 4,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    if isinstance(content, str):
        result = string(
            __name,
            content=content,
            is_abspath=is_abspath,
            errors=errors,
            encoding=encoding,
        )
    else:
        result = json(__name, content=content, indent=indent, is_abspath=is_abspath)
    return result
