# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jwtdown_fastapi']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.81.0,<0.82.0',
 'passlib[bcrypt]>=1.7.4,<2.0.0',
 'python-jose[cryptography]>=3.3.0,<4.0.0',
 'python-multipart>=0.0.5,<0.0.6']

setup_kwargs = {
    'name': 'jwtdown-fastapi',
    'version': '0.3.0',
    'description': 'An easy-to-use authentication library for FastAPI.',
    'long_description': '# JWTdown for FastAPI\n\nThis is an easy-to-use authentication mechanism for FastAPI.\n\nIt draws inspiration from the tutorials found in the FastAPI\ndocumentation.\n\nPlease read the\n[documentation](https://jwtdown-fastapi.readthedocs.io/en/latest/intro.html)\nto use this project.\n\n## Developing\n\nDevelopment on this project is limited to employees,\ncontractors, and students of Galvanize, Inc.\n\n',
    'author': 'Galvanize, Inc.',
    'author_email': 'foss@galvanize.com',
    'maintainer': 'Daniel Billotte',
    'maintainer_email': 'daniel.billotte@galvanize.com',
    'url': 'https://gitlab.com/galvanize-inc/foss/jwtdown-fastapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
