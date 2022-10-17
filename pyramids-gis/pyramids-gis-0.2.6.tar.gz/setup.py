# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyramids']

package_data = \
{'': ['*']}

install_requires = \
['Fiona==1.8.21',
 'GDAL==3.4.3',
 'Rtree>=1.0.0,<2.0.0',
 'Shapely>=1.8.4,<2.0.0',
 'affine>=2.3.1,<3.0.0',
 'geopandas>=0.11.1,<0.12.0',
 'geopy>=2.2.0,<3.0.0',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.5.3,<4.0.0',
 'netCDF4>=1.6.1,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pyproj>=3.4.0,<4.0.0',
 'rasterio>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'pyramids-gis',
    'version': '0.2.6',
    'description': 'GIS utility package',
    'long_description': '[![Python Versions](https://img.shields.io/pypi/pyversions/pyramids-gis.png)](https://img.shields.io/pypi/pyversions/pyramids-gis)\n[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MAfarrag/Hapi.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MAfarrag/Hapi/context:python)\n[![Documentation Status](https://readthedocs.org/projects/pyramids-gis/badge/?version=latest)](https://pyramids-gis.readthedocs.io/en/latest/?badge=latest)\n\n\n![GitHub last commit](https://img.shields.io/github/last-commit/MAfarrag/pyramids)\n![GitHub forks](https://img.shields.io/github/forks/MAfarrag/pyramids?style=social)\n![GitHub Repo stars](https://img.shields.io/github/stars/MAfarrag/pyramids?style=social)\n[![Coverage Status](https://coveralls.io/repos/github/MAfarrag/pyramids/badge.svg?branch=main)](https://coveralls.io/github/MAfarrag/pyramids?branch=main)\n\n\n![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/mafarrag/pyramids/0.2.1?include_prereleases&style=plastic)\n![GitHub last commit](https://img.shields.io/github/last-commit/mafarrag/pyramids)\n\nCurrent release info\n====================\n\n| Name                                                                                                                 | Downloads                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Version                                                                                                                                                                                                                                                                                                                                                 | Platforms |\n|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --- |\n| [![Conda Recipe](https://img.shields.io/badge/recipe-pyramids-green.svg)](https://anaconda.org/conda-forge/pyramids) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pyramids.svg)](https://anaconda.org/conda-forge/pyramids) [![Downloads](https://pepy.tech/badge/pyramids-gis)](https://pepy.tech/project/pyramids-gis) [![Downloads](https://pepy.tech/badge/pyramids-gis/month)](https://pepy.tech/project/pyramids-gis)  [![Downloads](https://pepy.tech/badge/pyramids-gis/week)](https://pepy.tech/project/pyramids-gis)  ![PyPI - Downloads](https://img.shields.io/pypi/dd/pyramids-gis?color=blue&style=flat-square) ![GitHub all releases](https://img.shields.io/github/downloads/MAfarrag/pyramids/total) ![GitHub release (latest by date)](https://img.shields.io/github/downloads/MAfarrag/pyramids/0.2.1/total) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/pyramids.svg)](https://anaconda.org/conda-forge/pyramids) [![PyPI version](https://badge.fury.io/py/pyramids-gis.svg)](https://badge.fury.io/py/pyramids-gis)  | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/pyramids.svg)](https://anaconda.org/conda-forge/pyramids) [![Join the chat at https://gitter.im/Hapi-Nile/Hapi](https://badges.gitter.im/Hapi-Nile/Hapi.svg)](https://gitter.im/Hapi-Nile/Hapi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) |\n\npyramids - GIS utility package\n=====================================================================\n**pyramids** is a GIS utility package using gdal, rasterio, ....\n\npyramids\n\nMain Features\n-------------\n  - GIS modules to enable the modeler to fully prepare the meteorological inputs and do all the preprocessing\n    needed to build the model (align rasters with the DEM), in addition to various methods to manipulate and\n    convert different forms of distributed data (rasters, NetCDF, shapefiles)\n\n\nFuture work\n-------------\n  - Developing a DEM processing module for generating the river network at different DEM spatial resolutions.\n\n\n\nInstalling pyramids\n===============\n\nInstalling `pyramids` from the `conda-forge` channel can be achieved by:\n\n```\nconda install -c conda-forge pyramids=0.2.3\n```\n\nIt is possible to list all of the versions of `pyramids` available on your platform with:\n\n```\nconda search pyramids --channel conda-forge\n```\n\n## Install from Github\nto install the last development to time you can install the library from github\n```\npip install git+https://github.com/MAfarrag/pyramids\n```\n\n## pip\nto install the last release you can easly use pip\n```\npip install pyramids-gis==0.2.3\n```\n\nQuick start\n===========\n\n```\n  >>> import pyramids\n```\n\n[other code samples](https://pyramids-gis.readthedocs.io/en/latest/?badge=latest)\n',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MAfarrag/pyramids',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
