# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['satellitevu', 'satellitevu.apis', 'satellitevu.auth', 'satellitevu.http']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0']

setup_kwargs = {
    'name': 'satellitevu',
    'version': '0.6.0',
    'description': "Client SDK for SatelliteVu's platform APIs",
    'long_description': '# SatelliteVu Platform API Client SDK\n\nLightweight API Client SDK for SatelliteVu\'s Platform APIs, providing authorization\nhandling and convenience methods to interact wit the published APIs.\n\n## Installation\n\nTBD\n\nFor now, need to use the repo as an git based dependency. Can use the `requests` or\n`httpx` optional dependency groups, as these http client implementations can be used\ninstead of the default urllib based client.\n\n## Usage\n\nA User API Client credential set consisting of an _client id_ and _client secret_ is\nneeded and should be set in your script\'s environment variables.\n\nCheck out the [examples](./examples/) provided. They can for example be run locally with\n\n```\npoetry run python ./examples/archive.py --example=recent\n```\n\n### Simple Client Usage\n\nThe easiest way to get started is to use the `satellitevu.Client` class, which needs\na client_id and client_secret only:\n\n```\nimport os\n\nfrom satellitevu import Client\n\n\nclient = Client(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))\nprint(client.archive_v1.search().json())\n```\n\n`client.archive_v1.search` supports all supported request body parameters documented\nin the [API docs](search-api-docs), with special handling for `datetime` which is\nconstructed from the optional `date_from` and `date_to` parameters and a default result\npage size limit of 25.\n\n### Authentication Handling\n\nThe `satellitevu.Auth` class provides the main interface to retrieve an\nauthorization token required to interact with the API endpoints.\n\n```\nimport os\n\nfrom satellitevu import Auth\n\n\nauth = Auth(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))\nprint(auth.token())\n```\n\nThus retrieved token can be used for bearer token authentication in HTTP request\nAuthorization headers.\n\nThe `Auth` class by default uses a file based cache which will store the token in\n\n- `~/.cache/SatelliteVu` on Linux\n- `~/Library/Caches/SatelliteVu` on MacOS\n- `C:\\Documents and Settings\\<username>\\Local Settings\\Application Data\\SatelliteVu\\Cache`\n  on Windows\n\nOther cache implementations must implement the `satellitevu.auth.cache.AbstractCache`\nclass.\n\n### HTTP Client Wrappers\n\nConvenience wrapper classes for common HTTP client implementations are provided as\nimplementations of `satellitevu.http.AbstractClient`, which provides an `request` method\nwith an interface similar to `requests.request` and returning an\n`satellitevu.http.ResponseWrapper` instance, where the response object of the underlying\nimplementation is available in the `raw` property.\n\nCommonly used properties and methods are exposed on both `AbstractClient` and\n`ResponseWrapper`.\n\n- `satellitevu.http.UrllibClient` for Python standard lib\'s `urllib`\n- `satellitevu.http.requests.RequestsSession` using `requests.Session` class\n- `satellitevu.http.httpx.HttpxClient` using `httpx.Client` (Todo)\n\nImplementations based on `requests` and `httpx` allow setting an instance of the\nunderlying implementation, but will provide a default instance if not.\n\n## Developer Setup\n\n### Requirements\n\n- Installations of Python 3.8 and 3.10 (for example using [Pyenv][pyenv])\n- Global installations (for example managed with [pipx][pipx]) of\n  - Python [Poetry](poetry)\n  - Python [nox](nox) with [nox-poetry](nox-poetry) plugin\n- Make (optional)\n\nExample global setup (with `pyenv` and `pipx`):\n\n```\npyenv install 3.8.13\npyenv install 3.10.4\npipx install poetry\npipx install nox\npipx inject nox nox-poetry\n```\n\nPlease bootstrap your environment with `make bootstrap`.\n\n#### Example test setup with `pyenv` and `pipx`\n\nRun tests against Python version used by poetry:\n\n```\nmake test\nmake PYTEST_ADDOPTS="-x -s" test\n```\n\nor\n\n```\npoetry run pytest\nPYTEST_ADDOPTS="-x -s" poetry run pytest\n```\n\nRun tests against Python 3.8 and Python 3.10:\n\n```\npyenv shell 3.8.13 3.10.4\nnox\n```\n\n[pyenv]: https://github.com/pyenv/pyenv\n[poetry]: https://python-poetry.org\n[pipx]: https://pypa.github.io/pipx/\n[nox]: https://nox.thea.codes/en/stable/\n[nox-poetry]: https://nox-poetry.readthedocs.io/en/stable/\n[search-api-docs]: https://api.satellitevu.com/archive/v1/docs#operation/Search_search_post\n',
    'author': 'Christian Wygoda',
    'author_email': 'christian.wygoda@satellitevu.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
