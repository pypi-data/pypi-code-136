# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioburst']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aioburst',
    'version': '0.1.0',
    'description': '',
    'long_description': '# aioburst\nA library to limit async calls using a waterwheel approach to ensure calls maximize the rate limit\n\nWARNING: This is an early release with minimal testing. The code is simple, but more tests are needed to make sure it works correctly.\n\n## Usage\n\n\n',
    'author': 'ericfeunekes',
    'author_email': 'ericwill.f@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
