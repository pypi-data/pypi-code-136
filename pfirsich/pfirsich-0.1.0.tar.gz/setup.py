# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pfirsich', 'pfirsich.func']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pfirsich',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Yixuan-Wang',
    'author_email': 'tom-yixuan_wang@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
