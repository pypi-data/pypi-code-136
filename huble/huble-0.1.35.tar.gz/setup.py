# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['huble',
 'huble.sklearn',
 'huble.sklearn.automl',
 'huble.sklearn.deploy',
 'huble.sklearn.process',
 'huble.sklearn.train',
 'huble.util']

package_data = \
{'': ['*'],
 'huble.sklearn': ['process/template/*', 'templates/*', 'train/template/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'auto-sklearn==0.14.7',
 'black>=22.8.0,<23.0.0',
 'pandas>=1.3.5,<2.0.0',
 'scikit-learn==0.24.2']

setup_kwargs = {
    'name': 'huble',
    'version': '0.1.35',
    'description': '',
    'long_description': '',
    'author': 'Rugz007',
    'author_email': 'rugvedsomwanshi007@gmail.com',
    'maintainer': 'Arjit Agarwal',
    'maintainer_email': 'arjitagarwal123@gmail.com',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
