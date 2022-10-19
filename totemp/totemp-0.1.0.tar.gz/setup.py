# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['totemp']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'totemp',
    'version': '0.1.0',
    'description': 'Temperature Converter',
    'long_description': '# ToTemp\n<div style="display: inline-block">\n  <img src="https://shields.io/pypi/v/totemp"  alt="package version"/>\n  <img src="https://img.shields.io/pypi/l/totemp.svg"  alt="license"/>\n</div>\n\n**ToTemp** is a temperature conversion package between Celcius, Delisle, Fahrenheit, Kelvin, Rankine, Reaumur, Newton and Romer\n',
    'author': 'Edson Pimenta',
    'author_email': 'edson.tibo@gmail.com',
    'maintainer': 'Edson Pimenta',
    'maintainer_email': 'edson.tibo@gmail.com',
    'url': 'https://github.com/eddyyxxyy/ToTemp',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
