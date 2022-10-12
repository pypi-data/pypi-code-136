# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cyral_django_wrapper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cyral-django-wrapper',
    'version': '0.1.26',
    'description': 'Enriches your Django database queries with user identity information',
    'long_description': 'None',
    'author': 'Cyral',
    'author_email': 'support@cyral.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
