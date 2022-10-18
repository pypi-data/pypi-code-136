# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raicontours']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions']

setup_kwargs = {
    'name': 'raicontours',
    'version': '0.3.0.dev1',
    'description': '',
    'long_description': '# raicontours\n',
    'author': 'Simon Biggs',
    'author_email': 'simon.biggs@radiotherapy.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
