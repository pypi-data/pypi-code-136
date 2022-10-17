# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pfs', 'pfs.api.v1']

package_data = \
{'': ['*']}

install_requires = \
['googleapis-common-protos>=1.56.4,<2.0.0', 'protobuf>=3.20.3,<4.0.0']

setup_kwargs = {
    'name': 'pfs-api',
    'version': '0.1.0',
    'description': 'protos generated python api for pfs',
    'long_description': 'API of photon feature store',
    'author': 'linyiming',
    'author_email': 'linyiming@ainnovation.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
