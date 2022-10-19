# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yao']

package_data = \
{'': ['*'], 'yao': ['etc/*']}

install_requires = \
['click>=8.1.2,<9.0.0', 'sdss-archon>=0.6.0', 'sdsstools>=0.4.0']

entry_points = \
{'console_scripts': ['yao = yao.__main__:yao']}

setup_kwargs = {
    'name': 'sdss-yao',
    'version': '1.0.0',
    'description': 'BOSS spectrograph actor that uses an STA Archon controller',
    'long_description': '# yao\n\n![Versions](https://img.shields.io/badge/python->3.9-blue)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Documentation Status](https://readthedocs.org/projects/lvmieb/badge/?version=latest)](https://sdss-yao.readthedocs.io/en/latest/?badge=latest)\n\nBOSS spectrograph actor that uses an STA Archon controller.\n',
    'author': 'José Sánchez-Gallego',
    'author_email': 'gallegoj@uw.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sdss/yao',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
