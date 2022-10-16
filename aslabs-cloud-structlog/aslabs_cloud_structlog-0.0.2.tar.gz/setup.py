# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloud_structlog']

package_data = \
{'': ['*']}

install_requires = \
['structlog>=22.1.0,<23.0.0']

setup_kwargs = {
    'name': 'aslabs-cloud-structlog',
    'version': '0.0.2',
    'description': 'Cloud ready configuration of structlog',
    'long_description': '',
    'author': 'Titusz Ban',
    'author_email': 'tituszban@antisociallabs.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
