# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbml_builder']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy==1.4.41',
 'click>=8.1,<9.0',
 'funcy>=1.17,<2.0',
 'omymodels==0.12.1',
 'pydantic==1.10.2',
 'pydbml==1.0.3']

entry_points = \
{'console_scripts': ['model-build = dbml_builder.cli:main']}

setup_kwargs = {
    'name': 'dbml-builder',
    'version': '0.1.3',
    'description': '',
    'long_description': '# dbml-builder\nGenerates Pydantic and SQLAlchemy from a DBML file.\n',
    'author': 'Five Grant',
    'author_email': 'five@jataware.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
