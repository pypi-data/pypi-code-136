# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_nomadstalker']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-nomadstalker',
    'version': '0.1.0',
    'description': 'This is our test project',
    'long_description': '',
    'author': 'Omurbek Orozaliev',
    'author_email': 'boexpresskg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
