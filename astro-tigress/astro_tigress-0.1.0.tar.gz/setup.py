# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['astro_tigress']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=5.1,<6.0',
 'h5py>=3.7.0,<4.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'numpy>=1.20.0,<2.0.0',
 'scipy>=1.8.1,<2.0.0',
 'urllib3>=1.26.9,<2.0.0',
 'yt>=4.0.4,<5.0.0']

setup_kwargs = {
    'name': 'astro-tigress',
    'version': '0.1.0',
    'description': 'TIGRESS data release and associate python scripts',
    'long_description': None,
    'author': 'Chang-Goo Kim',
    'author_email': 'cgkim@astro.princeton.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
