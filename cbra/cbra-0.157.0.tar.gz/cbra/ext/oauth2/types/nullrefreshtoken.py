# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .iclient import IClient
from .isubject import ISubject
from .irefreshtoken import IRefreshToken


class NullRefreshToken(IRefreshToken):
    __module__: str = 'cbra.ext.oauth2.types'

    async def generate(self, client: IClient, subject: ISubject) -> str | None:
        return None