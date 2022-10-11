from functools import update_wrapper
from types import FunctionType, MethodType
from typing import AnyStr, List, Type, get_type_hints


class FunctionMethodEnforcer:
    def __init__(self, __fn__):
        update_wrapper(self, __fn__)
        self.__fn__ = __fn__
        self.__outer_self__ = None
        self.__hints = get_type_hints(self.__fn__)
        self.__check_method_function__()

    def __exception__(self, message):
        raise Exception(f"({self.__fn__.__qualname__}): {message}")

    def __get__(self, obj, objtype):
        self.__outer_self__ = obj
        return self.__call__

    def __check_method_function__(self):
        if not isinstance(self.__fn__, (MethodType, FunctionType)):
            raise Exception(
                f"A non function/method was passed to Enforcer. See the stack trace above for more information."
            )

    def __call__(self, *args, **kwargs):
        if self.__outer_self__ is not None:
            args = (self.__outer_self__,) + args

        if self.__fn__.__defaults__ is not None:
            kwarg_defaults = dict(
                zip(
                    self.__fn__.__code__.co_varnames[-len(self.__fn__.__defaults__):],
                    self.__fn__.__defaults__,
                )
            )
        else:
            kwarg_defaults = {}
        assigned_vars = {
            **dict(zip(self.__fn__.__code__.co_varnames[: len(args)], args)),
            **kwarg_defaults,
            **kwargs,
        }
        annotations = dict(self.__annotations__)
        for key, value in annotations.items():
            if key in assigned_vars:
                self.__check_type__(assigned_vars.get(key), value, key)

        return_value = self.__fn__(*args, **kwargs)
        if "return" in annotations:
            self.__check_type__(return_value, annotations["return"], "return")
        return return_value

    def __check_type__(self, obj, types, key):
        print(self, obj, types, key, self.__hints[key])
        if key in self.__hints and isinstance(obj, self.__hints[key]):
            return
        if not isinstance(types, list):
            types = [types]

        types = [i if i is not None else type(None) for i in types]
        if isinstance(obj, type):
            passed_type = Type[obj]
        else:
            passed_type = type(obj)
        if passed_type not in types:
            self.__exception__(
                f"Type mismatch for typed variable `{key}`. Expected one of the following `{str(types)}` but got `{passed_type}` instead."
            )

    def __repr__(self):
        return f"<type_enforced {self.__fn__.__module__}.{self.__fn__.__qualname__} object at {hex(id(self))}>"


def Enforcer(clsFnMethod):
    if isinstance(clsFnMethod, (staticmethod, classmethod, FunctionType, MethodType)):
        if getattr(clsFnMethod, "__annotations__", {}) == {}:
            return clsFnMethod
        elif isinstance(clsFnMethod, staticmethod):
            return staticmethod(FunctionMethodEnforcer(clsFnMethod.__func__))
        elif isinstance(clsFnMethod, classmethod):
            return classmethod(FunctionMethodEnforcer(clsFnMethod.__func__))
        elif isinstance(clsFnMethod, (FunctionType, MethodType)):
            return FunctionMethodEnforcer(clsFnMethod)
    else:
        for key, value in clsFnMethod.__dict__.items():
            if hasattr(value, "__call__") or isinstance(value, (classmethod, staticmethod)):
                setattr(clsFnMethod, key, Enforcer(value))
        return clsFnMethod


@Enforcer
def fun(a: AnyStr, b):
    return


if __name__ == "__main__":
    issubclass([], List)
    fun("s", None)
