# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omito_config_plugin_env']

package_data = \
{'': ['*']}

install_requires = \
['omito-config-core>=0.1.5,<0.2.0']

setup_kwargs = {
    'name': 'omito-config-plugin-env',
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
