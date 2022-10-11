# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['larkspur']

package_data = \
{'': ['*']}

install_requires = \
['redis>=3.5.3,<4.0.0']

setup_kwargs = {
    'name': 'larkspur',
    'version': '0.2.2',
    'description': 'a Redis-backed, scalable Bloom filter',
    'long_description': 'None',
    'author': 'Thomas R Storey',
    'author_email': 'orey.st@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
