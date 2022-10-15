# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['random_quote_generator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'random-quote-generator-2xb3',
    'version': '0.1.0',
    'description': 'A random quote generator',
    'long_description': '# A Modern Python Project Workflow\n\nFrom [this excellent article](https://testdriven.io/blog/python-project-workflow/) on testdriven.io.\n',
    'author': 'Laurent VAYLET',
    'author_email': 'laurent.vaylet@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
