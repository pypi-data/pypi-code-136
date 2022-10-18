# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['c7n_left', 'c7n_left.providers.terraform']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0', 'rich>=12.5,<13.0', 'tfparse>=0.2,<0.3']

entry_points = \
{'console_scripts': ['c7n-left = c7n_left.cli:cli']}

setup_kwargs = {
    'name': 'c7n-left',
    'version': '0.0.1',
    'description': 'Custodian policies for IAAC definitions',
    'long_description': 'None',
    'author': 'Cloud Custodian Project',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://cloudcustodian.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
