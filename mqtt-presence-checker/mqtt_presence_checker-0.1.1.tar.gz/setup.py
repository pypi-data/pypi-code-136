# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mqtt_presence_checker']

package_data = \
{'': ['*']}

install_requires = \
['asyncio-mqtt>=0.13.0,<0.14.0',
 'docstring-parser>=0.15,<0.16',
 'dotwiz>=0.4.0,<0.5.0',
 'jsonargparse>=4.15.1,<5.0.0',
 'loguru>=0.6.0,<0.7.0',
 'pingparsing>=1.4.0,<2.0.0',
 'pytest-asyncio>=0.19.0,<0.20.0',
 'pytest>=7.1.3,<8.0.0',
 'toml>=0.10.2,<0.11.0']

extras_require = \
{'docs': ['sphinxcontrib-napoleon>=0.7,<0.8',
          'sphinx>=5.3.0,<6.0.0',
          'sphinx-rtd-theme>=1.0.0,<2.0.0']}

entry_points = \
{'console_scripts': ['mqtt-presence-checker = '
                     'mqtt_presence_checker.__main__:main']}

setup_kwargs = {
    'name': 'mqtt-presence-checker',
    'version': '0.1.1',
    'description': 'Check if you (or your phone) is at home and notify your smarthome via mqtt!',
    'long_description': 'None',
    'author': 'RincewindWizzard',
    'author_email': 'git@magierdinge.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
