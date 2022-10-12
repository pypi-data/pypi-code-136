# Copyright (C) 2022 Cochise Ruhulessin
# 
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from molano.canon import PicqerUser
from molano.lib import ServiceRepository


class PicqerRepository(ServiceRepository):
    resource: str = 'isg'

    async def get_user(self, user_id: int) -> PicqerUser | None:
        return await self.retrieve(
            resource_path=f'picqer/users/{user_id}',
            response_model=PicqerUser
        )