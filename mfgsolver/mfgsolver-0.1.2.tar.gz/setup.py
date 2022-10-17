# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mfgsolver']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.2,<4.0', 'numpy>=1.21,<2.0', 'scipy>=1.7,<2.0']

setup_kwargs = {
    'name': 'mfgsolver',
    'version': '0.1.2',
    'description': 'solve mean field game pde system with finite difference and policy iteration',
    'long_description': 'None',
    'author': 'songjhaha',
    'author_email': 'songjh96@foxmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
