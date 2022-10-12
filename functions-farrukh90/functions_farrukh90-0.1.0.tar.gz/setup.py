# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_farrukh90']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-farrukh90',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
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
