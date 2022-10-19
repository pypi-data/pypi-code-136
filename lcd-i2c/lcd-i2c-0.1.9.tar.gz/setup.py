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
    'version': '0.1.9',
    'description': 'Library for interacting with an I2C LCD screen through Python',
    'long_description': "# LCD I2C\n## Use an I2C LCD with Python\n\nBasic library for interacting with I2C LCD screens. It started off as a Python port of the Arduino [LiquidCristal_I2C](https://github.com/johnrickman/LiquidCrystal_I2C/) library and ended up implementing an object oriented API, for easier use.\n\nTested using a Raspberry Pi Zero 2W.\n\n## Examples\n\n### Connect to LCD screen and print some text:\n\n```python\nfrom lcd_i2c import LCD_I2C\n\nlcd = LCD_I2C(39, 16, 2)\n\n# Turn on the backlight\nlcd.backlight.on()\n\n# Show the blinking cursor\nlcd.blink.on()\n# or:\n# lcd.cursor.blink.on()\n\n# Print some text\nlcd.write_text('Hola!')\n```\n",
    'author': 'Federico Giancarelli',
    'author_email': 'hello@federicogiancarelli.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/omirete/lcd-i2c',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
