import json
from ssl import SSLContext
from typing import Any, Callable, Optional
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from ._http import HttpHeaders


def _handle_error(error: HTTPError, body: Any) -> None:
    raise RuntimeError("Request failed", body) from error


def fetch_json(
    url: str,
    *,
    body: Optional[Any] = None,
    headers: HttpHeaders = None,
    on_error: Callable[[HTTPError, Any], None] = _handle_error,
    ssl_context: Optional[SSLContext] = None,
) -> Any:
    data = json.dumps(body).encode("utf8") if body else None
    headers = {
        "Content-Type": "application/json",
        **(headers or {}),
    }
    request = Request(url, data=data, headers=headers)
    try:
        with urlopen(request, context=ssl_context) as response:  # nosec
            return json.load(response)
    except HTTPError as error:
        body = error.read()
        try:
            body = json.loads(body)
            on_error(error, body)
        except json.JSONDecodeError:
            raise RuntimeError("Request failed", body) from error
