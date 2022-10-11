# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bimato']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'scikit-image>=0.19.3,<0.20.0',
 'scipy>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'bimato',
    'version': '2022.1',
    'description': 'Bio Matrix Topology (BiMaTo) is a library containing all the biopolymer matrix topology analyses published by the Biological Physics Group, (BIP), Peter Debye Institute, University Leipzig, Germany.',
    'long_description': 'None',
    'author': 'Tony Fischer (tku137)',
    'author_email': 'tonyfischer@mailbox.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
