# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['org_ical']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'google-api-python-client>=2.64.0,<3.0.0',
 'httplib2>=0.20.4,<0.21.0',
 'icalendar>=4.1.0,<5.0.0',
 'oauth2client>=4.1.3,<5.0.0',
 'omegaconf>=2.2.3,<3.0.0',
 'tzlocal>=4.2,<5.0']

setup_kwargs = {
    'name': 'org-ical',
    'version': '0.1.0',
    'description': 'Sync your org files to ical provider',
    'long_description': None,
    'author': 'Aleksandar Ivanovski',
    'author_email': 'aleksandar.ivanovski123@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
