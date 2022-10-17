# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bru_analysis',
 'bru_analysis.common',
 'bru_analysis.ft_test',
 'bru_analysis.unit_test']

package_data = \
{'': ['*'], 'bru_analysis.common': ['stopwords/*']}

install_requires = \
['bertopic>=0.12.0,<0.13.0',
 'pandas>=1.4.4,<2.0.0',
 'sentence-transformers>=2.2.2,<3.0.0',
 'tensorflow>=2.10.0,<3.0.0',
 'torch>=1.12.1,<2.0.0',
 'transformers>=4.21.3,<5.0.0']

setup_kwargs = {
    'name': 'bru-analysis',
    'version': '0.3.0',
    'description': 'This library - Bru-analytics W&J. Private library',
    'long_description': 'None',
    'author': 'Oscar Riojas',
    'author_email': 'oscar@whaleandjaguar.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
