# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypipr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pypipr',
    'version': '0.1.1',
    'description': 'The Python Package Index Project',
    'long_description': '',
    'author': 'ufiapjj',
    'author_email': 'ufiapjj@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
