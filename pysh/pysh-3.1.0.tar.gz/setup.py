# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysh']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysh',
    'version': '3.1.0',
    'description': 'A library of small functions that simplify scripting in python',
    'long_description': '',
    'author': 'Stanislav Zmiev',
    'author_email': 'szmiev2000@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Ovsyanka83/pysh',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
