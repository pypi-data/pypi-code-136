# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['txtint']

package_data = \
{'': ['*']}

install_requires = \
['argcomplete>=2.0.0,<3.0.0', 'rich>=12.6.0,<13.0.0']

setup_kwargs = {
    'name': 'txtint',
    'version': '0.0.63',
    'description': 'tools for metamodern text interfaces',
    'long_description': 'Command Line Interfaces and Textual User Interfaces are old but not outdated.\n',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ragt.ag/code/txtint',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
