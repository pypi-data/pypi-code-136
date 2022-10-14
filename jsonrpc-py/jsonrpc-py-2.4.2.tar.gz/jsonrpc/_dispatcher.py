# Pure zero-dependency JSON-RPC 2.0 implementation.
# Copyright © 2022 Andrew Malchuk. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod
from collections import UserDict as Dict
from collections.abc import Callable
from functools import partial
from inspect import Signature, isfunction
from typing import Any, Final, Protocol, TypeAlias, TypeVar, cast, overload

from ._errors import Error, ErrorEnum

__all__: Final[tuple[str, ...]] = ("Dispatcher",)

_AnyCallable: TypeAlias = Callable[..., Any]
_FuncT = TypeVar("_FuncT", bound=_AnyCallable)


class register_decorator(Protocol):
    @overload
    def __call__(self, user_function: _FuncT, /) -> _FuncT: ...
    @overload
    def __call__(self, user_function: _FuncT, *, function_name: str | None = ...) -> _FuncT: ...
    @overload
    def __call__(self, *, function_name: str | None = ...) -> Callable[[_FuncT], _FuncT]: ...


class BaseDispatcher(Dict[str, _AnyCallable], metaclass=ABCMeta):
    __slots__: tuple[str, ...] = ()

    def __hash__(self) -> int:
        return hash(frozenset(self.items()))

    def __repr__(self) -> str:
        return f"<{self.__class__.__qualname__}({self.data!r})>"

    @property
    @abstractmethod
    def register(self) -> register_decorator:
        raise NotImplementedError

    @abstractmethod
    def dispatch(self, function_name: str, /, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


class Dispatcher(BaseDispatcher):
    """
    The :py:class:`collections.UserDict` subclass representing the storage of user-defined functions.

    For example::

        >>> dispatcher = Dispatcher()
        >>> dispatcher["func"] = lambda: True
        >>> dispatcher["func"]
        <function <lambda> at 0x\u2026>
    """
    __slots__: tuple[str, ...] = ()

    @property
    def register(self) -> register_decorator:
        """
        Returns a decorator for the registering user-defined functions.

        Example usage::

            >>> @dispatcher.register
            ... def truediv(a: float, b: float) -> float:
            ...     return a / b

        Also you can pass the different function's name::

            >>> @dispatcher.register(function_name="sum")
            ... def _(a: float, b: float) -> float:
            ...     return a + b

        :param user_function: The :py:data:`types.FunctionType` object representing the user-defined function.
        :param function_name: An optional function's name. If it is omitted, attribute ``__name__`` will be used instead.
        :raises RuntimeError: If the ``user_function`` isn't passed by the :py:func:`inspect.isfunction` method,
            or function with the provided name is already defined in the :class:`jsonrpc.Dispatcher` class.
        :returns: The unmodified ``user_function`` object, passed in the parameters.
        """
        def wrapper(user_function: _FuncT | None = None, *, function_name: str | None = None) -> _FuncT | Callable[[_FuncT], _FuncT]:
            if user_function is None:
                return cast(Callable[[_FuncT], _FuncT], partial(wrapper, function_name=function_name))

            if not isfunction(user_function):
                raise RuntimeError(f"{type(user_function).__name__!r} isn't a user-defined function")

            if (function_name := user_function.__name__ if function_name is None else function_name) in self:
                raise RuntimeError(f"{function_name!r} is already defined in {self[function_name].__module__!r}")

            self[function_name] = user_function
            return user_function

        return cast(register_decorator, wrapper)

    def dispatch(self, function_name: str, /, *args: Any, **kwargs: Any) -> Any:
        """
        Invoke the user-defined function by passed in parameters function's name.

        Example usage::

            >>> dispatcher = Dispatcher()
            >>> dispatcher.dispatch("sum", a=12, b=34)
            46

        :param function_name: The user-defined function's name.
        :param args: Positional arguments for the provided function.
        :param kwargs: Keyword arguments for the provided function.
        :raises jsonrpc.Error: If the function doesn't exists in the :class:`jsonrpc.Dispatcher` class,
            passed invalid parameters or unexpected internal error has raised. See also :class:`jsonrpc.ErrorEnum`.
        :returns: Result of execution the user-defined function.
        """
        try:
            user_function: Final[_AnyCallable] = self[function_name]
        except KeyError as exc:
            raise Error(code=ErrorEnum.METHOD_NOT_FOUND, message=f"Function {function_name!r} isn't found") from exc

        try:
            Signature.from_callable(user_function).bind(*args, **kwargs)
        except TypeError as exc:
            raise Error(code=ErrorEnum.INVALID_PARAMETERS, message=f"Invalid parameters: {exc!s}") from exc

        try:
            return user_function(*args, **kwargs)
        except Error:
            raise
        except Exception as exc:
            raise Error(code=ErrorEnum.INTERNAL_ERROR, message=f"Unexpected internal error: {exc!s}") from exc
