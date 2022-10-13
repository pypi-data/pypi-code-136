# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['legendkit']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5,<4.0']

setup_kwargs = {
    'name': 'legendkit',
    'version': '0.2.5',
    'description': 'Legend creation and manipulation with ease for matplotlib',
    'long_description': '<p align="center">\n<img src="https://raw.githubusercontent.com/Mr-Milk/legendkit/main/images/legendkit-project.svg">\n</p>\n\n[![Documentation Status](https://img.shields.io/readthedocs/legendkit?logo=readthedocs&logoColor=white&style=flat-square)](https://legendkit.readthedocs.io/en/stable)\n![pypi version](https://img.shields.io/pypi/v/legendkit?color=blue&logo=python&logoColor=white&style=flat-square)\n\nWhen you want to create or adjust the legend in matplotlib, things can get dirty. \nLegendKit may solve your headache.\n\n<img src="https://raw.githubusercontent.com/Mr-Milk/legendkit/main/images/showcase.svg">\n\n## Features\n\n- Easy title placement and alignment\n- Easy colorbar with shape\n- Layout for multiple legends and colorbar*\n\n## Installation\n\n```shell\npip install legendkit\n```\n',
    'author': 'Mr-Milk',
    'author_email': 'yb97643@um.edu.mo',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Mr-Milk/legendkit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
