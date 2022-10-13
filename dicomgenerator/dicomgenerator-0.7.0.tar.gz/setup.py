# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dicomgenerator', 'dicomgenerator.resources']

package_data = \
{'': ['*'], 'dicomgenerator.resources': ['templates/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'factory-boy>=3.2.1,<4.0.0',
 'numpy>=1.23.4,<2.0.0',
 'pydicom>=2.3.0,<3.0.0',
 'pytest-cov>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'dicomgenerator',
    'version': '0.7.0',
    'description': '',
    'long_description': 'None',
    'author': 'sjoerdk',
    'author_email': 'sjoerd.kerkstra@radboudumc.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
