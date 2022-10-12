# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_batirova']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-batirova',
    'version': '0.2.0',
    'description': 'This is out test project',
    'long_description': '',
    'author': 'Gulnara Batirova',
    'author_email': 'batirova@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
