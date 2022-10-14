# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arxiv_db', 'arxiv_db.models', 'arxiv_db.tables']

package_data = \
{'': ['*']}

install_requires = \
['sqlalchemy>=1.4,<2.0']

setup_kwargs = {
    'name': 'arxiv-db',
    'version': '0.12.0',
    'description': 'SQLAlchemy models for arXiv DB tables',
    'long_description': 'None',
    'author': 'Brian D. Caruso',
    'author_email': 'bdc34@cornell.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
