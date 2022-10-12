# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_dinara93']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-dinara93',
    'version': '0.2.0',
    'description': 'This is our test project',
    'long_description': '# Instructions\n\n#### This is our test project.\n#### Please install this packages\n```\npip install functions-by-dinara93\n```\n\n### You can also install older packages\n```\npip install functions-by-dinara93==VERSION NUMBER\n```',
    'author': 'Dinara Aidarova',
    'author_email': 'fordinara93@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
