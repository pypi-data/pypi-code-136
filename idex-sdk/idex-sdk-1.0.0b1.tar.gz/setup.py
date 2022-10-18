# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['idex_sdk',
 'idex_sdk.client',
 'idex_sdk.client.order_book',
 'idex_sdk.client.rest',
 'idex_sdk.client.websocket',
 'idex_sdk.idex_types',
 'idex_sdk.idex_types.rest',
 'idex_sdk.idex_types.websocket',
 'idex_sdk.order_book']

package_data = \
{'': ['*']}

install_requires = \
['pyee>=9.0.4,<10.0.0', 'web3>=5.30.0,<6.0.0', 'websockets==9.1']

setup_kwargs = {
    'name': 'idex-sdk',
    'version': '1.0.0b1',
    'description': 'IDEX v3 SDK for Python',
    'long_description': None,
    'author': 'IDEX',
    'author_email': 'support@idex.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.7.1,<3.10',
}


setup(**setup_kwargs)
