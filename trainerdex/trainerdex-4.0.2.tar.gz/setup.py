# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trainerdex',
 'trainerdex.api',
 'trainerdex.api.client',
 'trainerdex.api.http',
 'trainerdex.api.http.auth',
 'trainerdex.api.types',
 'trainerdex.api.types.v1']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.0,<4.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'typing-extensions>=4.3.0,<5.0.0']

setup_kwargs = {
    'name': 'trainerdex',
    'version': '4.0.2',
    'description': 'An API to interact with TrainerDex - a online database of Pokemon Go trainers',
    'long_description': '[![Support Server](https://img.shields.io/discord/614101299197378571.svg?color=7289da&label=Support&logo=discord&style=flat)](https://discord.gg/pdxh7P)\n[![PyPi version](https://badgen.net/pypi/v/trainerdex/)](https://pypi.org/project/trainerdex/)\n[![wakatime](https://wakatime.com/badge/github/TrainerDex/TrainerDex.py.svg?style=flat)](https://wakatime.com/badge/github/TrainerDex/TrainerDex.py)\n\nA python library for interacting with the TrainerDex API\n\nInstallation\n------------\n\n    pip install trainerdex\n',
    'author': 'Jay Turner',
    'author_email': 'jay@trainerdex.app',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://trainerdex.app/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
