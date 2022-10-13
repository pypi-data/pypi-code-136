# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_xujajon89']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-xujajon89',
    'version': '0.2.0',
    'description': 'This is our test project',
    'long_description': '# Instructions\n\n#### This is our test project.\n',
    'author': 'Sarvarkhuja Tursinov',
    'author_email': 'xujajon89@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
