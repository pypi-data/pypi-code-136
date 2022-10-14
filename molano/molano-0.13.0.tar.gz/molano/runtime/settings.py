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

AORTA_COMMAND_TOPIC: str = 'molano.commands'

AORTA_COMMAND_PROJECT: str = os.environ['GOOGLE_SERVICE_PROJECT']

AORTA_EVENT_TOPIC: str = 'molano.events'

AORTA_EVENT_PROJECT: str = os.environ['GOOGLE_HOST_PROJECT']

API_BASE_DOMAIN: str = os.environ['API_BASE_DOMAIN']

APP_ENCRYPTION_KEY: str = 'enc'

APP_SIGNING_KEY: str = 'sig'

GOOGLE_DATASTORE_NAMESPACE: str = os.environ['GOOGLE_DATASTORE_NAMESPACE']

GOOGLE_HOST_PROJECT: str = os.environ['GOOGLE_HOST_PROJECT']

GOOGLE_SERVICE_PROJECT: str = os.environ['GOOGLE_SERVICE_PROJECT']

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