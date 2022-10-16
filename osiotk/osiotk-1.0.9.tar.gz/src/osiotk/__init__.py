import os as _os
import json as _json
from collections import defaultdict as _defaultdict
from typing import Callable


def __system(__command: str):
    return _os.system(command=__command)


def __join_paths(__name, branch):
    return _os.path.join(__name, branch)


def __abspath(__name: str, is_abspath: bool = False):
    return __name if is_abspath else _os.path.abspath(__name)


def __basename(__name: str):
    return __name.split("/")[-1] if "/" in __name else __name


def __reads(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    with open(path, mode="r") as file:
        result = file.read()
    return result


def __readb(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    with open(path, mode="rb") as file:
        result = file.read()
    return result


def __readjson(__name: str, is_abspath: bool = False):
    return _json.loads(__reads(__name, is_abspath=is_abspath))


def __readlines(
    __name: str,
    is_abspath: bool = False,
    keepends: bool = False,
    where: Callable[[str], bool] = None,
):
    s = __reads(__name, is_abspath)
    result = s.splitlines(keepends=keepends)
    if where is not None:
        result = [line for line in result if where(line)]
    return result


def __writes(
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


def __writeb(
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


def __writejson(__name: str, content, indent: int = 4, is_abspath: bool = False):
    s = _json.dumps(content, indent=indent)
    return __writes(__name, content=s, is_abspath=is_abspath)


def __scandir(__name: str, is_abspath: bool, where: Callable[[object], bool] = None):
    path = __abspath(__name, is_abspath)
    result = _os.scandir(path=path)
    if where is not None:
        result = (file for file in result if where(file))
    return result


def __isfile(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return _os.path.isfile(path)


def __isdir(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return _os.path.isdir(path)


def __exists(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return _os.path.exists(path)


def __file_exists(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return __exists(path, is_abspath=True) and __isfile(path, is_abspath=True)


def __dir_exists(__name: str, is_abspath: bool = False):
    path = __abspath(__name, is_abspath)
    return __exists(path, is_abspath=True) and __isdir(path, is_abspath=True)


def __mkdir(__name: str, is_abspath: bool = False, exist_ok: bool = True):
    path = __abspath(__name, is_abspath)
    if not dir_exists(path, is_abspath=True):
        _os.makedirs(path, exist_ok=exist_ok)


def __mkfile(__name: str, is_abspath: bool = False):
    if not __file_exists(__name, is_abspath=is_abspath):
        __writes(__name, content="", is_abspath=is_abspath)


def __mk_filetree(__ft: str, overwrite_if_exists: bool = False):
    def filetree_paths(__ft: str) -> list[str]:
        dirlog, results = _defaultdict(list[str]), []
        for line in (line for line in __ft.splitlines(keepends=False) if line):
            offset, path = len(line) - len(line.lstrip()), line.strip()
            dirlog[offset].append(path)
            while offset > 0:
                if dirlog[offset - 4]:
                    path = f"{dirlog[offset-4][-1]}/{path}"
                offset -= 4
            results.append(path)
        return results

    ft_paths = filetree_paths(__ft)

    dirpaths = set(
        path
        for path in ft_paths
        if (
            next(
                (
                    ft_path
                    for ft_path in ft_paths
                    if (ft_path.startswith(f"{path}/") and ft_path != path)
                ),
                None,
            )
            is not None
        )
        and not "." in __basename(path)
    )

    for path in ft_paths:
        if path in dirpaths:
            __mkdir(path)
        else:
            if __exists(path):
                if overwrite_if_exists:
                    __writes(path, content="")
            else:
                __mkfile(path)


def system(__command: str):
    return __system(__command)


def join_paths(__base, branch):
    return __join_paths(__base, branch)


def abspath(__name: str, is_abspath: bool = False):
    return __abspath(__name, is_abspath=is_abspath)


def basename(__name: str):
    return __basename(__name)


def scandir(__name: str, is_abspath: bool, where: Callable[[object], bool] = None):
    return __scandir(__name, is_abspath=is_abspath, where=where)


def isfile(__name: str, is_abspath: bool = False):
    return __isfile(__name, is_abspath=is_abspath)


def isdir(__name: str, is_abspath: bool = False):
    return __isdir(__name, is_abspath)


def exists(__name: str, is_abspath: bool = False):
    return __exists(__name, is_abspath)


def file_exists(__name: str, is_abspath: bool = False):
    return __file_exists(__name, is_abspath)


def dir_exists(__name: str, is_abspath: bool = False):
    return __dir_exists(__name, is_abspath)


def mkdir(__name: str, is_abspath: bool = False, exist_ok: bool = True):
    return __mkdir(__name, is_abspath=is_abspath, exist_ok=exist_ok)


def mkfile(__name: str, is_abspath: bool = False):
    return __mkfile(__name, is_abspath)


def reads(__name: str, is_abspath: bool = False):
    return __reads(__name, is_abspath)


def readb(__name: str, is_abspath: bool = False):
    return __readb(__name, is_abspath)


def readjson(__name: str, is_abspath: bool = False):
    return __readjson(__name, is_abspath)


def readlines(
    __name: str,
    is_abspath: bool = False,
    keepends: bool = False,
    where: Callable[[str], bool] = None,
):
    return __readlines(__name, is_abspath=is_abspath, keepends=keepends, where=where)


def writes(
    __name: str,
    content: str,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    return __writes(
        __name, content=content, is_abspath=is_abspath, errors=errors, encoding=encoding
    )


def writeb(
    __name: str,
    content: bytes,
    is_abspath: bool = False,
    errors: str = "ignore",
    encoding: str = "utf-8",
):
    return __writeb(
        __name, content=content, is_abspath=is_abspath, errors=errors, encoding=encoding
    )


def writejson(__name: str, content, indent: int = 4, is_abspath: bool = False):
    return __writejson(__name, content=content, indent=indent, is_abspath=is_abspath)


def mk_filetree(__ft: str,overwrite_if_exists:bool=False):
    return __mk_filetree(__ft,overwrite_if_exists)
