# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_outbox',
 'python_outbox.base',
 'python_outbox.generic',
 'python_outbox.sqlalchemy_outbox']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy-Utils>=0.38.3,<0.39.0',
 'SQLAlchemy>=1.4.40,<2.0.0',
 'black>=22.8.0,<23.0.0',
 'cloudevents>=1.6.1,<2.0.0',
 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'python-outbox',
    'version': '0.1.8',
    'description': 'Implement the outbox pattern in a generic way for python projects.',
    'long_description': '# Python-Outbox\n\nPython-outbox is a library that implement the Outbox pattern.\n\nIt try to separate concerns of retrieving and publishing events in the pattern, allowing a generic implementation for any use case you would want.',
    'author': 'Sami Tahri',
    'author_email': 'sismixx@hotmail.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Smixi/python-outbox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
