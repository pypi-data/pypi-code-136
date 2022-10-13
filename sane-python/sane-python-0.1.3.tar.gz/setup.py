# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sane_python']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.3,<2.0.0']

setup_kwargs = {
    'name': 'sane-python',
    'version': '0.1.3',
    'description': 'Simple Array of Numbers Encoding in Python',
    'long_description': None,
    'author': 'Viktor Kronvall',
    'author_email': 'viktor.kronvall@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
