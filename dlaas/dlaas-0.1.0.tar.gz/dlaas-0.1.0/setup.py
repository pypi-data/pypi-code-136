# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dlaas']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dlaas',
    'version': '0.1.0',
    'description': 'Deep Learning as a service',
    'long_description': '# Deep Learning as a Service',
    'author': 'rcmalli',
    'author_email': 'refikcanmalli@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
