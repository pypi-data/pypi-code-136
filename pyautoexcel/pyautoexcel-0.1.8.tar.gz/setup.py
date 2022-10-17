# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyautoexcel']

package_data = \
{'': ['*']}

install_requires = \
['pywin32>=304,<305']

setup_kwargs = {
    'name': 'pyautoexcel',
    'version': '0.1.8',
    'description': '这是一个简单的操作 excel 的模块',
    'long_description': None,
    'author': 'wn0x00',
    'author_email': '320753691@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
