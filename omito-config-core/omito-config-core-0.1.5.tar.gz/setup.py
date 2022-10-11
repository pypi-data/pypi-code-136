# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omito_config_core']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'deepmerge>=1.0.1,<2.0.0',
 'flatten-dict>=0.4.2,<0.5.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'schematics>=2.1.1,<3.0.0']

setup_kwargs = {
    'name': 'omito-config-core',
    'version': '0.1.5',
    'description': '',
    'long_description': 'None',
    'author': 'Barath Kumar',
    'author_email': 'barath@mergedup.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
