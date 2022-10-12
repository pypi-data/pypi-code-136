# -*- coding: utf-8 -*-
from setuptools import setup
from datetime import datetime
import time

print(datetime.now().isoformat())
packages = \
['test_xfilter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'test-xfilter',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}
time.sleep(10)

print(datetime.now().isoformat())

setup(**setup_kwargs)
