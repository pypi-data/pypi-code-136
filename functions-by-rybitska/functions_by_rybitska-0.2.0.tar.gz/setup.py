# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_rybitska']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-rybitska',
    'version': '0.2.0',
    'description': 'This is test project',
    'long_description': '# Instructions\n\n### This is test project.',
    'author': 'somename',
    'author_email': 'krybitska@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
