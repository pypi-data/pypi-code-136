# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlflow_med_cli']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['mlflow-med-cli = mlflow_med_cli.main:app']}

setup_kwargs = {
    'name': 'mlflow-med-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': '# MLFlow-med-cli\nCLI tool for MLFlow-med experiment management.\n',
    'author': 'hossay',
    'author_email': 'youhs4554@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
