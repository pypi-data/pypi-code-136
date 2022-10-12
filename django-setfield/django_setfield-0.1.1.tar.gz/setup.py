# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_set_field', 'django_set_field.contrib.rest_framework']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.1.2,<5.0.0', 'djangorestframework>=3.14.0,<4.0.0']

setup_kwargs = {
    'name': 'django-setfield',
    'version': '0.1.1',
    'description': 'Django model field to handle sets (in the python/math sense)',
    'long_description': 'None',
    'author': 'Alban Siffer',
    'author_email': 'alban.siffer@irisa.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
