# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_alextsiasto']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-alextsiasto',
    'version': '0.3.0',
    'description': 'This is our test project',
    'long_description': '# Instructions\n\n#### This is our test project.\n#### Please install this pacage\n```\npip install functions-by-alextsiasto\n```\n\n#### You can also install older version\n```\npip install functions-by-alextsiasto==VERSION_NUMBER\n```',
    'author': 'Alex Tsiasto',
    'author_email': 'alex.tsiasto@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
