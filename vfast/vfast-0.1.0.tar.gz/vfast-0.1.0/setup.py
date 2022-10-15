# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vfast']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vfast',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Ethan Vu',
    'author_email': 'ethanvu.dev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
