# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['modelstar',
 'modelstar.commands',
 'modelstar.connectors',
 'modelstar.connectors.snowflake',
 'modelstar.connectors.snowflake.modelstar',
 'modelstar.executors',
 'modelstar.executors.py_parser',
 'modelstar.templates',
 'modelstar.templates.snowflake_project.functions',
 'modelstar.utils']

package_data = \
{'': ['*'],
 'modelstar.templates': ['snowflake_project/.gitignore',
                         'snowflake_project/.modelstar/*',
                         'snowflake_project/data/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'joblib>=1.2.0,<2.0.0',
 'snowflake-connector-python>=2.7.12,<3.0.0',
 'tabulate>=0.8.10,<0.9.0',
 'tomlkit>=0.11.4,<0.12.0']

entry_points = \
{'console_scripts': ['modelstar = modelstar.cli:main']}

setup_kwargs = {
    'name': 'modelstar',
    'version': '0.1.0',
    'description': 'DevOps for User Defined Functions and Stored Procedures in Data Warehouses',
    'long_description': "# Command line interface to work with modelstar\n\n## Project initialization\n\n```shell\nmodelstar init <project_name>/<.>\n``` \n\nCreates a folder named as `<project_name>`. With a project template of the required files and folders. \n\n## Add snowflake credentials\n\nInside the project folder change the values in `modelstar_project.toml` to the ones of your snowflake account information. \n\n## Test connection with the credentails you've given\n\n```shell\nmodelstar use <config_name>\n``` \n\n## Register a python function to your database and schema\n\n```shell\nmodelstar register addition.py addition\n```",
    'author': 'Adithya Krishnan',
    'author_email': 'krishsandeep@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://modelstar.io',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
