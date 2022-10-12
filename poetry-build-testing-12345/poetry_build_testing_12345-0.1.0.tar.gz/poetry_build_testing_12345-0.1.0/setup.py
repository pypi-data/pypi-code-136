# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_build_testing_12345']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

extras_require = \
{'boto3': ['boto3[boto3]>=1.24.89,<2.0.0']}

setup_kwargs = {
    'name': 'poetry-build-testing-12345',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Matthew',
    'author_email': 'matthew.proxenos@genomicsengland.co.uk',
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
