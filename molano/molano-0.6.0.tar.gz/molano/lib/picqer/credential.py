# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import httpx
from cbra.ext import ioc

from ..credential import ICredential


class PicqerCredential(ICredential):
    email: str
    key: str

    def __init__(
        self,
        api_email: str = ioc.environment('PICQER_API_EMAIL'),
        api_key: str = ioc.environment('PICQER_API_KEY')
    ):
        self.email = api_email
        self.key = api_key

    async def add_to_request(self, request: httpx.Request) -> None:
        request.headers.update({
            'User-Agent': f"Molano Internal Systems Gateway ({self.email})"
        })

    async def get_authentication(self) -> httpx.BasicAuth:
        return httpx.BasicAuth(username=self.key, password='X')