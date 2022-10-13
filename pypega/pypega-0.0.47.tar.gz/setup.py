# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypega']

package_data = \
{'': ['*']}

install_requires = \
['requests-oauthlib>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'pypega',
    'version': '0.0.47',
    'description': 'Python package for orchestrating Pega environments',
    'long_description': '# pyPega (Python for Pega)\n\nPython package for orchestrating Pega environments - details coming soon.',
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
