# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_build_testing_12345']

package_data = \
{'': ['*']}

install_requires = \
['requests']

extras_require = \
{'databases': ['boto3']}

setup_kwargs = {
    'name': 'awesome-mprox',
    'version': '0.1.9',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
