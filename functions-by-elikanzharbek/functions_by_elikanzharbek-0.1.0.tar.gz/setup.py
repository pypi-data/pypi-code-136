# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_elikanzharbek']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-elikanzharbek',
    'version': '0.1.0',
    'description': 'This is our first project',
    'long_description': '',
    'author': 'Eliza Kanzharbek',
    'author_email': 'elikanzharbek@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
