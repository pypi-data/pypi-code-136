# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrlclient', 'qctrlclient.auth', 'qctrlclient.transports']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.4.0,<3.0.0',
 'gql>=3.4.0,<4.0.0',
 'qctrl-commons>=17.1.0,<18.0.0',
 'requests-oauthlib>=1.3.1,<2.0.0']

setup_kwargs = {
    'name': 'qctrl-client',
    'version': '1.0.0',
    'description': 'Q-CTRL Client',
    'long_description': "# Q-CTRL Python Client\n\nThe Q-CTRL Python Client package provides a Python client to access Q-CTRL's GraphQL API. It is used as a base for Q-CTRL's client-side product packages and for inter-service communication.\n",
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<3.11',
}


setup(**setup_kwargs)
