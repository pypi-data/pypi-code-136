# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ajobot_manager']

package_data = \
{'': ['*']}

install_requires = \
['aioredis>=2.0.1,<3.0.0', 'loguru>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'ajobot-manager',
    'version': '1.1.1',
    'description': 'An interface for the different ajobots',
    'long_description': 'None',
    'author': 'Axel Amigo Arnold',
    'author_email': 'axl89@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
