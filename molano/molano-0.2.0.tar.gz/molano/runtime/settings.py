# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os
from typing import Any


API_BASE_DOMAIN: str = os.environ['API_BASE_DOMAIN']

RESOURCE_SERVERS: dict[str, Any] = {
    'isg': {
        'server': f'https://isg.{API_BASE_DOMAIN}',
        'scope': {"molanoapis.com/internal"}
    },
}