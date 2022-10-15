# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_scylla', 'django_scylla.cql']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.0,<5.0', 'scylla-driver>=3.25,<4.0']

setup_kwargs = {
    'name': 'django-scylla',
    'version': '0.0.1',
    'description': 'Django Scylla',
    'long_description': '# django-scylla (WIP)\n',
    'author': 'Rafał Furmański',
    'author_email': 'r.furmanski@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/r4fek/django-scylla',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
