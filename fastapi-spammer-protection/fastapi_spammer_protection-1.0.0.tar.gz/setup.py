# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_spammer_protection']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.85.1,<0.86.0']

setup_kwargs = {
    'name': 'fastapi-spammer-protection',
    'version': '1.0.0',
    'description': 'Middleware to protect a FastAPI app against spammers that try to exploit known vulnerabilities',
    'long_description': 'None',
    'author': 'Dogeek',
    'author_email': 'simon.bordeyne@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
