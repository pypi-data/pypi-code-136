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

from ckms.core import parse_dsn


API_BASE_DOMAIN: str = os.environ['API_BASE_DOMAIN']

APP_ENCRYPTION_KEY: str = 'enc'

APP_SIGNING_KEY: str = 'sig'

KEYCHAIN: dict[str, Any] = {
    APP_ENCRYPTION_KEY: {
        **parse_dsn(os.environ['APP_ENCRYPTION_KEY']),
        'tags': ['oauth2-client']
    },
    APP_SIGNING_KEY: {
        **parse_dsn(os.environ['APP_SIGNING_KEY']),
        'tags': ['oauth2-client']
    },
}

OAUTH2_SERVER: str = 'https://accounts.webidentity.id'

OAUTH2_SERVICE_CLIENT: str = os.environ['OAUTH_SERVICE_CLIENT']

RESOURCE_SERVERS: dict[str, Any] = {
    'isg': {
        'server': f'https://isg.{API_BASE_DOMAIN}',
        'scope': {"molanoapis.com/internal"}
    },
}