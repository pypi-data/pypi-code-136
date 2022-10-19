# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['leakix']

package_data = \
{'': ['*']}

install_requires = \
['l9format>=1.3.1,<2.0.0', 'requests']

setup_kwargs = {
    'name': 'leakix',
    'version': '0.1.2',
    'description': 'Official python client for LeakIX (https://leakix.net)',
    'long_description': None,
    'author': 'Danny Willems',
    'author_email': 'danny@leakix.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
