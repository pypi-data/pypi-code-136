# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['peltak_gitflow', 'peltak_gitflow.commands', 'peltak_gitflow.logic']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'peltak-gitflow',
    'version': '0.0.3',
    'description': '',
    'long_description': None,
    'author': 'Mateusz Klos',
    'author_email': 'novopl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://novopl.github.io/peltak-gitflow',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
