# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gfatpy',
 'gfatpy.aeronet',
 'gfatpy.atmo',
 'gfatpy.cli',
 'gfatpy.cli.lidar',
 'gfatpy.cli.lidar.plot',
 'gfatpy.cloudnet',
 'gfatpy.lidar',
 'gfatpy.lidar.depolarization',
 'gfatpy.lidar.depolarization.GHK',
 'gfatpy.lidar.depolarization.GHK.system_settings',
 'gfatpy.lidar.plot',
 'gfatpy.lidar.preprocessing',
 'gfatpy.lidar.quality_assurance',
 'gfatpy.lidar.raw2l1',
 'gfatpy.lidar.raw2l1.raw2l1_gfat.raw2l1',
 'gfatpy.lidar.raw2l1.raw2l1_gfat.raw2l1.doc.source',
 'gfatpy.lidar.raw2l1.raw2l1_gfat.raw2l1.reader',
 'gfatpy.lidar.raw2l1.raw2l1_gfat.raw2l1.reader.lib',
 'gfatpy.lidar.raw2l1.raw2l1_gfat.raw2l1.test',
 'gfatpy.lidar.raw2l1.raw2l1_gfat.raw2l1.tools',
 'gfatpy.lidar.retrieval',
 'gfatpy.utils']

package_data = \
{'': ['*'],
 'gfatpy': ['assets/*'],
 'gfatpy.lidar.depolarization.GHK': ['tests/datos/MULHACEN/QA/GHK/2022/10/04/*'],
 'gfatpy.lidar.raw2l1': ['config/*', 'raw2l1_gfat/*'],
 'gfatpy.lidar.raw2l1.raw2l1_gfat.raw2l1': ['conf/*', 'doc/*'],
 'gfatpy.lidar.raw2l1.raw2l1_gfat.raw2l1.doc.source': ['_templates/*',
                                                       'images/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'cloudnetpy>=1.36.2,<2.0.0',
 'dask>=2022.7.1,<2023.0.0',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.5.2,<4.0.0',
 'netCDF4>=1.5.7,<1.6.0',
 'numba>=0.56.2,<0.57.0',
 'numpy>=1.23.1,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'scikit-learn>=1.1.1,<2.0.0',
 'scipy>=1.9.0,<2.0.0',
 'seaborn>=0.12.0,<0.13.0',
 'typer[all]>=0.6.1,<0.7.0',
 'typing-extensions>=4.3.0,<5.0.0',
 'xarray[h5netcdf]>=2022.6.0,<2023.0.0']

extras_require = \
{'docs': ['pdoc>=12.0.2,<13.0.0']}

entry_points = \
{'console_scripts': ['gfatpy = gfatpy.cli.main:app']}

setup_kwargs = {
    'name': 'gfatpy',
    'version': '0.0.1',
    'description': 'A python package for GFAT utilities',
    'long_description': 'None',
    'author': 'Juan Diego De la Rosa',
    'author_email': 'jdidelarc@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
