# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_alpkocer3']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-alpkocer3-py',
    'version': '0.3.0',
    'description': 'Test Project',
    'long_description': '# Instructions\n\n### This is our test project.\n\n### Please install this package:\n```\npip install functions-by-alpkocer3-py\n```\n\n### You can also install older package:\n```\npip install functions-by-alpkocer3-py==VERSION_NUMBER\n```\n\n',
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
