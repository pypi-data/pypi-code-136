from http import HTTPStatus as HTTP_STATUS
from typing import Any

from sanic.request import Request as SanicRequest, File
from sanic.response import BaseHTTPResponse, HTTPResponse

__all__ = (
    'HTTP_STATUS',
    'File',
    'Request',
    'Response',
)

class Request(SanicRequest):
    pass

class Response(HTTPResponse):
    pass

def response_json(body: Any, status: int = 200, headers: dict[str, str] | None = None, **kwargs: Any) -> Response:
    json_data = BaseHTTPResponse._dumps(body, **kwargs)  # pylint: disable=protected-access
    return Response(json_data, headers=headers, status=status, content_type='application/json')
