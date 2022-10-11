import abc
import warnings
from dataclasses import dataclass
from functools import partial
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Generic,
    Iterator,
    List,
    Optional,
    Type,
    TypeVar,
    cast,
)

from pydantic import BaseModel, Field
from result import Result
from result.result import F, U

from blacksmith.domain.error import AbstractErrorParser, TError_co

if TYPE_CHECKING:
    from pydantic.typing import IntStr
else:
    IntStr = str

from ...domain.exceptions import HTTPError, NoResponseSchemaException
from ...typing import (
    ClientName,
    HttpLocation,
    HTTPMethod,
    Json,
    Path,
    ResourceName,
    Url,
)
from .http import HTTPRequest, HTTPResponse, Links

PATH: HttpLocation = "path"
HEADER: HttpLocation = "headers"
QUERY: HttpLocation = "querystring"
BODY: HttpLocation = "body"


PathInfoField = partial(Field, location=PATH)
"""Declare field that are serialized to the path info."""
HeaderField = partial(Field, location=HEADER)
"""Declare field that are serialized in http request header."""
QueryStringField = partial(Field, location=QUERY)
"""Declare field that are serialized in the http querystring."""
PostBodyField = partial(Field, location=BODY)
"""Declare field that are serialized in the json document."""


class Request(BaseModel):
    """
    Request Params Model.

    Fields must use subclass :func:`.PathInfoField`, :func:`.HeaderField`,
    :func:`.QueryStringField` or :func:`.PostBodyField` to declare each fields.
    """

    def to_http_request(self, method: HTTPMethod, url_pattern: Url) -> HTTPRequest:
        """Convert the request params to an http request in order to serialize
        the http request for the client.
        """
        req = HTTPRequest(method=method, url_pattern=url_pattern)
        fields_by_loc: Dict[HttpLocation, Dict[IntStr, Any]] = {
            HEADER: {},
            PATH: {},
            QUERY: {},
            BODY: {},
        }
        for field in self.__fields__.values():
            loc = cast(
                HttpLocation,
                field.field_info.extra["location"],  # type: ignore
            )
            fields_by_loc[loc].update({field.name: ...})

        headers = self.dict(
            include=fields_by_loc[HEADER], by_alias=True, exclude_none=True
        )
        req.headers = {key: str(val) for key, val in headers.items()}
        req.path = self.dict(
            include=fields_by_loc[PATH], by_alias=True, exclude_none=False
        )
        req.querystring = self.dict(
            include=fields_by_loc[QUERY], by_alias=True, exclude_none=True
        )
        req.body = self.json(
            include=fields_by_loc[BODY], by_alias=True, exclude_none=False
        )
        return req


TResponse = TypeVar("TResponse", bound="Response")
TCollectionResponse = TypeVar("TCollectionResponse", bound="Response")


class Response(BaseModel):
    """Response Model."""


@dataclass
class Metadata:
    """Metadata of a collection response."""

    count: int
    total_count: Optional[int]
    links: Links


class AbstractCollectionParser(abc.ABC):
    """
    Signature of the collection parser.
    """

    resp: HTTPResponse

    def __init__(self, resp: HTTPResponse):
        self.resp = resp

    @property
    @abc.abstractmethod
    def meta(self) -> Metadata:
        """
        Return the metatadata from the response.

        Usually, metadata are in a header, but if the API wrap the list,

        ::

            {
                "total_items": 0,
                "items": []
            }


        Then, the ``Metadata.total_count`` can be extracted from the json,
        instead of the header.
        """

    @property
    @abc.abstractmethod
    def json(self) -> List[Any]:
        """
        Return the list part of the response the response.

        For instance, if an API wrap the list in a structure like

        ::

            {
                "items": [
                    {"objkey": "objval"}
                ]
            }

        then, the ``resp.json["items"]`` has to be returned.
        """


class CollectionParser(AbstractCollectionParser):
    """
    Handle the rest collection metadata parser.

    Deserialize how a collection is wrapped.
    """

    total_count_header: str = "Total-Count"

    @property
    def meta(self) -> Metadata:
        total_count = self.resp.headers.get(self.total_count_header)
        return Metadata(
            count=len(self.json),
            total_count=None if total_count is None else int(total_count),
            links=self.resp.links,
        )

    @property
    def json(self) -> List[Json]:
        return self.resp.json or []


