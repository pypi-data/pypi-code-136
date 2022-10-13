# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyflow']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'alfred-pyflow',
    'version': '0.3.2',
    'description': 'Minimal library for the development of Alfred Workflows.',
    'long_description': '# alfred-pyflow',
    'author': 'Fede Calendino',
    'author_email': 'fede@calendino.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fedecalendino/alfred-pyflow',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
