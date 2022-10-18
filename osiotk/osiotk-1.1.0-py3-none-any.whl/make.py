import os as _os
from collections import defaultdict as _defaultdict
from . import base as _base
from . import write as _write
from . import exists_ as _exists


def dir(__name: str, is_abspath: bool = False, exist_ok: bool = True):
    path = _base.abspath(__name, is_abspath)
    if not _exists.dir(path, is_abspath=True):
        _os.makedirs(path, exist_ok=exist_ok)


def file(__name: str, is_abspath: bool = False):
    if not _exists.file(__name, is_abspath=is_abspath):
        _write.string(__name, content="", is_abspath=is_abspath)


def filetree(__ft: str, overwrite_if_exists: bool = False):
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
        and not "." in _base.basename(path)
    )
    for dirpath in dirpaths:
        dir(dirpath, is_abspath=True)

    for path in ft_paths:
        if not path in dirpaths:
            if _exists.file(path):
                if overwrite_if_exists:
                    _write.string(path, content="")
            else:
                file(path)
