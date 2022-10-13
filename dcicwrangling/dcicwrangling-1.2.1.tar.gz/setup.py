# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['scripts']

package_data = \
{'': ['*']}

install_requires = \
['Biopython==1.76',
 'GEOparse>=2.0.1,<3.0.0',
 'dcicutils>=4.1.0,<5.0.0',
 'jupyterlab==3.2.8',
 'openpyxl>=3.0.9,<4.0.0']

entry_points = \
{'console_scripts': ['fetch-items = scripts.item_fetcher:main']}

setup_kwargs = {
    'name': 'dcicwrangling',
    'version': '1.2.1',
    'description': 'Scripts and Jupyter notebooks for 4DN wrangling',
    'long_description': "# DCIC-wrangling\n\nThis is a collection of scripts and Jupyter notebooks that can be helpful when performing many data wrangling tasks.  Most of the tools are specific to 4DN Nucleome wrangling needs, however may be modified to be more generally useful for certain tasks.\n\n## Install\n\nPackaged with `poetry` can be installed using `make`, `poetry` or `pip`.\n\nFrom the dcicwrangling directory - `make build`\n\nIf you already have poetry installed - `poetry install`\n\nOr to pip install from PyPi - `pip install dcicwrangling`\n\nAll dependencies are installed by default - if for some reason you don't want to install `pytest` packages or `invoke` (used to launch notebooks) you can do `poetry install --no-dev` - not recommended.\n\n## Usage\n\n### Jupyter notebooks\nThere are a collection of commonly used jupyter notebooks in the `notebooks/useful_notebooks` directory.  You can start a jupyter notebook server locally using `invoke notebook` from the top level directory.  This should launch the server and open a browser page where the notebooks can be accessed.\n\n**IMPORTANT!** - You should create your own folder in the `notebooks` directory named `Yourname_scripts`.  This folder is where you should create, access and run your notebooks.  If you want to start with one of the notebooks in the useful_notebooks directory please create a copy and move it to your own folder.  This keeps the repository clean and organized.  Please **DO NOT** run notebooks in the useful_notebooks directory and commit the results to the repository.\n\n### Scripts\n\nThe scripts directory contains some useful command line scripts.  They can be run from the top level directory using `python scripts/script_name --options`.  Using `--help` shows available options.  In general, modified versions and bespoke scripts should not be committed to the repository - or alternatively committed to a separate non-master branch.\n\nAs scripts are developed and refined `tool.poetry.scripts` directives can be added to facilitate script usage - see `pyproject.toml` file example.\n",
    'author': '4DN-DCIC Team',
    'author_email': 'support@4dnucleome.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/4dn-dcic/dcicwrangling',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.9',
}


setup(**setup_kwargs)
