# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cradlebio']

package_data = \
{'': ['*']}

install_requires = \
['Sphinx>=5.1.1,<6.0.0',
 'biopython>=1.70,<2.0',
 'fsspec[gcs]>=2022.7.1,<2023.0.0',
 'google-api-python-client>=2.42.0,<3.0.0',
 'google-auth>=2.6,<3.0',
 'google-cloud-firestore>=2.4.0,<3.0.0',
 'google-cloud-storage>=2.2.1,<3.0.0',
 'importlib_metadata>=4.12.0,<5.0.0',
 'myst-parser>=0.18.0,<0.19.0',
 'packaging>=21.3,<22.0',
 'sphinxcontrib-fulltoc>=1.2.0,<2.0.0',
 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'cradlebio',
    'version': '0.2.0',
    'description': "Client for Cradle's Alphafold-as-a-service",
    'long_description': None,
    'author': 'Cradle Bio',
    'author_email': 'info@cradle.bio',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