class ResponseBox(Generic[TResponse, TError_co]):
    """
    Wrap a HTTP response and deserialize it.

    ::

        user: ResponseBox[User, HTTPError] = (
            await api.user.get({"username": username})
        )
        if user.is_ok():
            print(user.unwrap().username)
        else:
            print(f"API Call failed: {user.unwrap_err()}")

    """

    def __init__(
        self,
        result: Result[HTTPResponse, HTTPError],
        response_schema: Optional[Type[Response]],
        method: HTTPMethod,
        path: Path,
        name: ResourceName,
        client_name: ClientName,
        error_parser: AbstractErrorParser[TError_co],
    ) -> None:
        self.raw_result = result
        self.response_schema = response_schema
        self.method: HTTPMethod = method
        self.path: Path = path
        self.name: ResourceName = name
        self.client_name: ClientName = client_name
        self.error_parser = error_parser

    def _cast_optional_resp(self, resp: HTTPResponse) -> Optional[TResponse]:
        if self.response_schema is None:
            return None
        schema_cls = self.response_schema
        return cast(TResponse, schema_cls(**(resp.json or {})))

    def _cast_resp(self, resp: HTTPResponse) -> TResponse:
        if self.response_schema is None:
            raise NoResponseSchemaException(
                self.method, self.path, self.name, self.client_name
            )
        schema_cls = self.response_schema
        return cast(TResponse, schema_cls(**(resp.json or {})))

    @property
    def json(self) -> Optional[Dict[str, Any]]:
        """
        Return the raw json response.

        It return the raw response body without noticing if its a
        normal or an error response.
        """
        if self.raw_result.is_ok():
            return self.raw_result.unwrap().json
        return self.raw_result.unwrap_err().response.json

    @property
    def response(self) -> TResponse:
        """
        Parse the response using the schema.

        .. deprecated:: 2.0
            Use :meth:`ResponseBox.unwrap()`

        :raises blacksmith.HTTPError: if the response contains an error.
        :raises NoResponseSchemaException: if the response_schema has not been
            set in the contract.
        """
        warnings.warn(
            ".response is deprecated, use .unwrap() instead",
            category=DeprecationWarning,
        )
        if self.raw_result.is_err():
            raise self.raw_result.unwrap_err()
        if self.response_schema is None:
            raise NoResponseSchemaException(
                self.method, self.path, self.name, self.client_name
            )
        resp = self.response_schema(**(self.json or {}))
        return cast(TResponse, resp)

    def as_optional(self) -> Result[Optional[TResponse], TError_co]:
        """
        Expose the instance as an optional result.

        In case no response schema has been provided while registering the resource,
        then a ``Ok(None)`` is return to not raise any
        :class:`blacksmith.NoResponseSchemaException`
        """
        return self.raw_result.map(self._cast_optional_resp).map_err(
            self.error_parser  # type: ignore
        )

    @property
    def _result(self) -> Result[TResponse, TError_co]:
        return self.raw_result.map(self._cast_resp).map_err(
            self.error_parser  # type: ignore
        )

    def is_ok(self) -> bool:
        """Return True if the response was an http success."""
        return self.raw_result.is_ok()

    def is_err(self) -> bool:
        """Return True if the response was an http error."""
        return self.raw_result.is_err()

    def unwrap(self) -> TResponse:
        """
        Return the parsed response.

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        resp = self._result.unwrap()
        return resp

    def unwrap_err(self) -> TError_co:
        """Return the response error."""
        return self.as_optional().unwrap_err()

    def unwrap_or(self, default: TResponse) -> TResponse:
        """
        Return the response or the default value in case of error.

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        return self._result.unwrap_or(default)

    def unwrap_or_else(self, op: Callable[[TError_co], TResponse]) -> TResponse:
        """
        Return the response or the callable return in case of error.

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        return self._result.unwrap_or_else(op)

    def expect(self, message: str) -> TResponse:
        """
        Return the response or raise an UnwrapError exception with the given message.

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        return self._result.expect(message)

    def expect_err(self, message: str) -> TError_co:
        """Return the error or raise an UnwrapError exception with the given message."""
        return self.as_optional().expect_err(message)

    def map(self, op: Callable[[TResponse], U]) -> Result[U, TError_co]:
        """
        Apply op on response in case of success, and return the new result.

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        return self._result.map(op)  # type: ignore

    def map_or(self, default: U, op: Callable[[TResponse], U]) -> U:
        """
        Apply and return op on response in case of success, default in case of error.

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        return self._result.map_or(default, op)

    def map_or_else(
        self, default_op: Callable[[], U], op: Callable[[TResponse], U]
    ) -> U:
        """
        Return the result of default_op in case of error otherwise the result of op.

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        return self._result.map_or_else(default_op, op)

    def map_err(self, op: Callable[[HTTPError], F]) -> Result[TResponse, F]:
        """
        Apply op on error in case of error, and return the new result.

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        # works in mypy, not in pylance
        return self.raw_result.map(self._cast_resp).map_err(op)  # type: ignore

    def and_then(
        self, op: Callable[[TResponse], Result[U, HTTPError]]
    ) -> Result[U, HTTPError]:
        """
        Apply the op function on the response and return it if success

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        # works in mypy, not in pylance
        return self._result.and_then(op)  # type: ignore

    def or_else(
        self, op: Callable[[HTTPError], Result[TResponse, F]]
    ) -> Result[TResponse, F]:
        """
        Apply the op function on the error and return it if error

        :raises NoResponseSchemaException: if there are no response schema set.
        """
        return self._result.or_else(op)  # type: ignore


class CollectionIterator(Iterator[TResponse]):
    """
    Deserialize the models in a json response list, item by item.
    """

    response: AbstractCollectionParser

    def __init__(
        self,
        response: HTTPResponse,
        response_schema: Optional[Type[Response]],
        collection_parser: Type[AbstractCollectionParser],
    ) -> None:
        self.pos = 0
        self.response_schema = response_schema
        self.response = collection_parser(response)
        self.json_resp = self.response.json

    @property
    def meta(self) -> Metadata:
        """
        Get the response metadata such as counts in http header, links...

        Those metadata are generated by the collection_parser.
        """
        return self.response.meta

    def __next__(self) -> TResponse:
        try:
            resp = self.json_resp[self.pos]
            if self.response_schema:
                resp = self.response_schema(**resp)
        except IndexError:
            raise StopIteration()

        self.pos += 1
        return cast(TResponse, resp)  # Could be a dict

    def __iter__(self) -> "CollectionIterator[TResponse]":
        return self
