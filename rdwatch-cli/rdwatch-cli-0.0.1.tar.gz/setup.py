# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rdwatch_cli']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'aiohttp>=3.8.3,<4.0.0',
 'click>=8.1.3,<9.0.0',
 'mercantile>=1.2.1,<2.0.0',
 'pillow-avif-plugin>=1.2.2,<2.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['rdwatch = rdwatch_cli:cli']}

setup_kwargs = {
    'name': 'rdwatch-cli',
    'version': '0.0.1',
    'description': 'Client for the RD-WATCH server.',
    'long_description': '',
    'author': 'Kitware, Inc.',
    'author_email': 'kitware@kitware.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ResonantGeoData/RD-WATCH/django',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10.0,<3.11.0',
}


setup(**setup_kwargs)
