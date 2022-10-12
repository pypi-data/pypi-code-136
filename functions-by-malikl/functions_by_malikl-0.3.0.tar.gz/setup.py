# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_malikl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-malikl',
    'version': '0.3.0',
    'description': '',
    'long_description': '### math function ###',
    'author': 'Your MalikL',
    'author_email': 'quepasadewie@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
