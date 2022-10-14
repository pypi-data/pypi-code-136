# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_marieane22']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-marieane22',
    'version': '0.4.0',
    'description': 'This is a test project.',
    'long_description': '# Instructions\n\n#### This is our test project.\n\n#### Please install this package\n```\npip install functions-by-marieane22==0.4.0\n```\n#### You can also install older packages\n```\npip install functions-by-marieane22==(VERSION HERE)\n```',
    'author': 'marieane22',
    'author_email': 'marieane@live.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
