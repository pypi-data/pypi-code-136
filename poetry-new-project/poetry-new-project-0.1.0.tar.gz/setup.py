# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_new_project']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['poetry-new-project = poetry_new_project.app:cli']}

setup_kwargs = {
    'name': 'poetry-new-project',
    'version': '0.1.0',
    'description': '',
    'long_description': "\n\n\n# todo:\n\n- test cases:\n    - [] - test to make sure that installation goes through if python version is not installed and that python version is installed\n    - [] - test to make sure that pyenv is installed correctly\n    - [] -  test to ensure that if not forced and an environment exists, that nothing happens and an error message indicating that it may be useful to use that flag appears\n    - [] - test to make sure that if forced, a new environment is created\n    - [] - test to ensure that the rc init file operation is idempotent and we don't end up with a bunch of spam/repeats inside the rc files\n\n\n- starting case: base python image, no pyenv etc\n    - test case 1: create virtual environment\n        - poetry-new-project test1 --version 3.9.5\n    - test case 2: create same virtual environment and expect failure because it is not forced\n        - poetry-new-project test1 --version 3.9.5\n        - assert fail\n    - test case 3: create same virtual environment with force flag and ensure that environment is re-created\n        - poetry-new-project test1 --version 3.9.5 --force\n    \n\ndocker build -t poetry-new-project-test:latest -f test/Dockerfile .\ndocker run -it --rm -v $(pwd):/code -w /code poetry-new-project-test:latest bash\n\ndocker run -it --rm -v $(pwd):/app -w /app python:3.9.5-slim-buster bash",
    'author': 'Zach Bellay',
    'author_email': 'zachbellay@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
