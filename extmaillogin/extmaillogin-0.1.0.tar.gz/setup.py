# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['extmaillogin']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.10,<4.0.0']

setup_kwargs = {
    'name': 'extmaillogin',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Beda Kosata',
    'author_email': 'beda.kosata@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
