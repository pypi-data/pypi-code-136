# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_cloudproject']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-cloudproject',
    'version': '0.2.0',
    'description': 'This is our test project',
    'long_description': '# Instarunctions\n\n#### This is our test project',
    'author': 'Cloud',
    'author_email': 'cloudproject092022@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
