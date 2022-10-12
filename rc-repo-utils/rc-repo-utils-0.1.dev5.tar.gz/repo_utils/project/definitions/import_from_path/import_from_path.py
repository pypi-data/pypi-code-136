import inspect
import os
from importlib.util import module_from_spec, spec_from_file_location
from os.path import basename, dirname, join


def import_from_path(path: str, root_dir: str = None):
    """Given a filepath, return the module

    Args:
        - path (str): Relative or absolute path to the module.
        - root_dir (str): Directory from which to start the relative path (e.g. __file__).

    Returns:
        - mod (ModuleType): The loaded module.
    """
    if not path.startswith(os.sep):
        if root_dir:
            path = join(dirname(root_dir), path)
        else:
            # Apply relative path from caller's directory.
            path = join(dirname(inspect.stack()[1].filename), path)
    name = basename(path).replace(".py", "")
    if not path.endswith(".py"):
        path += ".py"
    mod = None
    try:
        spec = spec_from_file_location(name, path)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)
    except ModuleNotFoundError:
        pass
    return mod
