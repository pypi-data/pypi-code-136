# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylsoFoam']

package_data = \
{'': ['*']}

install_requires = \
['PyFoam>=2022.9,<2023.0',
 'argh>=0.26.2,<0.27.0',
 'byteparsing>=0.1.2,<0.2.0',
 'numpy>=1.23.4,<2.0.0']

setup_kwargs = {
    'name': 'pylso-foam',
    'version': '0.1.0',
    'description': 'Python Large Scale Orchestrator for OpenFOAM computations.',
    'long_description': "---\ntitle: pylso-foam\nsubtitle: Python module for Large Scale Orchestration of OpenFoam computations.\nauthor: Johan Hidding, Pablo Rodríguez Sanchez\n---\n[![Entangled badge](https://img.shields.io/badge/entangled-Use%20the%20source!-%2300aeff)](https://entangled.github.io/)\n[![Python package](https://github.com/parallelwindfarms/pylso-foam/actions/workflows/python-package.yml/badge.svg)](https://github.com/parallelwindfarms/pylso-foam/actions/workflows/python-package.yml)\n\nThis module lets you interact with OpenFOAM through Python. You may use it in cases where you need to run a lot of separate computations in OpenFOAM, possibly in parallel. In our view, this fixes a few gaps in the PyFoam module. Here's what `pylso-foam` can and `PyFoam` can't do:\n\n- Run jobs in parallel: PyFoam has a lot of hidden state. In `pylso-foam` every job runs in its own case directory.\n- Work with binary OpenFOAM files: by using the [`byteparsing`](https://parallelwindfarms.github.io/byteparsing) package, we can interact with binary data. We don't involve any geometry here, we can just read the raw data and do some arithmetic on it.\n\n# Admin\nYou may `pip install` this module. If you're developing however, we use `poetry` to manage dependencies.\n\n# License\nApache 2\n\n",
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
