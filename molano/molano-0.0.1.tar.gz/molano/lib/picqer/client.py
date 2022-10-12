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
from typing import TypeVar

import fastapi
import httpx
from cbra.ext import ioc

from .user import User


T = TypeVar('T')


class PicqerClient:
    __module__: str = 'molano.lib.picqer'
    domain: str
    email: str
    http: httpx.AsyncClient
    key: str

    @classmethod
    def inject(cls) -> 'PicqerClient':
        return fastapi.Depends(cls)

    def __init__(
        self,
        api_domain: str = ioc.environment('PICQER_API_DOMAIN'),
        api_email: str = ioc.environment('PICQER_API_EMAIL'),
        api_key: str = ioc.environment('PICQER_API_KEY')
    ):
        self.domain = api_domain
        self.email = api_email
        self.key = api_key

    def get_http_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(
            auth=httpx.BasicAuth(
                username=self.key,
                password='X'
            ),
            base_url=f'https://{self.domain}/api/v1/',
            headers={
                'User-Agent': f"Molano Internal Systems Gateway ({self.email})"
            }
        )

    async def request(
        self,
        method: str,
        response_model: Callable[..., T],
        *args: Any,
        **kwargs: Any
    ) -> T:
        async with self.get_http_client() as client:
            response = await client.request(method=method, *args, **kwargs) # type: ignore
        return response_model(response.json())

    # Implementation
    async def get_user(self, user_id: int) -> User:
        return await self.request(
            method='GET',
            response_model=User.parse_obj,
            url=f'users/{user_id}'
        )