# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.', 'psycopg2': './psycopg2'}

packages = \
['psycopg2',
 'puff',
 'puff.contrib',
 'puff.contrib.django',
 'puff.contrib.django.postgres']

package_data = \
{'': ['*']}

install_requires = \
['greenlet>=1.1,<2.0']

setup_kwargs = {
    'name': 'puff-py',
    'version': '0.1.0',
    'description': 'Python support for Puff',
    'long_description': 'None',
    'author': 'Kyle Hanson',
    'author_email': 'me@khanson.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hansonkd/puff',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
