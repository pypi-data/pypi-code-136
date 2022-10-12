# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_Aizhan_user']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-aizhan-user',
    'version': '0.1.0',
    'description': 'This is our test project',
    'long_description': '',
    'author': 'Aizhan Myrzakimova',
    'author_email': 'amyrzakimova@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
