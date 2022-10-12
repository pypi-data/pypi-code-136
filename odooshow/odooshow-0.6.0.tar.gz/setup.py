# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['odooshow']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.5.1,<13.0.0']

setup_kwargs = {
    'name': 'odooshow',
    'version': '0.6.0',
    'description': 'Make use of rich power tools to have nice formatted data in Odoo shells',
    'long_description': None,
    'author': 'David Vidal',
    'author_email': 'chienandalu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.3,<4.0',
}


setup(**setup_kwargs)
