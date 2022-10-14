# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Callable

import aorta
from cbra.ext import service

from .aortaendpoint import AortaEndpoint


class Service(service.Service):
    beat_prefix: str = '/.well-known/beat'

    def beat(
        self,
        name: str,
        command: type[aorta.Command]
    ) -> None:
        """Expose an endpoint where the scheduler can beat the application
        to produce the specified command.
        """
        async def f(dto: command._model):
            await self.publisher.publish(command())

        self.add_api_route(
            path=f'{self.beat_prefix}/{name}',
            endpoint=f,
            methods=['POST'],
            tags=['Beats'],
            status_code=204,
            responses={
                204: {'description': f"A **{command.__name__}** is issued."},
                401: {'description': "The request requires authentication."},
                403: {'description': "The principal is not allowed to beat the application."},
                422: {'description': "Parameters are required to invoke the command."}
            }
        )

    async def boot(self):
        await super().boot()
        self.add(AortaEndpoint)