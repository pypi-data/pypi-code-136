# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rating_model']

package_data = \
{'': ['*'], 'rating_model': ['data/*', 'models/*']}

setup_kwargs = {
    'name': 'rating-model',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'rahul',
    'author_email': 'rahul07031991@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
