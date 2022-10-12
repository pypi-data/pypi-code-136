from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable, Collection, Optional

from atoti_core import keyword_only_dataclass

from ._py4j_utils import to_python_dict
from .pyapi.http_request import HttpRequest
from .pyapi.user import User

if TYPE_CHECKING:
    from ._local_session import LocalSession  # pylint: disable=nested-import

    CallbackEndpoint = Callable[[HttpRequest, User, LocalSession[Any]], Any]


@keyword_only_dataclass
@dataclass
class EndpointHandler:
    name: str = field(default="Python.EndpointHandler", init=False, repr=False)
    callback: CallbackEndpoint
    session: LocalSession[Any]

    def handleRequest(  # pylint: disable=invalid-name, too-many-positional-parameters
        self,
        url: str,
        username: str,
        roles: str,
        path_parameter_values: Any,  # JavaMap, but is not typed
        body: Optional[str] = None,
    ) -> str:
        path_parameters = {
            str(key): str(value)
            for key, value in to_python_dict(path_parameter_values).items()
        }
        parsed_body = None if body is None else json.loads(body)
        request = HttpRequest(
            url=url, path_parameters=path_parameters, body=parsed_body
        )
        user = User(name=username, roles=roles[1 : len(roles) - 1].split(", "))

        response_body = self.callback(
            request,
            user,
            self.session,
        )

        return json.dumps(response_body)

    def toString(self) -> str:  # pylint: disable=invalid-name
        return self.name

    class Java:
        """Code needed for Py4J callbacks."""

        implements: Collection[str] = ["io.atoti.pyapi.EndpointHandler"]
