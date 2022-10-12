# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['devind_helpers',
 'devind_helpers.files',
 'devind_helpers.generators',
 'devind_helpers.import_from_file',
 'devind_helpers.mutation_factories',
 'devind_helpers.permissions',
 'devind_helpers.schema',
 'devind_helpers.validator']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.12,<5.0.0',
 'flatten-dict>=0.4.2,<0.5.0',
 'graphene-django-optimizer>=0.8.0,<0.9.0',
 'graphene-django>=2.15.0,<3.0.0',
 'inflection>=0.5.1,<0.6.0',
 'openpyxl>=3.0.9,<4.0.0',
 'redis>=4.1.4,<5.0.0']

setup_kwargs = {
    'name': 'devind-helpers',
    'version': '0.7.0',
    'description': 'Devind helpers.',
    'long_description': '# Devind helpers python library.',
    'author': 'Victor',
    'author_email': 'lyferov@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/devind-team/devind-django-helpers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
