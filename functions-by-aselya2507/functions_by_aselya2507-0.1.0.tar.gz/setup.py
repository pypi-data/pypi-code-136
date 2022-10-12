# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_aselya2507']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-aselya2507',
    'version': '0.1.0',
    'description': 'this is our test project',
    'long_description': '',
    'author': 'Assel Agaidarova',
    'author_email': 'aselya25789@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
