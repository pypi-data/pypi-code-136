# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_resources',
 'fastapi_resources.resources',
 'fastapi_resources.resources.sqlmodel',
 'fastapi_resources.routers',
 'fastapi_resources.routers.json_api_router']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.85.0,<0.86.0', 'sqlmodel>=0.0.8,<0.0.9']

setup_kwargs = {
    'name': 'fastapi-resources',
    'version': '0.2.14',
    'description': '',
    'long_description': 'None',
    'author': 'Ben Davis',
    'author_email': 'ben@bencdavis.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
