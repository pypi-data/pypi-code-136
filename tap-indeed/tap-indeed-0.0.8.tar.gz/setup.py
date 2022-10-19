# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_indeedsponsoredjobs', 'tap_indeedsponsoredjobs.tests']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=2.2.0,<3.0.0',
 'cloudscraper==1.2.64',
 'requests>=2.25.1,<3.0.0',
 'singer-sdk>=0.11.0,<0.12.0']

entry_points = \
{'console_scripts': ['tap-indeedsponsoredjobs = '
                     'tap_indeedsponsoredjobs.tap:TapIndeedSponsoredJobs.cli']}

setup_kwargs = {
    'name': 'tap-indeed',
    'version': '0.0.8',
    'description': '`tap-indeed` is a Singer tap for IndeedSponsoredJobs, built with the Meltano SDK for Singer Taps.',
    'long_description': None,
    'author': 'AutoIDM',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
