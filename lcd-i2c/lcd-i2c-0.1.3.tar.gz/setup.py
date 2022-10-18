# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lcd_i2c', 'lcd_i2c.helpers']

package_data = \
{'': ['*']}

install_requires = \
['smbus2>=0.4.2,<0.5.0']

setup_kwargs = {
    'name': 'lcd-i2c',
    'version': '0.1.3',
    'description': 'Library for interacting with an I2C LCD screen through Python',
    'long_description': 'Basic library for interacting with I2C LCD screens.\n\nTested using a Raspberry Pi Zero 2W.\n',
    'author': 'Federico Giancarelli',
    'author_email': 'hello@federicogiancarelli.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
