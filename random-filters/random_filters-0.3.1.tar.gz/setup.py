# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src', 'random_date': 'src\\random_date'}

packages = \
['random_date', 'random_filters']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'random-filters',
    'version': '0.3.1',
    'description': '',
    'long_description': '',
    'author': 'Renan',
    'author_email': 'renancavalcantercb@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
