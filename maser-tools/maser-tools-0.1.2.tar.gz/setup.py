# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['maser',
 'maser.tools',
 'maser.tools.cdf',
 'maser.tools.cdf.cdfcompare',
 'maser.tools.cdf.serializer',
 'maser.tools.cdf.validator',
 'maser.tools.time']

package_data = \
{'': ['*'], 'maser.tools': ['support/cdf/*', 'support/data/*']}

install_requires = \
['numpy>=1.23.3,<2.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pytz>=2022.4,<2023.0',
 'spacepy>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'maser-tools',
    'version': '0.1.2',
    'description': '',
    'long_description': 'None',
    'author': 'MASER Team',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
