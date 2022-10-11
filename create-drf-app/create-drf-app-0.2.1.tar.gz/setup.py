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
    'version': '0.2.1',
    'description': 'Starting a DRF project made easy',
    'long_description': '# create-drf-app tool\n\n\ncreate-drf-app helps you create Django + DRF project. choosing the type of template you want from basic to advance. \n\n\n\n## Installations\nAssuming you have Python installed..\nInstall create-drf-app tool.\n```shell script\n$ pip install create-drf-app\n```\n\n## Create proejct\nCreate a new Django + DRF project.\n```shell script\n$ create-drf-app start <template_type>\n```\n\n## Template types\nfor now we only have a basic template\n- basic\n- intermediate\n- advance\n\n## Road map\n- Intermediate DRF template\n- Advance DRF template\n- React/DRF template\n- Vue/DRF template\n- SolidJs/DRF template\n\n\n## License\n\nEverything inside this repository is [MIT licensed](https://github.com/MohammedBajuaifer/create-drf-app/blob/master/README.md).\n\n',
    'author': 'Mohammed Bajuaifer',
    'author_email': 'm.bajuaifer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MohammedBajuaifer/create-drf-app',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
