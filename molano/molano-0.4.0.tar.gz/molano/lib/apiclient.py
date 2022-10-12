# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Callable
from typing import Generic
from typing import TypeVar

import fastapi
import httpx
from cbra.exceptions import NotFound

from .credential import ICredential
from .credential import NullCredential


C = TypeVar('C')
M = TypeVar('M')


class Consumer(Generic[C]):
    __module__: str = 'cbra.ext.api'
    credential: ICredential = NullCredential()

    @classmethod
    def inject(cls) -> C:
        return fastapi.Depends(cls)

    def get_http_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(**self.get_http_client_kwargs())

    def get_http_client_kwargs(self) -> dict[str, Any]:
        raise NotImplementedError

    async def request(
        self,
        method: str,
        response_model: Callable[..., M],
        *args: Any,
        **kwargs: Any
    ) -> M:
        async with self.get_http_client() as client:
            request = await self.request_factory(
                client=client,
                method=method,
                *args, **kwargs
            )
            response = await self.credential.send(client, request)
        if response.status_code == 404:
            raise NotFound
        response.raise_for_status()
        return response_model(response.json())

    async def request_factory(
        self,
        client: httpx.AsyncClient,
        method: str,
        json: Any | None = None,
        *args: Any,
        **kwargs: Any
    ) -> httpx.Request:
        """Create a :class:`httpx.Request` instance."""
        if json is not None:
            kwargs['json'] = await self.preprocess_json(json)
        request = client.build_request(method=method, *args, **kwargs) # type: ignore
        await self.credential.add_to_request(request)
        return request

    async def preprocess_json(
        self,
        json: dict[str, Any] | list[Any]
    ) -> dict[str, Any] | list[Any]:
        """Preprocess the JSON payload of a request."""
        return await self.credential.preprocess_json(json)