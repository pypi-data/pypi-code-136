# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_dimdate', 'tap_dimdate.tests']

package_data = \
{'': ['*'], 'tap_dimdate': ['schemas/*']}

install_requires = \
['singer-sdk>=0.11.1,<0.12.0']

entry_points = \
{'console_scripts': ['tap-dimdate = tap_dimdate.tap:TapDimDate.cli']}

setup_kwargs = {
    'name': 'tap-dimdate',
    'version': '0.0.1',
    'description': '`tap-dimdate` is a Singer tap for generating a date dimension, built with the Meltano Singer SDK.',
    'long_description': 'None',
    'author': 'Neil McGuigan',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
