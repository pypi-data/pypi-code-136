# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_welkin',
 'django_welkin.management',
 'django_welkin.management.commands',
 'django_welkin.migrations',
 'django_welkin.models']

package_data = \
{'': ['*']}

install_requires = \
['django-solo>=2.0.0,<3.0.0', 'welkin>=0.0.6,<0.0.7']

setup_kwargs = {
    'name': 'django-welkin',
    'version': '0.0.1b1',
    'description': 'A Django app interfacing with the Welkin API.',
    'long_description': '# Welkin\n\nWelkin is a Django app to connect to the Welkin Health API.\n\n## Quick start\n\n1. Install django-welkin with pip:\n\n```\npip install django-welkin\n```\n\n2. Add django-welkin and django-solo to your INSTALLED_APPS setting like this:\n\n```python\nINSTALLED_APPS = [\n    ...\n    "solo",\n    \'django_welkin\',\n]\n```\n\n3. Include the django-welkin URLconf in your project urls.py like this:\n\n```python\npath(\'welkin/\', include(\'django_welkin.urls\')),\n```\n\n4. Run `python manage.py migrate` to create the welkin models.\n\n5. Start the development server and visit http://localhost:8000/admin/welkin/configuration/\n   to and add API secrets to the singleton (you\'ll need the Admin app enabled).\n',
    'author': 'Sam Morgan',
    'author_email': 'sam@lightmatter.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/django-welkin/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
