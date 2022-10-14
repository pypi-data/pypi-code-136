# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['factly', 'factly.standard_names']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'factly-standard-names',
    'version': '0.1.1',
    'description': '',
    'long_description': 'None',
    'author': 'Factly Labs',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
