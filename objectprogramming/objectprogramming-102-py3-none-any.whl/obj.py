# This file is placed in the Public Domain.
# pylint: disable=R,C,W


"Object"


import types


from .cls import Class


def __dir__():
    return (
            'Object',
            'edit',
            'items',
            'kind',
            'type',
            'register',
            'update',
            'values'
           )


class Object:

    def __init__(self, *args, **kwargs):
        object.__init__(self)
        if args:
            try:
                self.__dict__.update(vars(args[0]))
            except TypeError:
                self.__dict__.update(args[0])
        if kwargs:
            self.__dict__.update(kwargs)
            
    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return str(self. __dict__)


Class.add(Object)


def edit(obj, setter):
    for key, value in items(setter):
        register(obj, key, value)


def items(obj):
    if isinstance(obj, type({})):
        return obj.items()
    return obj.__dict__.items()


def keys(obj):
    return obj.__dict__.keys()


def kind(obj):
    return str(type(obj)).split()[-1][1:-2]


def register(obj, key, value):
    setattr(obj, key, value)


def update(obj, data):
    for key, value in items(data):
        setattr(obj, key, value)


def values(obj):
    return obj.__dict__.values()
