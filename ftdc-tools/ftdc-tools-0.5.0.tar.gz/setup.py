# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ftdc_tools', 'ftdc_tools.rollups']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.4,<2.0.0', 'pymongo>=4.2.0,<5.0.0']

setup_kwargs = {
    'name': 'ftdc-tools',
    'version': '0.5.0',
    'description': '',
    'long_description': 'None',
    'author': 'Alexander Costas',
    'author_email': 'alexander.costas@mongodb.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
