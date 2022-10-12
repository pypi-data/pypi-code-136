from importlib.util import module_from_spec, spec_from_file_location
from os.path import basename, join


def import_from_dir(path: str):
    """Given a path to a directory with an __init__.py file, return the module"""
    name = basename(path)
    mod = None
    try:
        path = join(path, "__init__.py")
        spec = spec_from_file_location(name, path)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod = getattr(mod, name)
    except (ModuleNotFoundError, AttributeError):
        pass
    return mod
