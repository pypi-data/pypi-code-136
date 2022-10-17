# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dsind']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.4,<2.0.0', 'pandas>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'dsind',
    'version': '0.1.0',
    'description': 'the package related to the mlops1 formation',
    'long_description': None,
    'author': 'ismael',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
