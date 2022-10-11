# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tidyverse']

package_data = \
{'': ['*']}

install_requires = \
['plotnine>=0.10.1,<0.11.0', 'siuba>=0.3.0,<0.4.0']

setup_kwargs = {
    'name': 'tidyverse',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'edavidaja',
    'author_email': 'self@edavidaja.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
