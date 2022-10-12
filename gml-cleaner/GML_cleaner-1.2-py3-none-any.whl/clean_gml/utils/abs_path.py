import os


def add_abspath(rel_path: str = None, file: str = None, dirlist: list = None) -> str:
    rel_path = os.path.abspath(os.path.dirname(rel_path))
    if dirlist is None:
        return os.path.join(rel_path, file)
    return os.path.join(rel_path, *dirlist, file)