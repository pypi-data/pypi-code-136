# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_madina3006']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-madina3006',
    'version': '0.3.0',
    'description': 'This is our test project',
    'long_description': '# Instructions \n\n#### This is our test project. \n#### Please install this package \n```\npip install functions-by-madina3006\n```\n\n#### You can also install older version \n```\npip install functions-by-madina3006==VERSION_NUMBER\n```',
    'author': 'Madina Shumbolova',
    'author_email': 'madina.shumbolova@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
