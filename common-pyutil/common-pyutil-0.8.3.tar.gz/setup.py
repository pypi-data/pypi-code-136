# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['common_pyutil']

package_data = \
{'': ['*']}

install_requires = \
['file-magic>=0.4.0,<0.5.0', 'requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['test = pytest:main']}

setup_kwargs = {
    'name': 'common-pyutil',
    'version': '0.8.3',
    'description': 'Some common python utility functions',
    'long_description': "# common-pyutil\nBunch of common utility functions I've used in various projects. This package\nprovides a uniform interface to them.\n\n# Features\n\n- Pure python stdlib with no external dependencies (except [requests](https://github.com/psf/requests))\n- Bunch of useful modules like:\n  1. A simple hierarchical argument parser.\n  2. Functional programming library.\n  3. A `Timer` context for easy monitoring\n  4. A `Tag` decorator for function tagging\n  5. A logging module to get generate a logger with sensible defaults.\n  6. A `Get` class with progress tracking.\n",
    'author': 'Akshay',
    'author_email': 'atavist13@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/akshaybadola/common-pyutil',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
