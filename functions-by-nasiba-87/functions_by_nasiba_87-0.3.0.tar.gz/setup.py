# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_nasiba_87']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-nasiba-87',
    'version': '0.3.0',
    'description': '',
    'long_description': '# Instructions\n\n#### This is our first project.\n\n\n#### Please install this package\n```\n\npip install functions_by_nasiba_87\n```\n\n#### You can also install older packages\n\n```\npip install functions_by_nasiba_87==VERSION_NUMBER',
    'author': 'somename',
    'author_email': 'a@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
