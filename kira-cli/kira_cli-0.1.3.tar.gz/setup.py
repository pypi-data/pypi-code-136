# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli_template']

package_data = \
{'': ['*']}

install_requires = \
['pre-commit>=2.20.0,<3.0.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['kira-cli = cli_template.main:app']}

setup_kwargs = {
    'name': 'kira-cli',
    'version': '0.1.3',
    'description': '',
    'long_description': '# Portal Gun\n\nThe awesome Portal Gun\n',
    'author': 'Tristan Leonard',
    'author_email': 'trisco2001@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
