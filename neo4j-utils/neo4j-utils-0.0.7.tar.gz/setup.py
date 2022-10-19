# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neo4j_utils']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.0', 'colorlog', 'neo4j>=4.4,<5.0', 'toml']

setup_kwargs = {
    'name': 'neo4j-utils',
    'version': '0.0.7',
    'description': '',
    'long_description': 'Extras on top of the official Neo4j driver\n##########################################\n\nIf you search *neo4j* in *PyPI*, besides a ton of abandoned or irrelevant\nmodules, you will find the ``neo4j`` module provided by the Neo4j company,\nand the full-fledged, community developed ``py2neo``. The official module\ncomes with a really bare-bones API. Here we only add a thin wrapper around\nit to make its usage a bit more convenient.\n',
    'author': 'Denes Turei',
    'author_email': 'turei.denes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/saezlab/neo4j-utils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
