# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ok_zadanie_1',
 'ok_zadanie_1.edge',
 'ok_zadanie_1.graph',
 'ok_zadanie_1.graph_creator',
 'ok_zadanie_1.graph_utils',
 'ok_zadanie_1.graph_visualizer',
 'ok_zadanie_1.vertex']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.1,<4.0.0', 'networkx>=2.8.7,<3.0.0']

setup_kwargs = {
    'name': 'ok-zadanie-1',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'Rafał Majewski',
    'author_email': 'goodheropl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
