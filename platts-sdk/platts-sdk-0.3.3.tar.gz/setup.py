# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['platts_sdk']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.10.0,<23.0.0',
 'cachetools==4.2.4',
 'pandas==1.3.5',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'platts-sdk',
    'version': '0.3.3',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
