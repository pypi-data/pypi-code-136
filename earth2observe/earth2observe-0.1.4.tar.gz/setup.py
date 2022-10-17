# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['earth2observe', 'earth2observe.gee']

package_data = \
{'': ['*']}

install_requires = \
['Fiona==1.8.21',
 'earthengine-api>=0.1.324,<0.2.0',
 'ecmwf-api-client>=1.6.3,<2.0.0',
 'gdal==3.4.3',
 'joblib>=1.2.0,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'netCDF4>=1.6.1,<2.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pyramids-gis>=0.2.6,<0.3.0']

setup_kwargs = {
    'name': 'earth2observe',
    'version': '0.1.4',
    'description': 'remote sensing package',
    'long_description': '[![Python Versions](https://img.shields.io/pypi/pyversions/earthobserve.png)](https://img.shields.io/pypi/pyversions/earthobserve)\n[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MAfarrag/Hapi.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MAfarrag/Hapi/context:python)\n\n\n\n![GitHub last commit](https://img.shields.io/github/last-commit/MAfarrag/earthobserve)\n![GitHub forks](https://img.shields.io/github/forks/MAfarrag/earthobserve?style=social)\n![GitHub Repo stars](https://img.shields.io/github/stars/MAfarrag/earthobserve?style=social)\n\n\nCurrent release info\n====================\n\n| Name | Downloads                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Version | Platforms |\n| --- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --- | --- |\n| [![Conda Recipe](https://img.shields.io/badge/recipe-earth2observe-green.svg)](https://anaconda.org/conda-forge/earth2observe) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/earth2observe.svg)](https://anaconda.org/conda-forge/earth2observe) [![Downloads](https://pepy.tech/badge/earth2observe)](https://pepy.tech/project/earth2observe) [![Downloads](https://pepy.tech/badge/earth2observe/month)](https://pepy.tech/project/earth2observe)  [![Downloads](https://pepy.tech/badge/earth2observe/week)](https://pepy.tech/project/earth2observe)  ![PyPI - Downloads](https://img.shields.io/pypi/dd/earth2observe?color=blue&style=flat-square) ![GitHub all releases](https://img.shields.io/github/downloads/MAfarrag/earth2observe/total) ![GitHub release (latest by date)](https://img.shields.io/github/downloads/MAfarrag/earth2observe/0.1.0/total) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/earth2observe.svg)](https://anaconda.org/conda-forge/earth2observe) [![PyPI version](https://badge.fury.io/py/earth2observe.svg)](https://badge.fury.io/py/earth2observe) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/earth2observe/badges/version.svg)](https://anaconda.org/conda-forge/earth2observe) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/earth2observe.svg)](https://anaconda.org/conda-forge/earth2observe) [![Join the chat at https://gitter.im/Hapi-Nile/Hapi](https://badges.gitter.im/Hapi-Nile/Hapi.svg)](https://gitter.im/Hapi-Nile/Hapi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) |\n\nearthobserve - Remote Sensing package\n=====================================================================\n**earthobserve** is a Remote Sensing package\n\nearthobserve\n\nMain Features\n-------------\n  -\n\n\nFuture work\n-------------\n  -\n\n\n\nInstalling earthobserve\n===============\n\nInstalling `earthobserve` from the `conda-forge` channel can be achieved by:\n\n```\nconda install -c conda-forge earthobserve\n```\n\nIt is possible to list all of the versions of `earthobserve` available on your platform with:\n\n```\nconda search earthobserve --channel conda-forge\n```\n\n## Install from Github\nto install the last development to time you can install the library from github\n```\npip install git+https://github.com/MAfarrag/earthobserve\n```\n\n## pip\nto install the last release you can easly use pip\n```\npip install earthobserve==0.1.3\n```\n\nQuick start\n===========\n\n```\n  >>> import earthobserve\n```\n\n[other code samples](https://earthobserve.readthedocs.io/en/latest/?badge=latest)\n',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MAfarrag/earth2observe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
