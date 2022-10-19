# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['extra_ds_tools',
 'extra_ds_tools.decorators',
 'extra_ds_tools.plots',
 'extra_ds_tools.transformers']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib==3.6.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'scipy>=1.9.2,<2.0.0',
 'seaborn>=0.12.0,<0.13.0',
 'tabulate>=0.8.10,<0.9.0']

setup_kwargs = {
    'name': 'extra-datascience-tools',
    'version': '0.2.0',
    'description': 'Python package which offers additional tools for data scientists.',
    'long_description': "[![Version](https://img.shields.io/pypi/v/extra-datascience-tools)](https://pypi.org/project/extra-datascience-tools/)\n[![Downloads](https://pepy.tech/badge/extra-datascience-tools)](https://pepy.tech/project/extra-datascience-tools)\n![](https://img.shields.io/github/license/sTomerG/extra-datascience-tools)\n![](https://img.shields.io/pypi/pyversions/extra-datascience-tools)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n# Python package with extra tools to use for data science.\n\nWelcome to `extra-datascience-tools`, a Python package which offers additional tools for data scientists. These tools include or will include e.g.:\n- functions\n- classes\n- decorators\n- plots\n\n..which are useful and often used for most data science projects, so that you don't need to rewrite the same code over again or invent it yourself. Please be aware that this package was launched in oktober 2022 and thus the current amount of features might be limited, but the features that are present can be of great use.\n\n Personally I'm a huge fan of well-documented code, and this package strives for quality and well-documented code over lots of under-documented features. Please visit [ReadTheDocs](https://extra-datascience-tools.readthedocs.io/en/latest/#) for this package's extensive documentation.\n\n**[Github page](https://github.com/sTomerG/extra-datascience-tools)**\n\n## Installation\n\n### Using PyPi\n\n    pip install extra-datascience-tools\n\nWithout using PyPi\n\n    git clone https://github.com/sTomerG/extra-datascience-tools.git\n    cd extra-datascience-tools\n    pip install .\n\nIf problems arise make sure to have the latest version of pip:\n\n    python3 -m pip install --upgrade pip\n\n## Usage\n    >>> import extra_ds_tools\n\n\n",
    'author': 'Tomer Gabay',
    'author_email': 'tomergabay001@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
