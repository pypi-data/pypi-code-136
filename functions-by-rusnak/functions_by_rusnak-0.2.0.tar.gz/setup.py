# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_rusnak']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-rusnak',
    'version': '0.2.0',
    'description': 'This is our test project',
    'long_description': '#instructions\n\n### This is our test project.\n',
    'author': 'Kateryna Rusnak',
    'author_email': 'minipytka888@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
