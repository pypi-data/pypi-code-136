# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import fastapi
import httpx


class ICredential:
    """The base class for all HTTP credential implementations."""
    __module__: str = 'cbra.ext.api'

    @classmethod
    def inject(cls) -> Any:
        return fastapi.Depends(cls)

    async def add_to_request(self, request: httpx.Request) -> None:
        """Modify a :class:`httpx.Request` instance to include this
        credential.
        """
        pass

    async def get_authentication(self) -> httpx.Auth | None:
        return None

    async def preprocess_json(
        self,
        json: dict[str, Any] | list[Any]
    ) -> dict[str, Any] | list[Any]:
        """Preprocess the JSON payload of a request."""
        return json

    async def send(
        self,
        client: httpx.AsyncClient,
        request: httpx.Request
    ) -> httpx.Response:
        response = await client.send(request, auth=await self.get_authentication())
        return await self.process_response(client, response.request, response)

    async def process_response(
        self,
        client: httpx.AsyncClient,
        request: httpx.Request,
        response: httpx.Response
    ) -> httpx.Response:
        return response