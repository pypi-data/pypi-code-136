# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cockroachdb_cloud_client',
 'cockroachdb_cloud_client.api',
 'cockroachdb_cloud_client.api.cockroach_cloud',
 'cockroachdb_cloud_client.models']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.3.0', 'httpx>=0.15.4,<0.24.0', 'python-dateutil>=2.8.0,<3.0.0']

setup_kwargs = {
    'name': 'cockroachdb-cloud-client',
    'version': '0.0.3',
    'description': 'A client library for accessing CockroachDB Cloud API',
    'long_description': '# cockroachdb_cloud_client\n\nA client library for accessing the CockroachDB Cloud API.\n\nRead the [CockroachDB Cloud OpenAPI Spec](https://www.cockroachlabs.com/docs/api/cloud/v1.html) on our docs page.\n\n## Usage\n\nFirst, create a client, then, call your endpoint and use your models:\n\n```python\nfrom cockroachdb_cloud_client import AuthenticatedClient\nfrom cockroachdb_cloud_client.models import ListClustersResponse\nfrom cockroachdb_cloud_client.api.cockroach_cloud import cockroach_cloud_list_clusters\nfrom cockroachdb_cloud_client.types import Response\n\nimport os\n\ncc_key = os.environ[\'CC_KEY\']\n\nclient = AuthenticatedClient(\n    base_url="https://cockroachlabs.cloud",\n    token=cc_key,\n    headers={"cc-version": "2022-09-20"},\n)\n\nresp: Response[ListClustersResponse] = cockroach_cloud_list_clusters.sync_detailed(client=client)\n\nfor x in resp.parsed.clusters:\n    print(x.name)\n\n# Output:\n# cute-otter\n# gummy-rabbit\n# half-weasel\n# itchy-donkey\n# redear-thrush\n```\n\n### Things to know\n\n1. Every path/method combo becomes a Python module with four functions:\n    1. `sync`: Blocking request that returns parsed data (if successful) or `None`\n    2. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.\n    3. `asyncio`: Like `sync` but async instead of blocking\n    4. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking\n\n2. All path/query params, and bodies become method arguments.\n3. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)\n4. Any endpoint which did not have a tag will be in `cockroachdb_cloud_client.api.default`\n',
    'author': 'Cockroach Labs',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.cockroachlabs.com/docs/api/cloud/v1.html#get-/api/v1/clusters',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
