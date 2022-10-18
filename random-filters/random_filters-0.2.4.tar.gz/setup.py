# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['random_filters', 'random_filters.random_date']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'random-filters',
    'version': '0.2.4',
    'description': '',
    'long_description': '',
    'author': 'Renan',
    'author_email': 'renancavalcantercb@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
