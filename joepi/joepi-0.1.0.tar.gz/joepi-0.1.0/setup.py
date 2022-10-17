# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['joepi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'joepi',
    'version': '0.1.0',
    'description': 'Hello, World!',
    'long_description': 'joepi\n',
    'author': 'Joseph Abrahams',
    'author_email': 'joseph@abrahams.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
