# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seiwhale']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['sei = seiwhale.cli:run']}

setup_kwargs = {
    'name': 'seiwhale',
    'version': '0.0.1',
    'description': 'Rapid Dockerfile generator',
    'long_description': None,
    'author': 'Naruhide KITADA',
    'author_email': 'kitfactory@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
