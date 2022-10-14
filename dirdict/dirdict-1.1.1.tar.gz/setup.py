# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['dirdict']
setup_kwargs = {
    'name': 'dirdict',
    'version': '1.1.1',
    'description': 'A dictionary-like interface for your file system.',
    'long_description': 'None',
    'author': 'AsbjornOlling',
    'author_email': 'asbjornolling@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
