# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logfmt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'logfmt-julian-sobott',
    'version': '0.1.0',
    'description': 'Logging Formatter to format log messages in logfmt format',
    'long_description': None,
    'author': 'JulianSobott',
    'author_email': 'julian.sobott@mail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/JulianSobott/python-logfmt',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
