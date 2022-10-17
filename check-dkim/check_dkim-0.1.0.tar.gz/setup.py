# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['check_dkim']

package_data = \
{'': ['*']}

install_requires = \
['click', 'dkimpy']

entry_points = \
{'console_scripts': ['check-dkim = check_dkim:main']}

setup_kwargs = {
    'name': 'check-dkim',
    'version': '0.1.0',
    'description': 'A simple CLI script to verify DKIM signatures on EML files',
    'long_description': '# check-dkim\n\nA simple CLI script to verify DKIM signatures on EML files.\n',
    'author': 'Micah Lee',
    'author_email': 'micah@micahflee.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
