# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['make_gtfs']

package_data = \
{'': ['*']}

install_requires = \
['gtfs-kit>=5', 'pandera>=0.11.0']

setup_kwargs = {
    'name': 'make-gtfs',
    'version': '4.0.2',
    'description': 'A Python 3.8+ library to build GTFS feeds from basic route information.',
    'long_description': None,
    'author': 'Alex Raichev',
    'author_email': 'araichev@mrcagney.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
