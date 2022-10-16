# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['beancount_exporter']

package_data = \
{'': ['*']}

install_requires = \
['beancount-data>=0.1.4,<0.2.0',
 'beancount>=2.3.5,<3.0.0',
 'click>=8.0.4,<9.0.0']

setup_kwargs = {
    'name': 'beancount-exporter',
    'version': '0.1.4',
    'description': 'Command line tool for exporting Beancount data as JSON',
    'long_description': None,
    'author': 'Fang-Pen Lin',
    'author_email': 'fangpen@launchplatform.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
