# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_nasiba_87']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-nasiba-87',
    'version': '0.2.0',
    'description': '',
    'long_description': '# Instructions\n\n#### This is our first project',
    'author': 'somename',
    'author_email': 'a@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
