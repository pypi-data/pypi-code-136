# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['heath']

package_data = \
{'': ['*']}

install_requires = \
['bl-event-sourcing-sqlalchemy>=0.1.0',
 'bl-event-sourcing>=0.1.0',
 'typer>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['heath = heath:app']}

setup_kwargs = {
    'name': 'heath',
    'version': '0.2.1',
    'description': 'Manage projections',
    'long_description': '# Heath — Manage projections\n\nDefine the DSN to work with:\n\n```console\n$ export HEATH_DSN="sqlite:////tmp/projections.sqlite"\n```\n\nInitialise projection database:\n\n```console\n$ heath init\n```\n\nList the projections:\n\n```console\n$ heath status\n```\n',
    'author': 'Tanguy Le Carrour',
    'author_email': 'tanguy@bioneland.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.easter-eggs.org/bioneland/heath',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
