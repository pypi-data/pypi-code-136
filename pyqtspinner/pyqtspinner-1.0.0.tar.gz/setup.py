# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyqtspinner']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>5.8']

entry_points = \
{'console_scripts': ['pyqtspinner-conf = pyqtspinner.configurator:main']}

setup_kwargs = {
    'name': 'pyqtspinner',
    'version': '1.0.0',
    'description': 'Waiting spinner for PyQt5',
    'long_description': None,
    'author': 'Denis',
    'author_email': 'fbjorn@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
