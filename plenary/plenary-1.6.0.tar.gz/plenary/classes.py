# -*- coding: utf-8 -*-
from importlib import import_module
from inspect import isabstract
from pkgutil import walk_packages
from types import ModuleType
from typing import Any, List, Type, TypeVar, Union

__all__ = [
    'TObject',
    'get_subclasses',
    'resolve_global'
]


TObject = TypeVar('TObject', bound=object)


def _recurse_subclasses(subclass_list: List[Type[TObject]]) -> List[Type[TObject]]:
    return_list = []

    for subclass in subclass_list:
        if len(subclass.__subclasses__()) > 0:
            return_list.extend(_recurse_subclasses(subclass.__subclasses__()))

            if not isabstract(subclass):
                return_list.append(subclass)
        else:
            return_list.append(subclass)

    return return_list


def get_subclasses(class_root: Type[TObject], include_parent: bool = True) -> List[Type[TObject]]:
    """ Get a list of subclasses for a given parent class.

    :param class_root: parent class type
    :param include_parent: if True returned list includes the parent class, otherwise it is discarded
    :return: list
    """
    subclass_list = _recurse_subclasses([class_root])

    if not include_parent:
        subclass_list.remove(class_root)

    return subclass_list


def import_submodules(package: Union[str, ModuleType], recursive: bool = True) -> List[ModuleType]:
    """ Import all submodules within a given package.

    :param package: base package to begin import from
    :param recursive: if True then import submodules
    :return: list of imported submodules
    """
    if isinstance(package, str):
        package = import_module(package)

    import_list = []

    for loader, name, is_pkg in walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name

        import_list.append(import_module(full_name))

        if recursive and is_pkg:
            import_list.extend(import_submodules(full_name))

    return import_list


def resolve_global(name: str) -> Any:
    """ Resolve a global method, class or module name, importing as required.

    :param name:
    :return:
    """
    # Split name
    name_split = name.split('.')

    # Find root object
    obj_name = name_split.pop(0)
    obj = __import__(obj_name)

    while len(name_split) > 0:
        attr_name = name_split.pop(0)
        obj_name = obj_name + '.' + attr_name

        try:
            obj = getattr(obj, attr_name)
        except AttributeError:
            # Attempt to import module if not already imported
            __import__(obj_name)
            obj = getattr(obj, attr_name)

    return obj
