# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['digitalearth']

package_data = \
{'': ['*']}

install_requires = \
['cleopatra>=0.2.3,<0.3.0',
 'loguru>=0.6.0,<0.7.0',
 'numpy>=1.23.3,<2.0.0',
 'pyramids-gis>=0.2.6,<0.3.0']

setup_kwargs = {
    'name': 'digitalearth',
    'version': '0.1.6',
    'description': 'Geo-spatial Visualization package',
    'long_description': '[![Python Versions](https://img.shields.io/pypi/pyversions/digitalearth.png)](https://img.shields.io/pypi/pyversions/digitalearth)\n[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MAfarrag/digitalearth.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MAfarrag/digitalearth/context:python)\n[![Documentation Status](https://readthedocs.org/projects/digitalearth/badge/?version=latest)](https://cleopatra.readthedocs.io/en/latest/?badge=latest)\n\n\n![GitHub last commit](https://img.shields.io/github/last-commit/MAfarrag/digitalearth)\n![GitHub forks](https://img.shields.io/github/forks/MAfarrag/digitalearth?style=social)\n![GitHub Repo stars](https://img.shields.io/github/stars/MAfarrag/digitalearth?style=social)\n\n\nCurrent release info\n====================\n\n| Name | Downloads                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Version | Platforms |\n| --- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --- | --- |\n| [![Conda Recipe](https://img.shields.io/badge/recipe-digitalearth-green.svg)](https://anaconda.org/conda-forge/digitalearth) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/digitalearth.svg)](https://anaconda.org/conda-forge/digitalearth) [![Downloads](https://pepy.tech/badge/digitalearth)](https://pepy.tech/project/digitalearth) [![Downloads](https://pepy.tech/badge/digitalearth/month)](https://pepy.tech/project/digitalearth)  [![Downloads](https://pepy.tech/badge/digitalearth/week)](https://pepy.tech/project/digitalearth)  ![PyPI - Downloads](https://img.shields.io/pypi/dd/digitalearth?color=blue&style=flat-square) ![GitHub all releases](https://img.shields.io/github/downloads/MAfarrag/digitalearth/total) ![GitHub release (latest by date)](https://img.shields.io/github/downloads/MAfarrag/digitalearth/0.1.0/total) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/digitalearth.svg)](https://anaconda.org/conda-forge/digitalearth) [![PyPI version](https://badge.fury.io/py/digitalearth.svg)](https://badge.fury.io/py/digitalearth) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/digitalearth/badges/version.svg)](https://anaconda.org/conda-forge/digitalearth) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/digitalearth.svg)](https://anaconda.org/conda-forge/digitalearth) [![Join the chat at https://gitter.im/Hapi-Nile/Hapi](https://badges.gitter.im/Hapi-Nile/Hapi.svg)](https://gitter.im/Hapi-Nile/Hapi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) |\n\ndigitalearth - Remote Sensing package\n=====================================================================\n**digitalearth** is a Remote Sensing package\n\ndigitalearth\n\nMain Features\n-------------\n  -\n\n\nFuture work\n-------------\n  -\n\n\n\nInstalling digitalearth\n===============\n\nInstalling `digitalearth` from the `conda-forge` channel can be achieved by:\n\n```\nconda install -c conda-forge digitalearth\n```\n\nIt is possible to list all of the versions of `digitalearth` available on your platform with:\n\n```\nconda search digitalearth --channel conda-forge\n```\n\n## Install from Github\nto install the last development to time you can install the library from github\n```\npip install git+https://github.com/MAfarrag/digitalearth\n```\n\n## pip\nto install the last release you can easly use pip\n```\npip install digitalearth==0.1.6\n```\n\nQuick start\n===========\n\n```\n  >>> import digitalearth\n```\n\n[other code samples](https://digitalearth.readthedocs.io/en/latest/?badge=latest)\n',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MAfarrag/Digital-Earth',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
