# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['retry_async']

package_data = \
{'': ['*']}

install_requires = \
['decorator>=5.1.1,<6.0.0']

setup_kwargs = {
    'name': 'retry-async',
    'version': '0.1.1',
    'description': '',
    'long_description': 'This is a fork of `https://github.com/invl/retry` that includes the ability to decorate async functions. See `https://github.com/invl/retry` for the README.\nAlso using the sync tests from the original repo.\n\n`pip install retry-async`\n\nFor mypy:\n\n`mypy retry_async`',
    'author': 'Jeremy Berman',
    'author_email': 'jerber@sas.upenn.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
