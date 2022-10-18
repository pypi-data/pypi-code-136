# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['signialib']

package_data = \
{'': ['*'],
 'signialib': ['calibrations/001/Ferraris/2022-07-24_16-00/*',
               'calibrations/002/Ferraris/2022-07-24_16-00/*']}

install_requires = \
['joblib>=1.0.0,<2.0.0',
 'nilspodlib>=3.2.2,<4.0.0',
 'numpy>=1',
 'pandas>=1,<2',
 'scipy>=1.6.1,<2.0.0',
 'typing_extensions>=4.1.1']

extras_require = \
{':python_version < "3.9"': ['numba>=0,<1'],
 ':python_version >= "3.10" and python_version < "4.0"': ['numba>=0.55,<0.56'],
 ':python_version >= "3.9" and python_version < "3.10"': ['numba>=0.53,<0.54'],
 ':sys_platform == "darwin" and platform_machine == "arm64"': ['numba>=0.55.2,<1.0.0']}

setup_kwargs = {
    'name': 'signialib',
    'version': '1.0.1',
    'description': 'Data handling of the IMUs integrated into Signia hearing aids',
    'long_description': None,
    'author': 'Ann-Kristin Seifer',
    'author_email': 'ann-kristin.seifer@fau.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
