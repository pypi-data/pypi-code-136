# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['energium_protocol_sdk', 'energium_protocol_sdk.fields']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'energium-protocol-sdk',
    'version': '0.0.2',
    'description': '',
    'long_description': None,
    'author': 'dyus',
    'author_email': 'dyuuus@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
