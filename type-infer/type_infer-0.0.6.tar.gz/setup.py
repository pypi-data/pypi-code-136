# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['type_infer']

package_data = \
{'': ['*']}

install_requires = \
['colorlog>=6.5.0,<7.0.0',
 'dataclasses-json>=0.5.4,<0.6.0',
 'langid>=1.1.6,<2.0.0',
 'nltk>=3,<4',
 'numpy>=1.15,<2.0',
 'pandas>=1,<2',
 'python-dateutil>=2.1,<3.0',
 'scipy>=1,<2',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'type-infer',
    'version': '0.0.6',
    'description': 'Automated type inference for Machine Learning pipelines.',
    'long_description': '# type_infer\nAutomated type inference for Machine Learning pipelines.\n',
    'author': 'MindsDB Inc.',
    'author_email': 'hello@mindsdb.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
