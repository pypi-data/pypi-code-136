# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vinor']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vinor',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Vinor\n\nFull-stack Web Framework',
    'author': 'VinorTeam',
    'author_email': 'opensource@vinor.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
