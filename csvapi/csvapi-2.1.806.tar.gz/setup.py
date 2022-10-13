# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['csvapi']

package_data = \
{'': ['*']}

install_requires = \
['Quart>=0.18.0,<0.19.0',
 'agate-excel>=0.2.5,<0.3.0',
 'agate-sql>=0.5.8,<0.6.0',
 'agate>=1.6.3,<1.7.0',
 'aiohttp>=3.8.1,<3.9.0',
 'aiosqlite>=0.17.0,<0.18.0',
 'boto3>=1.24.66,<1.25.0',
 'cchardet>=2.1.7,<2.2.0',
 'click>=8.1.3,<8.2.0',
 'click_default_group>=1.2.2,<1.3.0',
 'csv-detective>=0.4.6,<0.5.0',
 'pandas-profiling>=3.2.0,<3.3.0',
 'pandas>=1.4.4,<1.5.0',
 'python-stdnum>=1.17,<1.18',
 'quart-cors>=0.5.0,<0.6.0',
 'requests>=2.28.1,<2.29.0',
 'sentry-sdk>=1.9.8,<1.10.0',
 'validators>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['csvapi = csvapi.cli:cli']}

setup_kwargs = {
    'name': 'csvapi',
    'version': '2.1.806',
    'description': 'An instant JSON API for your CSV',
    'long_description': 'None',
    'author': 'Opendatateam',
    'author_email': 'opendatateam@data.gouv.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
