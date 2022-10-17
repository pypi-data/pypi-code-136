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
from json import dumps as _json_encode, loads as _json_decode
from pickle import HIGHEST_PROTOCOL, dumps as _pickle_encode, loads as _pickle_decode
from typing import Any, ClassVar, Final

from ._errors import Error, ErrorEnum

__all__: Final[tuple[str, ...]] = ("JSONSerializer", "PickleSerializer")


class BaseSerializer(metaclass=ABCMeta):
    __slots__: tuple[str, ...] = ()

    def __repr__(self) -> str:
        return f"<{self.__class__.__qualname__}()>"

    @abstractmethod
    def serialize(self, obj: Any) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def deserialize(self, obj: bytes) -> Any:
        raise NotImplementedError


class JSONSerializer(BaseSerializer):
    """
    Simple class for JSON serialization and deserialization.
    """
    __slots__: tuple[str, ...] = ()

    def serialize(self, obj: Any) -> bytes:
        """
        Returns the JSON representation of a value.

        :param obj: An any type of object that must be JSON serializable.
        :raises jsonrpc.Error: If any exception has occurred due the serialization or/and encoding to :py:class:`bytes`.
        :returns: The :py:class:`bytes` object containing the serialized Python data structure.
        """
        try:
            return _json_encode(obj, separators=(",", ":")).encode("latin-1")
        except Exception as exc:
            raise Error(code=ErrorEnum.PARSE_ERROR, message="Failed to serialize object to JSON") from exc

    def deserialize(self, obj: bytes) -> Any:
        """
        Returns the value encoded in JSON in appropriate Python type.

        :param obj: The :py:class:`bytes` object containing the serialized JSON document.
        :raises jsonrpc.Error: If any exception has occurred due the deserialization or/and decoding from :py:class:`bytes`.
        :returns: An any type of object containing the deserialized Python data structure.
        """
        try:
            return _json_decode(obj)
        except Exception as exc:
            raise Error(code=ErrorEnum.PARSE_ERROR, message="Failed to deserialize object from JSON") from exc


class PickleSerializer(BaseSerializer):
    """
    Simple class for the "Pickling" and "Unpickling" Python objects.
    """
    __slots__: tuple[str, ...] = ()

    #: Pickle protocol version used for the serialization.
    #: Defaults to :py:data:`pickle.HIGHEST_PROTOCOL`.
    PROTOCOL_VERSION: ClassVar[int] = HIGHEST_PROTOCOL

    def serialize(self, obj: Any) -> bytes:
        """
        Returns the pickled representation of a value.

        :param obj: An any type of object that must be serializable.
        :raises jsonrpc.Error: If exception has occurred due the pickling.
        :returns: The :py:class:`bytes` object containing the pickled object.
        """
        try:
            return _pickle_encode(obj, self.PROTOCOL_VERSION)
        except Exception as exc:
            raise Error(code=ErrorEnum.PARSE_ERROR, message="Failed to serialize object") from exc

    def deserialize(self, obj: bytes) -> Any:
        """
        Returns the unpickled representation of a value.

        :param obj: The :py:class:`bytes` object containing the pickled object.
        :raises jsonrpc.Error: If exception has occurred due the unpickling.
        :returns: An any type of object containing the deserialized Python data structure.
        """
        try:
            return _pickle_decode(obj)
        except Exception as exc:
            raise Error(code=ErrorEnum.PARSE_ERROR, message="Failed to deserialize object") from exc
