# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['didyoumean_nhannht']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['didyoumean = didyoumean_nhannht.main:main']}

setup_kwargs = {
    'name': 'didyoumean-nhannht',
    'version': '0.1.6',
    'description': '',
    'long_description': '',
    'author': 'nhanclassroom',
    'author_email': 'nhanclassroom@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
