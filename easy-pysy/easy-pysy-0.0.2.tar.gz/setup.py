# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easy_pysi']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.85.0,<0.86.0',
 'pendulum>=2.1.2,<3.0.0',
 'requests>=2.28.0,<3.0.0',
 'toml>=0.10.2,<0.11.0',
 'typer>=0.6.1,<0.7.0',
 'uvicorn[standard]>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['ez = easy_pysi.console:main']}

setup_kwargs = {
    'name': 'easy-pysy',
    'version': '0.0.2',
    'description': '',
    'long_description': None,
    'author': 'Pierre Merienne',
    'author_email': 'pierre.merienne@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
