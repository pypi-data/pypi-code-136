# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ogoutils']

package_data = \
{'': ['*']}

install_requires = \
['pyAesCrypt>=6.0.0,<7.0.0', 'pytest>=7.1.3,<8.0.0']

entry_points = \
{'console_scripts': ['ogoutils = ogoutils.__main__:main']}

setup_kwargs = {
    'name': 'ogo-utils',
    'version': '0.1.20',
    'description': 'This project prefer utils for self working',
    'long_description': '# OGO Clients Utils | Python == 3.9.10\n\n> This project provides utilities for my daily use.\n\n## Installation\n\n```shell\npython3 -m pip install ogo-utils\n```\n\n## Set config\n```shell\npoetry config pypi-token.pypi pypi-token\n```',
    'author': 'Vasiliy Silver',
    'author_email': 's555133@mail.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
