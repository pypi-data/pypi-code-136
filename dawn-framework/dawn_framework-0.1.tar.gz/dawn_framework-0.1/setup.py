# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dawn']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dawn-framework',
    'version': '0.1',
    'description': 'DawnFramework',
    'long_description': '# DawnFramework',
    'author': 'Sergey Shikhovtsov',
    'author_email': 'sh.sergey.yur@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/dawn-framework/dawn-framework',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
