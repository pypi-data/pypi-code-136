# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagster_ext',
 'dagster_meltano',
 'files_dagster_ext',
 'files_dagster_ext.dagster.{{ cookiecutter.project_name }}',
 'meltano',
 'meltano.edk']

package_data = \
{'': ['*'], 'files_dagster_ext': ['dagster/*', 'github/*']}

install_requires = \
['PyYAML>=6.0.0,<7.0.0',
 'click>=8.1.3,<9.0.0',
 'cookiecutter>=2.1.1,<3.0.0',
 'dagit>=1.0,<1.1',
 'dagster-dbt>=0.16,<0.17',
 'dagster>=1.0,<1.1',
 'devtools>=0.9.0,<0.10.0',
 'pydantic>=1.9.0,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'structlog>=21.2.0,<22.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['dagit_invoker = '
                     'dagster_ext.pass_through:pass_through_cli_dagit',
                     'dagster_extension = dagster_ext.main:app',
                     'dagster_invoker = '
                     'dagster_ext.pass_through:pass_through_cli_dagster']}

setup_kwargs = {
    'name': 'dagster-ext',
    'version': '0.0.1a6',
    'description': '`dagster-ext` is a Meltano utility extension.',
    'long_description': 'None',
    'author': 'Jules Huisman',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
