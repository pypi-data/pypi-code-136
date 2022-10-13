# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypega_dm']

package_data = \
{'': ['*']}

install_requires = \
['pypega>=0.0.47']

setup_kwargs = {
    'name': 'pypega-dm',
    'version': '0.0.21',
    'description': 'Python package for orchestrating Pega environments',
    'long_description': '# pyPega Deployment Manager (Python)\n\nPython package for orchestrating Pega Deployment Manager - details coming soon',
    'author': 'Rob Smart',
    'author_email': 'rob.smart@pega.com',
    'maintainer': 'Rob Smart',
    'maintainer_email': 'rob.smart@pega.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
