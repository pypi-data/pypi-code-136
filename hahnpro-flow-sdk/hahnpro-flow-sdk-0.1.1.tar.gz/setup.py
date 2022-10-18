# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hahnpro_flow_sdk']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=8.2.2,<9.0.0', 'typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'hahnpro-flow-sdk',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'timoklingenhoefer',
    'author_email': 'timo.klingenhoefer@web.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
