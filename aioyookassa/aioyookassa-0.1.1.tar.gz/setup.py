# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioyookassa',
 'aioyookassa.contrib',
 'aioyookassa.core',
 'aioyookassa.core.abc',
 'aioyookassa.core.methods',
 'aioyookassa.exceptions',
 'aioyookassa.types']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'aioyookassa',
    'version': '0.1.1',
    'description': 'Asynchronous wrapper to interact with yookassa.ru API',
    'long_description': None,
    'author': 'Marple',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
