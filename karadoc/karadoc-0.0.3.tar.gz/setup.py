# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['karadoc',
 'karadoc.airflow',
 'karadoc.biqguery',
 'karadoc.cli',
 'karadoc.cli.commands',
 'karadoc.cli.commands.build',
 'karadoc.common',
 'karadoc.common.analyze',
 'karadoc.common.commands',
 'karadoc.common.commands.options',
 'karadoc.common.conf',
 'karadoc.common.exceptions',
 'karadoc.common.graph',
 'karadoc.common.job_core',
 'karadoc.common.model',
 'karadoc.common.observability',
 'karadoc.common.output',
 'karadoc.common.quality',
 'karadoc.common.run',
 'karadoc.common.stream',
 'karadoc.common.utils',
 'karadoc.common.validations',
 'karadoc.connectors',
 'karadoc.spark',
 'karadoc.test_utils']

package_data = \
{'': ['*']}

install_requires = \
['azure-keyvault>=1.1.0,<2.0.0',
 'dynaconf>=2.2.3,<3.0.0',
 'google-cloud-bigquery>=2.31.0,<3.0.0',
 'graphviz>=0.12,<0.13',
 'networkx>=2.2,<3.0',
 'tabulate>=0.8.9,<0.9.0',
 'termcolor>=1.1.0,<2.0.0',
 'xlsxwriter>=3.0.1,<4.0.0']

entry_points = \
{'console_scripts': ['karadoc = karadoc.launcher:main']}

setup_kwargs = {
    'name': 'karadoc',
    'version': '0.0.3',
    'description': 'Karadoc is a data engineering Python framework built on top of PySpark that simplifies ETL/ELT',
    'long_description': '# Karadoc\n',
    'author': 'Furcy Pin',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FurcyPin/karadoc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<3.11',
}


setup(**setup_kwargs)
