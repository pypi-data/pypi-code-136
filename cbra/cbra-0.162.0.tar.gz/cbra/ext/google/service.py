# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import aorta
from cbra.ext import ioc
from cbra.ext import service

from .aortaendpoint import AortaEndpoint
from .debugtransport import DebugTransport
from .commandendpoint import CommandEndpoint


class Service(service.Service):
    beat_prefix: str = '/.well-known/beat'

    def beat(
        self,
        name: str,
        command: type[aorta.Command],
        summary: str | None = None
    ) -> None:
        """Expose an endpoint where the scheduler can beat the application
        to produce the specified command.
        """
        self.add(CommandEndpoint.as_command_handler(name, command, summary))

    async def boot(self):
        await super().boot()
        self.add(AortaEndpoint)
        if not ioc.is_satisfied('MessageTransport'):
            ioc.provide(
                name='MessageTransport',
                value=DebugTransport(
                    app=self,
                    base_url="https://127.0.0.1",
                    path="/.well-known/aorta"
                ),
                force=True
            )