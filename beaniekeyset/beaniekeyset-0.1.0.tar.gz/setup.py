# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['beaniekeyset']

package_data = \
{'': ['*']}

install_requires = \
['beanie>=1.12.0,<2.0.0',
 'pydantic[all]>=1.10.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'beaniekeyset',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'vamshi.aruru',
    'author_email': 'vamshi.aruru@virgodesigns.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
