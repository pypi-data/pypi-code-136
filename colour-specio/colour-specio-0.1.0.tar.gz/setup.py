# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['specio', 'specio.ColorimetryResearch']

package_data = \
{'': ['*']}

install_requires = \
['aenum>=3.1.11,<4.0.0',
 'colour-science==0.4.1',
 'numpy>=1.23.1,<2.0.0',
 'pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'colour-specio',
    'version': '0.1.0',
    'description': 'Instrument control for spectrometers',
    'long_description': '# Specio\n\nSpecio is a python library for interacting with spectrometers. Currently only\nthe Colorimetry Research family is supported, and particularly this library is\ntested and maintained with a CR300.\n\nThis library also provides a virtual spectrometer which provides semi-random\nSPDs as measurements.\n\n## Usage\n\nSee Examples Folder\n',
    'author': 'Tucker',
    'author_email': 'tucker@tuckerd.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tjdcs/specio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
