# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imouapi', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

extras_require = \
{':extra == "test"': ['aioresponses>=0.7.3,<0.8.0'],
 'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocstrings-python>=0.7.1,<0.8.0',
         'mkdocs>=1.3.1,<2.0.0',
         'mkdocs-include-markdown-plugin>=3.8.1,<4.0.0',
         'mkdocs-material>=8.5.3,<9.0.0',
         'mkdocs-autorefs>=0.4.1,<0.5.0'],
 'test': ['black>=22.3.0,<23.0.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

setup_kwargs = {
    'name': 'imouapi',
    'version': '1.0.1',
    'description': 'Library for controlling Imou devices by interacting with the Imou Life API.',
    'long_description': '# imouapi\nThis python library helps in interacting with [Imou Life Open API](https://open.imoulife.com) for remote controlling programmatically your [Imou devices](https://www.imoulife.com), especially those settings such as motion detection, human detection, privacy, etc that can be changed by the Imou Life App only.\n\n## Features\n\n- Provide classes for both low level API interaction as well as device and sensors abastractions\n- Exceptions and error handling\n- Based on asyncio module\n\n## Quickstart\n\n- Install the library with `pip install imouapi`\n- Register a developer account on [Imou Life Open API](https://open.imoulife.com) and get your `appId` and `appSecret`\n- Instantiate the Imou API client (`from imouapi.api import ImouAPIClient`) and initialize it (e.g. `api_client = ImouAPIClient(app_id, app_secret, session)`)\n- Discover registered devices by importing the Discover service (`from imouapi.device import ImouDiscoverService`), inializing it (e.g. `discover_service = ImouDiscoverService(api_client)`) and running a discovery (e.g. `discovered_devices = await discover_service.async_discover_devices()`)\n- Either use the high level API by importing the Imou Device class (`from imouapi.device import ImouDevice`) and initializing it (e.g. `device = ImouDevice(api_client, device_id)`) or using directly the low level API provided by `ImouAPIClient` to interact with the device\n\nFull details on the installation process, requirements, usage and classes and methods made available by the library are available at [https://user2684.github.io/imouapi](https://user2684.github.io/imouapi)\n',
    'author': 'user2684',
    'author_email': 'user2684@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/user2684/imouapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
