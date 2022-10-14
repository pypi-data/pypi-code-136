# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['localpdb',
 'localpdb.plugins',
 'localpdb.plugins.config',
 'localpdb.plugins.utils',
 'localpdb.utils',
 'localpdb.utils.search_api',
 'localpdb.utils.search_api.tools']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'beautifulsoup4>=4.9.3,<5.0.0',
 'biopython>=1,<2',
 'coloredlogs>=15.0,<16.0',
 'pandas>=1,<2',
 'pyaml>=20.4.0,<21.0.0',
 'requests>=2.25.1,<3.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'tqdm>=4,<5']

entry_points = \
{'console_scripts': ['localpdb_setup = localpdb.localpdb_setup:main']}

setup_kwargs = {
    'name': 'localpdb',
    'version': '0.2.5',
    'description': '',
    'long_description': None,
    'author': 'Jan Ludwiczak',
    'author_email': 'j.ludwiczak@cent.uw.edu.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
