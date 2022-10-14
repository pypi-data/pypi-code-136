# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""Declares :class:`CloudSchedulerEndpoint`."""
from typing import Any

import aorta

from cbra.utils import classproperty
from .cloudschedulerendpoint import CloudSchedulerEndpoint


class CommandEndpoint(CloudSchedulerEndpoint):
    """A :class:`~cbra.ext.google.CloudSchedulerEndpoint` implementation that handles
    a request that is received from Google Cloud Scheduler and issues a command.
    """
    __module__: str = 'cbra.ext.google'
    default_response_code: int = 204
    response_description: str = "The command was issued."
    tags: list[str] = ["Beat"]

    @classproperty
    def responses(cls) -> dict[str | int, Any]:
        return {
            204: {'description': f"The command is issued."},
            401: {'description': "The request requires authentication."},
            403: {'description': "The principal is not allowed to beat the application."},
            422: {'description': "Parameters are required to invoke the command."}
        }

    @classmethod
    def as_command_handler(
        cls,
        name: str,
        command: type[aorta.Command],
        summary: str | None = None
    ) -> Any:
        """Create a new :class:`CommandEndpoint` implementation that
        handles the given command.
        """
        async def f(self: CommandEndpoint, dto: command._model): # type: ignore
            await self.publisher.publish(command(**dto.dict()))
        return cls.new(
            command_class=command,
            handle=f,
            methods=['POST'],
            tags=['Beats'],
            mount_path=f'.well-known/beat/{name}',
            name=f'commands.{name}',
            summary=summary or f"Issue {command.__name__}",
        )