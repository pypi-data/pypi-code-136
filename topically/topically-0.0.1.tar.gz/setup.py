# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['topically', 'topically.prompts']

package_data = \
{'': ['*']}

install_requires = \
['altair>=4.2,<5.0',
 'bertopic[bertopic]',
 'cohere>=2.1,<3.0',
 'matplotlib>=3.5,<4.0',
 'pandas>=1.4,<2.0',
 'streamlit>=1.12,<2.0',
 'umap-learn>=0.5,<0.6']

setup_kwargs = {
    'name': 'topically',
    'version': '0.0.1',
    'description': '',
    'long_description': 'None',
    'author': 'Jay Alammar',
    'author_email': 'jay@cohere.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
