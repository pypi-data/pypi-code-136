# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['peltak_todos']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'peltak-todos',
    'version': '0.0.9',
    'description': '',
    'long_description': None,
    'author': 'Mateusz Klos',
    'author_email': 'novopl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://novopl.github.io/peltak-todos',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
