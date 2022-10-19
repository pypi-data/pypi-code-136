# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['totemp']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'totemp',
    'version': '0.2.0',
    'description': 'Temperature Converter',
    'long_description': '# ToTemp\n<div style="display: inline-block">\n  <img src="https://shields.io/pypi/v/totemp"  alt="package version"/>\n  <img src="https://img.shields.io/pypi/l/totemp.svg"  alt="license"/>\n</div>\n\n**ToTemp** is a temperature conversion package between Celcius, Delisle, Fahrenheit, Kelvin, Rankine, Reaumur, Newton and Romer\n\n## Usage\n\nFirst of all, install the package:\n\n```\npip install totemp\n```\n\nor, to have an example in poetry environments:\n\n```\npoetry add --group dev totemp\n```\n\nThen, just use it:\n\n> In these two examples, we want to know the equivalent in Fahrenheit\n> of 35º Celsius and 18.746º Celsius to Newton.\n\n```python\nfrom totemp import Celsius\n\ntemperature = Celsius.to_fahrenheit(35)  # Return: 95.0\n```\n```python\nfrom totemp import Celsius\n\ntemperature = Celsius.to_newton(18.746)  # Return: 6.186179999999999\n```\n\nNote that **all returns are *float values***, and that **applies to all methods**.\n\n## Versions\n\n- 0.1.0:\n  - Yanked, not functional\n- 0.2.0:\n  - Functional;\n  - Can convert Celsius to Delisle, Fahrenheit, Kelvin, Newton, Rankine, Réaumur and Rømer.\n\n## License\n\nFor more information, check LICENSE file.\n',
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
