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


GOOGLE_DATASTORE_NAMESPACE: str = os.environ['GOOGLE_DATASTORE_NAMESPACE']

GOOGLE_SERVICE_PROJECT: str = os.environ['GOOGLE_SERVICE_PROJECT']

GLOBAL_DEPENDENCIES: list[dict[str, Any]] = [
    {
        'kind': 'symbol',
        'spec': {
            'name': 'PicqerRepository',
            'qualname': 'molano.infra.PicqerRepository'
        }
    },
    {
        'type': 'symbol',
        'spec': {
            'name': 'DatastoreClient',
            'qualname': 'google.cloud.datastore.Client',
            'invoke': True,
            'kwargs': {
                'project': GOOGLE_SERVICE_PROJECT,
                'namespace': GOOGLE_DATASTORE_NAMESPACE
            }
        }
    }
]