# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aslabs', 'aslabs.dependencies.gcp.cloud_tasks']

package_data = \
{'': ['*']}

install_requires = \
['aslabs-dependencies>=0.0.3,<0.0.4', 'google-cloud-tasks>=2.9.0,<3.0.0']

setup_kwargs = {
    'name': 'aslabs-dependencies-gcp-cloud-tasks',
    'version': '0.0.1',
    'description': '',
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
