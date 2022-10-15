# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_nizamimeydan']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-nizamimeydan',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Meydan52',
    'author_email': 'nizamimeydan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
