import os as _os
from . import base as _base
from . import write as _write
from . import exists_ as _exists
from . import paths as _paths


def dir(__name: str, is_abspath: bool = False, exist_ok: bool = True):
    path = _base.abspath(__name, is_abspath)
    if not _exists.dir(path, is_abspath=True):
        _os.makedirs(path, exist_ok=exist_ok)


def file(__name: str, is_abspath: bool = False):
    if not _exists.file(__name, is_abspath=is_abspath):
        _write.string(__name, content="", is_abspath=is_abspath)


def filetree(__ft: str, overwrite_if_exists: bool = False,indent:int=4):

    ft_paths = _paths.filetree(__ft,indent=indent)

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
        dir(dirpath)

    for path in ft_paths:
        if not path in dirpaths:
            if _exists.file(path):
                if overwrite_if_exists:
                    _write.string(path, content="")
            else:
                file(path)
    

    for path in ft_paths:
        if not _exists.node(path):
            print(f"error: path does not exist:{path}")
