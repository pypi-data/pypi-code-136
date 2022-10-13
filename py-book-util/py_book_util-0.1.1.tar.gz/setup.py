# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_book_util']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-book-util',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': '"Richard.Tang"',
    'author_email': 'tang_can@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
