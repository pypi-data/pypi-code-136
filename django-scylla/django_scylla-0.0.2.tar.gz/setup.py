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
    'version': '0.0.2',
    'description': 'Django Scylla',
    'long_description': '# Django Scylla - the Cassandra & ScyllaDB backend for Django\n\nDjango-scylla makes possible to connect your Django app to Cassandra or ScyllaDB and **use native Django ORM** as with any other relational database backend.\n\n\n[![Latest version](https://img.shields.io/pypi/v/django-scylla.svg "Latest version")](https://pypi.python.org/pypi/django-scylla/)\n![workflow](https://github.com/r4fek/django-scylla/actions/workflows/tox.yml/badge.svg)\n\nDiscord: https://discord.gg/pxunMGmDNc\n\n## Sponsors ##\nHelp support ongoing development and maintenance by [sponsoring Django Scylla](https://github.com/sponsors/r4fek).\n\n## Installation ##\n\nRecommended installation:\n\n    pip install django-scylla\n\n## Basic Usage ##\n\n1. Add `django_scylla` to `INSTALLED_APPS` in your `settings.py` file:\n\n        INSTALLED_APPS = (\'django_scylla\',) + INSTALLED_APPS\n\n2. Change `DATABASES` setting:\n\n        DATABASES = {\n            \'default\': {\n                \'ENGINE\': \'django_scylla\',\n                \'NAME\': \'db\',\n                \'TEST_NAME\': \'test_db\',\n                \'HOST\': \'db1.example.com,db2.example.com,db3.example.com\',\n                \'OPTIONS\': {\n                    \'consistency_level\': ...,\n                    \'load_balancing_policy\': ...,\n                    \'retry_policy\': ...,\n                    \'request_timeout\': 10,\n\n                }\n            }\n        }\n\n3. Define some model:\n\n        # myapp/models.py\n\n        from django.db import models\n\n\n        class Person(models.Model):\n            first_name = models.CharField(max_length=30)\n            last_name = models.CharField(max_length=30)\n\n\n4. Connect to ScyllaDB and create a keyspace.\n5. Run `./manage.py makemigrations && ./manage.py migrate`\n6. Done!\n\n## License ##\nCopyright (c) 2021-2022, [Rafał Furmański](https://linkedin.com/in/furmanski).\n\nAll rights reserved. Licensed under MIT License.\n',
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
