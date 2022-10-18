# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['project2singleFile']

package_data = \
{'': ['*']}

install_requires = \
['astunparse>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'project2singlefile',
    'version': '0.0.2',
    'description': '',
    'long_description': 'None',
    'author': 'stolati',
    'author_email': '<stolati@gmail.com>',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
