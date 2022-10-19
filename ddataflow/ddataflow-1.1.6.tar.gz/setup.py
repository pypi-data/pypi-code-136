# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ddataflow', 'ddataflow.sampling', 'ddataflow.setup']

package_data = \
{'': ['*']}

install_requires = \
['databricks-cli>=0.16', 'fire>=0.4', 'oauthlib>=3.2.1', 'pyspark>3']

entry_points = \
{'console_scripts': ['ddataflow = ddataflow.ddataflow:main']}

setup_kwargs = {
    'name': 'ddataflow',
    'version': '1.1.6',
    'description': 'A tool for end2end data tests',
    'long_description': 'None',
    'author': 'Data products GYG',
    'author_email': 'engineering.data-products@getyourguide.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
