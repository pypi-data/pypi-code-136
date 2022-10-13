# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_twined',
 'django_twined.admin',
 'django_twined.consumers',
 'django_twined.management',
 'django_twined.management.commands',
 'django_twined.migrations',
 'django_twined.models',
 'django_twined.models.querysets',
 'django_twined.signals',
 'django_twined.templatetags']

package_data = \
{'': ['*'],
 'django_twined': ['static/*',
                   'templates/admin/*',
                   'templates/django_twined/*']}

install_requires = \
['channels>=3.0,<4.0',
 'django-gcp>=0.7.3,<0.8.0',
 'django-jsoneditor>=0.2.2,<0.3.0',
 'django-model-utils>=4.2.0,<5.0.0',
 'django>=3.0,<4.0',
 'octue>=0.39.0,<0.40.0',
 'pika>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'django-twined',
    'version': '0.4.1',
    'description': 'A django app to manage octue services',
    'long_description': "[![PyPI version](https://badge.fury.io/py/django-twined.svg)](https://badge.fury.io/py/django-twined)\n[![codecov](https://codecov.io/gh/octue/django-twined/branch/master/graph/badge.svg)](https://codecov.io/gh/octue/django-twined)\n[![Documentation Status](https://readthedocs.org/projects/django-twined/badge/?version=latest)](https://django-twined.readthedocs.io/en/latest/?badge=latest)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\n# Django Twined\n\nThis is a plugin for django, enabling you to orchestrate [twined-based octue services](https://octue.readthedocs.io) services from your own django\nserver.\n\nDocumentation is [here](https://django-twined.readthedocs.io/en/latest/).\n\nThis is great for advanced use cases where:\n\n- you have specific security/firewalling requirements, or\n- you want to manage your own auth, or\n- you have specific/unusual data integration needs, or\n- already have a web based data service, and want to expose it in the twined ecosystem.\n\n**Health warning:** to use this plugin to deploy your services, you'll need to handle all your own data\nstorage/orchestration, devops, server management, security and auth. So for most users we'd recommend getting in touch at\n[octue.com](https://www.octue.com/contact) so we can help!\n",
    'author': 'Tom Clark',
    'author_email': 'tom@octue.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/octue/django-twined',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
