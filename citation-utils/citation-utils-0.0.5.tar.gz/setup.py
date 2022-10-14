# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['citation_utils']

package_data = \
{'': ['*']}

install_requires = \
['citation-docket>=0.0.6,<0.0.7',
 'citation-report>=0.0.3,<0.0.4',
 'pydantic>=1.10.2,<2.0.0',
 'python-slugify>=6.1.2,<7.0.0']

setup_kwargs = {
    'name': 'citation-utils',
    'version': '0.0.5',
    'description': 'Regex-based docket and report formula for Citations found in Philippine Supreme Court Decisions',
    'long_description': 'None',
    'author': 'Marcelino G. Veloso III',
    'author_email': 'mars@veloso.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
