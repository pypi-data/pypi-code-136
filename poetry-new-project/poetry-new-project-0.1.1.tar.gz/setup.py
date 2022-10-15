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
    'version': '0.1.1',
    'description': '',
    'long_description': '\n\npoetry-new-project\n==================\n\nThis is a small CLI utility meant to make it easier to set up a new Python project using Poetry and Pyenv.\n\n\n\n## Quickstart 🚀\n\n0. Prerequisite: Pyenv is already installed and configured on your system. If not, see [pyenv installer](https://github.com/pyenv/pyenv-installer).\n\n1. Install the package: `pip install poetry-new-project`\n\n2. Create a new project directory and cd into it: `mkdir my-new-project && cd my-new-project`\n\n2. Create a new pyenv environment + poetry project : `poetry-new-project my-new-project-venv --version=3.10.6`\n\n3. Wait for any python downloads to complete and finish the interactive poetry setup process.\n\n4. Code! 🎉\n\n## Inspiration (and why) 🤔\n\n[Blog Post: Pyenv & Poetry New Project Start](https://zachbellay.com/posts/pyenv-poetry-new-project-start/)\n\nOver the past year or so I have found myself referencing this blog post many times to start a new python project. \n\nThis project is meant to supplant running (most) of these commands manually and to turn it into one CLI utility.\n\n```bash\n# install pyenv on your machine\n\ncurl https://pyenv.run | bash\n\n# install python in pyenv\n\npyenv install 3.9.5\n\n# create virtual environment:\n\npyenv virtualenv 3.9.5 hotdog-not-hotdog\n\n# set hotdog-not-hotdog as the default virtual environment for the current directory\n\npyenv local hotdog-not-hotdog\n\n# install poetry in your virtual environment\n\npip install poetry\n\n# initialize project\n\npoetry init\n\n# install new dependencies\n\npoetry add numpy\n\n# install dependencies (if a pyproject.toml + poetry.lock already exists for a project)\n\npoetry install\n```\n\n## Build 🛠\n\n```bash\n\n    poetry build\n\n```\n\n## Publish 📖\n\n_Note:_ Remember to update the version in `pyproject.toml` when publishing a new version.\n\n```bash\n\n    poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD\n\n```\n\n## Formatting ✨\n\n```bash\n\n    black poetry_new_project\n\n```\n\n## License 📜\nThis project is licensed under the terms of the MIT license, see MIT - see `License file <LICENSE>`_.\n\n\n\n# TODO\n\n- [] - Write test cases (should run inside of Docker container)\n    - starting case: base python image, no pyenv etc\n        - test case 1: create virtual environment\n            - poetry-new-project test1 --version 3.9.5\n        - test case 2: create same virtual environment and expect failure because it is not forced\n            - poetry-new-project test1 --version 3.9.5\n            - assert fail\n        - test case 3: create same virtual environment with force flag and ensure that environment is re-created\n            - poetry-new-project test1 --version 3.9.5 --force\n        - write tox test to test multiple versions of python, especially earlier versions (i.e. 3.5) since the current setting is only 3.9+\n- [] - write CI/CD pipeline\n    - [] - create github action to push successfully built project to pypi\n    - [] - create github action to run test cases',
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
