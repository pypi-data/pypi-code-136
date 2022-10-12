# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dev_utils_su']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dev-utils-su',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Salvatore Uras',
    'author_email': 'salvatore.uras@dontouch.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
