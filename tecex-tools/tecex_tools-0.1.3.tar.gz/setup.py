# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tecex_tools']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.5.1,<2.0.0',
 'pytest>=7.1.3,<8.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['tecex-tools = tecex_tools.cli:app']}

setup_kwargs = {
    'name': 'tecex-tools',
    'version': '0.1.3',
    'description': '',
    'long_description': '',
    'author': 'Scott Fuller',
    'author_email': 'fullerscott085@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
