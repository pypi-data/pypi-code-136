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
from collections import UserList as List
from collections.abc import Iterable, MutableMapping, MutableSequence
from numbers import Number
from typing import Any, Final, Literal, TypeAlias, TypeVar, Union

from ._errors import BaseError, Error, ErrorEnum
from ._utilities import Undefined, UndefinedType, make_hashable

__all__: Final[tuple[str, ...]] = ("BatchRequest", "Request")

_Params: TypeAlias = list[object] | dict[str, object]
_BaseRequestOrError = TypeVar("_BaseRequestOrError", bound=Union["BaseRequest", BaseError])

# Method names that begins with the "rpc." prefix are reserved for internal usage only:
_INVALID_SIGNATURE: Final[str] = "\x72\x70\x63\x2E"


class BaseRequest(metaclass=ABCMeta):
    __slots__: tuple[str, ...] = ()

    @property
    @abstractmethod
    def method(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def args(self) -> tuple[Any, ...]:
        raise NotImplementedError

    @property
    @abstractmethod
    def kwargs(self) -> dict[str, Any]:
        raise NotImplementedError

    @property
    @abstractmethod
    def request_id(self) -> str | float | UndefinedType:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_notification(self) -> bool:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_json(obj: dict[str, Any]) -> Union["BaseRequest", BaseError]:
        raise NotImplementedError


class BaseBatchRequest(List[_BaseRequestOrError], metaclass=ABCMeta):
    __slots__: tuple[str, ...] = ()

    def __hash__(self) -> int:
        return hash(tuple(self.data))

    def __repr__(self) -> str:
        return f"<{self.__class__.__qualname__}({self.data!r})>"

    @staticmethod
    @abstractmethod
    def from_json(iterable: Iterable[dict[str, Any]]) -> "BaseBatchRequest[_BaseRequestOrError]":
        raise NotImplementedError


class Request(BaseRequest):
    """
    Base JSON-RPC request object.

    :param method: The :py:class:`str` object containing the name of the method.
    :param params: The object of type :py:class:`list` or :py:class:`dict` that holds the parameter values
        to be used during the invocation of the method.
        May be omitted if provided method has no parameters for example.
    :param request_id: The :py:class:`str` object or any type of :py:class:`numbers.Number` object which represents an identifier
        of the request instance. May be omitted. If its value omitted, the request assumed to be a notification.
    :raises jsonrpc.Error: If the request method isn't a string or have a \"rpc.\" prefix, if the request parameters
        aren't an objects of type :py:class:`collections.abc.MutableSequence` or :py:class:`collections.abc.MutableMapping` if provided,
        also if the request identifier isn't an object of type :py:class:`str` or :py:class:`numbers.Number` if provided.
    """
    __slots__: tuple[str, ...] = ("_method", "_params", "_id")

    def __init__(
        self,
        *,
        method: str,
        params: _Params | UndefinedType = Undefined,
        request_id: str | float | UndefinedType = Undefined
    ) -> None:
        self._method: Final[str] = self._validate_method(method) and method
        self._params: Final[_Params | UndefinedType] = self._validate_params(params) and params
        self._id: Final[str | float | UndefinedType] = self._validate_id(request_id) and request_id

    def __repr__(self) -> str:
        return f"<{self.__class__.__qualname__}(" \
            f"method={self._method!r}, " \
            f"params={self._params!r}, " \
            f"request_id={self._id!r})>"

    def __hash__(self) -> int:
        return hash((self._method, make_hashable(self._params), self._id))

    def __eq__(self, obj: Any) -> bool:
        if not isinstance(obj, self.__class__):
            return NotImplemented
        return (self._method, self._params, self._id) == (obj.method, obj._params, obj._id)

    def _validate_method(self, method: Any) -> Literal[True]:
        if not isinstance(method, str) or method.startswith(_INVALID_SIGNATURE, 0, len(_INVALID_SIGNATURE)):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message=f"Request method must be a string and doesn't have a {_INVALID_SIGNATURE!r} prefix")
        return True

    def _validate_params(self, params: Any) -> Literal[True]:
        if not isinstance(params, MutableSequence | MutableMapping | UndefinedType):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message=f"Request params must be a sequence or mapping, not a {type(params).__name__!r}")
        return True

    def _validate_id(self, request_id: Any) -> Literal[True]:
        if not isinstance(request_id, str | Number | UndefinedType):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message=f"Request id must be an optional string or number, not a {type(request_id).__name__!r}")
        return True

    @property
    def method(self) -> str:
        """
        Returns the :py:class:`str` object containing the name of the method.
        """
        return self._method

    @property
    def args(self) -> tuple[object, ...]:
        """
        Returns the :py:class:`tuple` object containing positional arguments of the method.
        """
        return tuple(params) if isinstance(params := self._params, MutableSequence) else ()

    @property
    def kwargs(self) -> dict[str, object]:
        """
        Returns the :py:class:`dict` object containing keyword arguments of the method.
        """
        return params if isinstance(params := self._params, MutableMapping) else {}

    @property
    def request_id(self) -> str | float | UndefinedType:
        """
        Returns the :py:class:`str` object or any type of :py:class:`numbers.Number` object
        containing the identifier of the request if its value is set.
        """
        return self._id

    @property
    def is_notification(self) -> bool:
        """
        Returns :py:data:`True` if the identifier of the request is omitted, :py:data:`False` elsewise.
        """
        return isinstance(self._id, UndefinedType)

    @staticmethod
    def from_json(obj: dict[str, Any]) -> Union["Request", Error]:
        """
        The static method for creating the :class:`jsonrpc.Request` object from :py:class:`dict` object.
        Unlike the :class:`jsonrpc.Request` constructor, doesn't raises any exceptions by validations,
        it returns the :class:`jsonrpc.Error` as is.

        Example usage::

            >>> Request.from_json({"jsonrpc": "2.0", "method": "foobar", "id": 1})
            <Request(method="foobar", params=Undefined, request_id=1)>
            >>> Request.from_json({"not_jsonrpc": True})
            <Error(code=-32600, message="Invalid request object", data={"not_jsonrpc": True})>
        """
        try:
            match obj:
                case {"jsonrpc": "2.0", "method": method, "params": params, "id": request_id}:
                    return Request(method=method, params=params, request_id=request_id)
                case {"jsonrpc": "2.0", "method": method, "params": params}:
                    return Request(method=method, params=params)
                case {"jsonrpc": "2.0", "method": method, "id": request_id}:
                    return Request(method=method, request_id=request_id)
                case {"jsonrpc": "2.0", "method": method}:
                    return Request(method=method)
                case _:
                    raise Error(code=ErrorEnum.INVALID_REQUEST, message="Invalid request object", data=obj)
        except Error as error:
            return error


class BatchRequest(BaseBatchRequest[Request | Error]):
    """
    The :py:class:`collections.UserList` subclass representing the collection
    of :class:`jsonrpc.Request` and :class:`jsonrpc.Error` objects.
    """
    __slots__: tuple[str, ...] = ()

    @staticmethod
    def from_json(iterable: Iterable[dict[str, Any]]) -> "BatchRequest":
        """
        The static method for creating the :class:`jsonrpc.BatchRequest` object from :py:class:`collections.abc.Iterable`
        of :py:class:`dict` objects.
        Similar to :func:`jsonrpc.Request.from_json` function it doesn't raises any exceptions.

        Example usage::

            >>> BatchRequest.from_json([
            ...     {"jsonrpc": "2.0", "method": "foobar", "id": 1},
            ...     {"not_jsonrpc": True}
            ... ])
            <BatchRequest((<Request(\u2026)>, <Error(\u2026)>))>
        """
        return BatchRequest(map(Request.from_json, iterable))
