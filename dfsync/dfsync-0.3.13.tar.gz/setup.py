# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dfsync', 'dfsync.backends']

package_data = \
{'': ['*']}

install_requires = \
['click>=7,<8',
 'gitpython>=3.1.14,<4.0.0',
 'kubernetes>=12.0.1,<13.0.0',
 'tenacity>=8.0.1,<9.0.0',
 'toml>=0.10.2,<0.11.0',
 'watchdog>=2.0.2,<3.0.0']

entry_points = \
{'console_scripts': ['dfsync = dfsync.cli:dfsync']}

setup_kwargs = {
    'name': 'dfsync',
    'version': '0.3.13',
    'description': '',
    'long_description': None,
    'author': 'Mihai Balint',
    'author_email': 'balint.mihai@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
