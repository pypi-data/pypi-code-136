# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_gregvalico']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-gregvalico',
    'version': '0.3.0',
    'description': 'This is a test project.',
    'long_description': '# Instructions\n\n#### This is our test project.\n#### Please install this package\n```\npip install functions-by-gregvalico==0.2.0\n```\n#### You can also install older packages\n```\npip install functions-by-gregvalico==(VERSION HERE)\n```',
    'author': 'GregValico',
    'author_email': 'GregValico@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
