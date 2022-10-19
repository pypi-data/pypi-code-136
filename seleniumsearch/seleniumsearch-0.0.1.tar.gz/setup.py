# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['seleniumsearch']
setup_kwargs = {
    'name': 'seleniumsearch',
    'version': '0.0.1',
    'description': 'Search with selenium',
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
