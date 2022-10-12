# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_aizhan_user']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-aizhan-user',
    'version': '0.3.0',
    'description': 'This is our test project',
    'long_description': "# \n\n#### This is our test project.\n\n#### Please install this project.\n'''\npip install functions-by-aizhan-user\n\n'''\n\n#### You can also install older packages\n'''\npip install functions-by-aizhan-user==VERSION_NUMBER\n'''",
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
