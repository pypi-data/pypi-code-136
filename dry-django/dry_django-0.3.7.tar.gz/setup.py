# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dry_django',
 'dry_django.contrib',
 'dry_django.contrib.rest_framework',
 'dry_django.selectors',
 'dry_django.services',
 'dry_django.utils']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.1.0,<5.0.0',
 'django-filter>=22.1,<23.0',
 'djangorestframework>=3.14.0,<4.0.0',
 'dry-core>=0.5.5,<0.6.0',
 'mkdocstrings[crystal,python]>=0.19.0,<0.20.0']

setup_kwargs = {
    'name': 'dry-django',
    'version': '0.3.7',
    'description': '',
    'long_description': '# Dry-core\n\n`dry-core` is core package of `dry-*` package series. Main goal \nis to minimize and power up code, make it clear and easy supportable.\n\nDocumentation will be available soon.\n',
    'author': 'Илья Маркевич',
    'author_email': 'samuray21x@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
