import importlib.util
import pathlib
import types

def load_module_from_file(fpath):
    """
    Load a module from a python file. 
    The module name is the file name without file extension. 
    """
    name = module_name_from_file(fpath)
    spec = importlib.util.spec_from_file_location(name, fpath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def method(obj):
    """
    Decorator used to define a function as a new method of the object obj.
    The method name is the function name.
    """

    def _(func):
        name = func.__name__
        setattr(obj, name, types.MethodType(func, obj))
        return getattr(obj, name)

    return _


def module_name_from_file(fpath):
    """
    Return The module name of the associated python file.
    """
    return pathlib.Path(fpath).stem
    
