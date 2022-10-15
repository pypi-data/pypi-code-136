# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flaura']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'tomlkit>=0.11.5,<0.12.0']

entry_points = \
{'console_scripts': ['flaura = flaura:flaura']}

setup_kwargs = {
    'name': 'flaura',
    'version': '0.2.1',
    'description': 'Merge upstream with ease!',
    'long_description': "# Flaura\nMerge upstream with ease!\n\nFlaura implements all the merging behaviors of Git, and not only that, it's Git-ndependent, or standalone, which makes merging a non-Git folder, or just a certain folder in a Git repository, instead of the whole repository. \n\nIt allows hardforking to be like a charm!!\n\n## Project Status\nAt the moment, Flaura is still in early development. \n\nNo commands have been implemented except `flaura merge` and `flaura init`. \n\n`flaura merge` should be the basic functionality of Flaura for it to be useful, even though the UX is lacking!! You can see its documentation with `flaura merge --help`",
    'author': 'Fiana Fortressia',
    'author_email': 'fortressnordlys@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/waylovely-project/flaura.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
