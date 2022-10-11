# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amos']

package_data = \
{'': ['*']}

install_requires = \
['miller>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'amos',
    'version': '0.1.8',
    'description': 'Your Python project companion',
    'long_description': '[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Documentation Status](https://readthedocs.org/projects/amos/badge/?version=latest)](http://amos.readthedocs.io/?badge=latest)\n\n"I AM that guy." - Amos Burton\n\nLike the Roci\'s most interesting character, this package is designed to handle the dirtiest jobs in a python project.\n\n\n\n\namos\'s framework supports a wide range of coding styles. You can create complex multiple inheritance structures with mixins galore or simpler, compositional objects. Even though the data structures are necessarily object-oriented, all of the tools to modify them are also available as functions, for those who prefer a more funcitonal approaching to programming. \n\nThe project is also highly internally documented so that users and developers can easily make amos work with their projects. It is designed for Python coders at all levels. Beginners should be able to follow the readable code and internal documentation to understand how it works. More advanced users should find complex and tricky problems addressed through efficient code.',
    'author': 'corey rayburn yung',
    'author_email': 'coreyrayburnyung@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/WithPrecedent/amos',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
