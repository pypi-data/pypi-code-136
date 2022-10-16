# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['function_by_svetlanakoroleva']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'function-by-svetlanakoroleva',
    'version': '0.1.0',
    'description': 'This is our test project',
    'long_description': '',
    'author': 'Svetlana Koroleva',
    'author_email': 'svetlanakoroleva312@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
