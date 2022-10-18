# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['parareal']

package_data = \
{'': ['*']}

install_requires = \
['argh>=0.26.2,<0.27.0',
 'dask-mpi>=2022.4.0,<2023.0.0',
 'dask[complete]>=2022.10.0,<2023.0.0',
 'h5py>=3.7.0,<4.0.0',
 'mpi4py>=3.1.3,<4.0.0',
 'numpy>=1.23.4,<2.0.0']

setup_kwargs = {
    'name': 'parareal',
    'version': '0.1.0',
    'description': 'Parallel-in-time framework for Python',
    'long_description': '---\ntitle: Parareal\nsubtitle: a library for parallel-in-time computations in Python\n---\n[![Entangled badge](https://img.shields.io/badge/entangled-Use%20the%20source!-%2300aeff)](https://entangled.github.io/)\n\nThis package runs the parareal algorithm on a black-box simulator. Parallelisation is managed through Dask.\n\n# License\nApache 2, see `LICENSE`.\n\n',
    'author': 'Johan Hidding',
    'author_email': 'j.hidding@esciencecenter.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
