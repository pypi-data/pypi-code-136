# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['olxparsing']
setup_kwargs = {
    'name': 'olxparsing',
    'version': '0.0.1',
    'description': 'Olx parsing qilish',
    'long_description': '',
    'author': 'Brodyaga',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
