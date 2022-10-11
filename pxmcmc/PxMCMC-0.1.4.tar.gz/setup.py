# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pxmcmc']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=5.0.4,<6.0.0',
 'greatcirclepaths>=1.1.0,<2.0.0',
 'h5py>=3.3.0,<4.0.0',
 'matplotlib>=3.4.2,<4.0.0',
 'numpy>=1.21.1,<2.0.0',
 'pys2let>=2.2.3,<3.0.0',
 'pyssht>=1.4.0,<2.0.0',
 'scipy>=1.9.2,<2.0.0']

extras_require = \
{'cartopy': ['Cartopy>=0.19.0,<0.20.0'],
 'docs': ['sphinx>=4,<5', 'sphinx-rtd-theme>=1.0.0,<2.0.0']}

setup_kwargs = {
    'name': 'pxmcmc',
    'version': '0.1.4',
    'description': 'Proximal Markov Chain Monte Carlo',
    'long_description': "[![Documentation Status](https://readthedocs.org/projects/pxmcmc/badge/?version=latest)](https://pxmcmc.readthedocs.io/en/latest/?badge=latest)\n\n# Python ProxMCMC\n\n## Installation\n\nAvailable on [pypi](https://pypi.org/project/pxmcmc/)\n\n```bash\npip install pxmcmc\n```\n\nIf installing from source it recommended to use [poetry](https://python-poetry.org/)\n\n```bash\ngit clone https://github.com/auggiemarignier/pxmcmc\ncd pxmcmc\npoetry install\nsource <ENVIRONMENT_LOCATION>/bin/activate\npytest\n```\n\n## Documentation\n\nFull documentation available on [readthedocs](https://pxmcmc.readthedocs.io/en/latest/?badge=latest).\n\n## Examples\n\nExamples of how to use this code are found in the `experiments` directory.  Note that we don't provide any example input data files for the various experiments here, though can be made available upon request.\n\n```bash\ncd experiments/phasevelocity\npython main.py --help\n```\n",
    'author': 'Auggie Marignier',
    'author_email': 'augustin.marignier.14@ucl.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/auggiemarignier/pxmcmc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
