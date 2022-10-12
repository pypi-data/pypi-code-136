# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_ambrosi91']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-ambrosi91',
    'version': '0.3.0',
    'description': 'This is a test project.',
    'long_description': '# Instructions\n\n#### This is our test project\n#### Please install this package\n```\npip install functions-by-ambrosi91\n```\n\n#### You can also install older packages\n```\npip install functions-by-ambrosi91==VERSION_NUMBER\n```',
    'author': 'ambrosi91',
    'author_email': 'ambrosi11151991@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
