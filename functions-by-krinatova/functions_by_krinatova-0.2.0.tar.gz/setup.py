# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_krinatova']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-krinatova',
    'version': '0.2.0',
    'description': 'This is our test project',
    'long_description': '# Instractions \n\n#### This is our test project.',
    'author': 'Kanykei Rinatova',
    'author_email': 'krdevops22@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
