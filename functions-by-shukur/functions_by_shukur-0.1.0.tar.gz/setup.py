# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_shukur']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-shukur',
    'version': '0.1.0',
    'description': 'THis is our test project',
    'long_description': '',
    'author': 'Shukur Iminov',
    'author_email': 'ssean6754@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
