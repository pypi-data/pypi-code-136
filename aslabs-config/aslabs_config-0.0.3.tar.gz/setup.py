# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aslabs', 'aslabs.config']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'aslabs-config',
    'version': '0.0.3',
    'description': 'Universal configuration system, that maps your env vars, json file and dotenv to dataclass configs',
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
