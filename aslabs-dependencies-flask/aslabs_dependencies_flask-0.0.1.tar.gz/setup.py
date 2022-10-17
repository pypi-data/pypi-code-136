# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aslabs', 'aslabs.dependencies.flask']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.0.3,<3.0.0', 'aslabs-dependencies']

setup_kwargs = {
    'name': 'aslabs-dependencies-flask',
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
