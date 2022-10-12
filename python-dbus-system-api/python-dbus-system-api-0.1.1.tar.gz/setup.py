# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_dbus_system_api', 'python_dbus_system_api.interfaces']

package_data = \
{'': ['*']}

install_requires = \
['dbus-next>=0.2.3,<0.3.0', 'pulsectl-asyncio>=0.2.3,<0.3.0']

entry_points = \
{'console_scripts': ['pysysapi = python_dbus_system_api.main:start_server']}

setup_kwargs = {
    'name': 'python-dbus-system-api',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
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
