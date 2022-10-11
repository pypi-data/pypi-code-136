# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['create_drf_app',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}.users',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name '
 '}}.users.migrations',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}.{{ '
 'cookiecutter.project_name }}',
 'create_drf_app.templates.basic.{{ cookiecutter.project_name }}.{{ '
 'cookiecutter.project_name }}.settings']

package_data = \
{'': ['*'], 'create_drf_app': ['templates/basic/*']}

install_requires = \
['cookiecutter==2.1.1', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['create-drf-app = create_drf_app.main:app']}

setup_kwargs = {
    'name': 'create-drf-app',
    'version': '0.2.0',
    'description': '',
    'long_description': '',
    'author': 'Mohammed Bajuaifer',
    'author_email': 'mohamadbajuaifer@gmail.com',
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
