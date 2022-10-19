# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['flake8_import_rules']
entry_points = \
{'flake8.extension': ['I013 = flake8_import_rules:ImportRulesChecker']}

setup_kwargs = {
    'name': 'flake8-import-rules',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'VL',
    'author_email': '1844144@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
