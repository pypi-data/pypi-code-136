# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['getswish']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'rsa>=4.7,<5.0']

setup_kwargs = {
    'name': 'getswish',
    'version': '0.1.2',
    'description': 'Getswish python client library',
    'long_description': None,
    'author': 'Daniel Nibon',
    'author_email': 'daniel@nibon.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
