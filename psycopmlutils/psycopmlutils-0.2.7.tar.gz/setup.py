# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['psycopmlutils',
 'psycopmlutils.loaders.synth.raw',
 'psycopmlutils.sql',
 'psycopmlutils.synth_data_generator']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.40,<1.4.42',
 'catalogue>=2.0.8,<2.1.0',
 'dill>=0.3.5,<0.3.6',
 'numpy>=1.23.3,<1.24.0',
 'pandas>=1.4.4,<1.6.0',
 'psutil>=5.9.1,<6.0.0',
 'pydantic>=1.9.0',
 'pyodbc>=4.0.34,<=4.1.0',
 'scikit-learn>=1.1.2,<1.2.0',
 'scipy>=1.8.1,<1.10.0',
 'srsly>=2.4.4,<2.5.0',
 'transformers>=4.22.0,<=4.23.0',
 'wandb>=0.12.7,<0.13.5',
 'wasabi>=0.9.0,<0.11.0']

setup_kwargs = {
    'name': 'psycopmlutils',
    'version': '0.2.7',
    'description': 'A collection of machine-learning utilities used across the psycop-projects.',
    'long_description': 'None',
    'author': 'Martin Bernstorff',
    'author_email': 'martinbernstorff@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
