# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rlaas']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rlaas',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Reinforcement Learning as a service',
    'author': 'rcmalli',
    'author_email': 'refikcanmalli@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
