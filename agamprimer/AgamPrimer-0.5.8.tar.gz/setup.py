# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['AgamPrimer']

package_data = \
{'': ['*'], 'AgamPrimer': ['agamPrimer.egg-info/*']}

install_requires = \
['gget',
 'kaleido==0.2.1',
 'malariagen_data',
 'openpyxl',
 'primer3-py',
 'seaborn']

setup_kwargs = {
    'name': 'agamprimer',
    'version': '0.5.8',
    'description': 'A package to design primers in Anopheles gambiae whilst considering genetic variation with malariagen_data',
    'long_description': None,
    'author': 'Sanjay Nagi',
    'author_email': 'sanjay.nagi@lstmed.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
