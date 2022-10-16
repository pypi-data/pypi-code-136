# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aslabs', 'aslabs.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aslabs-utils',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'Titusz Ban',
    'author_email': 'tituszban@antisociallabs.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
