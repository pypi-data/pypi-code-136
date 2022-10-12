# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_alpkocer3']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-alpkocer3-py',
    'version': '0.2.0',
    'description': 'Test Project',
    'long_description': '# Instructions\n\n### This is our test project.',
    'author': 'Alp Kocer',
    'author_email': 'gokalpkocer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
