# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omito_config_plugin_aws']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.89,<2.0.0', 'omito-config-core>=0.1.5,<0.2.0']

setup_kwargs = {
    'name': 'omito-config-plugin-aws',
    'version': '0.1.7',
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
