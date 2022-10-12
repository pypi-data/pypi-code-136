# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import httpx
from cbra.ext import ioc

from ..apiclient import Consumer
from .credential import PicqerCredential
from .supplier import Supplier
from .user import User
from .warehouse import Warehouse


class PicqerClient(Consumer['PicqerClient']):
    __module__: str = 'molano.lib.picqer'
    domain: str
    http: httpx.AsyncClient

    def __init__(
        self,
        api_domain: str = ioc.environment('PICQER_API_DOMAIN'),
        credential: PicqerCredential = PicqerCredential.inject()
    ):
        self.credential = credential
        self.domain = api_domain

    def get_http_client_kwargs(self) -> dict[str, Any]:
        return {'base_url': f'https://{self.domain}/api/v1/'}

    # Implementation
    async def get_supplier(self, supplier_id: int) -> Supplier:
        return await self.request(
            method='GET',
            response_model=Supplier.parse_obj,
            url=f'suppliers/{supplier_id}'
        )

    async def get_user(self, user_id: int) -> User:
        return await self.request(
            method='GET',
            response_model=User.parse_obj,
            url=f'users/{user_id}'
        )

    async def get_warehouse(self, warehouse_id: int) -> Warehouse:
        return await self.request(
            method='GET',
            response_model=Warehouse.parse_obj,
            url=f'warehouses/{warehouse_id}'
        )