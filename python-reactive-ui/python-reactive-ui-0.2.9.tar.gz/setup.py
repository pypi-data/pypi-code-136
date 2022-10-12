# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_reactive_ui',
 'python_reactive_ui.backends',
 'python_reactive_ui.backends.gtk3',
 'python_reactive_ui.backends.gtk3.builtin',
 'python_reactive_ui.lib']

package_data = \
{'': ['*']}

install_requires = \
['PyGObject>=3.42.2,<4.0.0']

entry_points = \
{'console_scripts': ['example = python_reactive_ui.main:test']}

setup_kwargs = {
    'name': 'python-reactive-ui',
    'version': '0.2.9',
    'description': '',
    'long_description': '# python-reactive-ui\n\nHave you ever wanted to use React, only to stumble upon the realization that\nyour project uses Python and GTK for the UI? Grieve no more, my friend, for this\nproject seeks to save you from your choices.\n\nAttach components to arbitrary GTK containers.\n',
    'author': 'Manuel Brea',
    'author_email': 'm.brea.carreras@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
