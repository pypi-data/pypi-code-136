# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pystub', 'pystub._cli_modules']

package_data = \
{'': ['*']}

install_requires = \
['requests==2.28.1', 'setuptools==65.3.0']

setup_kwargs = {
    'name': 'pystub',
    'version': '0.0.2a0',
    'description': 'Python Stub',
    'long_description': '# pystub\nPython Project Stub\n',
    'author': 'tonynv',
    'author_email': 'avattathil@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
