# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['menage_jupyter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'menage-jupyter',
    'version': '0.1.3',
    'description': 'Simple package to menage jupyter files',
    'long_description': None,
    'author': 'Bartłomiej Chwiłkowski',
    'author_email': 'bartekchwilkowski@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
