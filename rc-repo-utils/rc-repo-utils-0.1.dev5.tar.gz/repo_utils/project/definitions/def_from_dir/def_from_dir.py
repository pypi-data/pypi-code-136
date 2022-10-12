import os

from repo_utils import import_from_path


def def_from_dir(path: str):
    """Return definition function or object at provided path"""
    if not path.endswith(".py"):
        path += os.sep + os.path.basename(path) + ".py"
    mod = import_from_path(path)
    try:
        definition = getattr(mod, mod.__name__)
    except AttributeError:
        return None
    return definition
