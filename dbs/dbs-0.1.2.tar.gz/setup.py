# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbs']

package_data = \
{'': ['*']}

install_requires = \
['databases[aiosqlite]>=0.6.1,<0.7.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['query = dbs.query:app']}

setup_kwargs = {
    'name': 'dbs',
    'version': '0.1.2',
    'description': '',
    'long_description': '# DBS\n\n## Getting started\nInstallation:\n```\npip install dbs\n```\n\nRun with:\n```\npython3 -m dbs.query\n```\n',
    'author': 'yeger00',
    'author_email': 'yeger00@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
