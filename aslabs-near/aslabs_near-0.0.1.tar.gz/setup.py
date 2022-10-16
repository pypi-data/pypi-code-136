# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aslabs',
 'aslabs.near',
 'aslabs.near.models',
 'aslabs.near.signature_verifier']

package_data = \
{'': ['*']}

install_requires = \
['base58>=2.1.1,<3.0.0', 'ed25519>=1.5,<2.0', 'near-api-py>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'aslabs-near',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'Titusz Ban',
    'author_email': 'tituszban@antisociallabs.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
