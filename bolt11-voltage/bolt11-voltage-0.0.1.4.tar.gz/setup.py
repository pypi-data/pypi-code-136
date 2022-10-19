# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bolt11']

package_data = \
{'': ['*']}

install_requires = \
['base58>=2.1.1,<3.0.0',
 'bech32>=1.2.0,<2.0.0',
 'bitstring>=3.1.9,<4.0.0',
 'ecdsa>=0.17.0,<0.18.0',
 'typing-extensions>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'bolt11-voltage',
    'version': '0.0.1.4',
    'description': '',
    'long_description': 'None',
    'author': 'eillarra',
    'author_email': 'eneko@illarra.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
