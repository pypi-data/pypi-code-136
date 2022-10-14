# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sdk', 'sdk.mis']

package_data = \
{'': ['*']}

install_requires = \
['httpx==0.13.3', 'pre-commit==2.9.2', 'pydantic>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'mm-sdk',
    'version': '0.1.249',
    'description': '',
    'long_description': None,
    'author': 'dyus',
    'author_email': 'dyuuus@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
