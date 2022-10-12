# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['byu_pytest_utils']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.0.1,<8.0.0']

entry_points = \
{'pytest11': ['byu_pytest_utils = byu_pytest_utils.pytest_plugin']}

setup_kwargs = {
    'name': 'byu-pytest-utils',
    'version': '0.3.1',
    'description': 'A few utilities for pytest to help with integration into gradescope',
    'long_description': None,
    'author': 'Daniel Zappala',
    'author_email': 'daniel.zappala@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
