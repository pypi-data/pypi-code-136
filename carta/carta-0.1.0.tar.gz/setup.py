# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['carta']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'carta',
    'version': '0.1.0',
    'description': 'Python library for making GUI applications on the ReMarkable tablet wrapped around the "simple" application',
    'long_description': '# Carta\nPython library for making GUI applications on the ReMarkable tablet wrapped around the "simple" application\n',
    'author': 'JaySec',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
