# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multicall_thread_safe']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.8,<23.0',
 'flake8>=5.0,<6.0',
 'joblib>=1.2,<2.0',
 'pytest>=7.1,<8.0']

setup_kwargs = {
    'name': 'multicall-thread-safe',
    'version': '0.1.1',
    'description': 'Thread Safe Multicall for execution in containerised environments, tweaked from https://github.com/banteg/multicall.py',
    'long_description': '',
    'author': 'cbhondwe',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cbsystango/multicall-thread-safe/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
