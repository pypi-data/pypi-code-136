# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cool_ip_api', 'cool_ip_api.provider', 'cool_ip_api.utils']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'pydantic>=1.10.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'cool-ip-api',
    'version': '0.1.1',
    'description': 'A collections of wrapper for different IP info APIs',
    'long_description': '# cool-ip-api\nA package to get information from an IP using a collection of IP info apis.\n',
    'author': 'sokripon',
    'author_email': 'sokripon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sokripon/cool-ip-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
