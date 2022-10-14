# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tfdiagrams', 'tfdiagrams.console']

package_data = \
{'': ['*'], 'tfdiagrams': ['resources/*']}

install_requires = \
['diagrams>=0.22.0,<0.23.0', 'pydot>=1.4.2,<2.0.0']

entry_points = \
{'console_scripts': ['tfdot = tfdiagrams.console:main']}

setup_kwargs = {
    'name': 'tfdiagrams',
    'version': '0.2.3',
    'description': '',
    'long_description': 'None',
    'author': 'Tetsuya Shinone',
    'author_email': 'info@semnil.com',
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
