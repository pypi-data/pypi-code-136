# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_vladalt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-vladalt',
    'version': '0.1.0',
    'description': 'This is our testproject',
    'long_description': '',
    'author': 'Vladyslav Altyok',
    'author_email': 'vladyslav.altyok@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
