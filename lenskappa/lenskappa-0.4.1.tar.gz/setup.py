# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lenskappa',
 'lenskappa.analysis',
 'lenskappa.catalog',
 'lenskappa.counting',
 'lenskappa.datasets',
 'lenskappa.datasets.simulations',
 'lenskappa.datasets.surveys',
 'lenskappa.datasets.surveys.ms',
 'lenskappa.output',
 'lenskappa.plugin',
 'lenskappa.utils',
 'lenskappa.weighting']

package_data = \
{'': ['*'], 'lenskappa': ['config/*'], 'lenskappa.weighting': ['config/*']}

install_requires = \
['Shapely>=1.8.1,<2.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'astropy>=5.0.3,<6.0.0',
 'heinlein>=0.3.6,<0.4.0',
 'multiprocess>=0.70.13,<0.71.0',
 'numpy>=1.22.3,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'regions>=0.6,<0.7',
 'scipy>=1.8.0,<2.0.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'lenskappa',
    'version': '0.4.1',
    'description': '',
    'long_description': None,
    'author': 'Patrick Wells',
    'author_email': 'pwells@ucdavis.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11git',
}


setup(**setup_kwargs)
