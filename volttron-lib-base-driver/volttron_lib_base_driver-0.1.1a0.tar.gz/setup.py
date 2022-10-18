# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['volttron', 'volttron.driver.base']

package_data = \
{'': ['*']}

install_requires = \
['volttron>=10.0.1a28,<11.0.0']

setup_kwargs = {
    'name': 'volttron-lib-base-driver',
    'version': '0.1.1a0',
    'description': 'Volttron Driver libraries used to support development within the Volttron Driver Framework.',
    'long_description': '# volttron-lib-base-driver\n\n![Passing?](https://github.com/eclipse-volttron/volttron-lib-base-driver/actions/workflows/run-tests.yml/badge.svg)\n[![pypi version](https://img.shields.io/pypi/v/volttron-lib-base-driver.svg)](https://pypi.org/project/volttron-lib-base-driver/)\n\n\n## Prerequisites\n\n* Python 3.8\n* Poetry\n\n### Python\n\nVolttron Base Driver requires Python 3.8 or above.\n\n\nTo install Python 3.8, we recommend using [pyenv](https://github.com/pyenv/pyenv).\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.8\npyenv install 3.8.10\n\n# make it available globally\npyenv global system 3.8.10\n```\n\n### Poetry\n\nThis project uses `poetry` to install and manage dependencies. To install poetry,\nfollow these [instructions](https://python-poetry.org/docs/master/#installation).\n\n\n\n## Installation and Virtual Environment Setup\n\nSet the environment to be in your project directory:\n\n```poetry config virtualenvs.in-project true```\n\nIf you want to install all your dependencies, including dependencies to help with developing your agent, run this command:\n\n```poetry install```\n\nIf you want to install only the dependencies needed to run your agent, run this command:\n\n```poetry install --no-dev```\n\nTo view all the installed dependencies in your virtual environment, run this command:\n```shell\npoetry show\n```\n\nActivate the virtual environment:\n\n```poetry shell```\n\n\n## Git Setup\n\n1. To use git to manage version control, create a new git repository in your local agent project.\n\n```\ngit init\n```\n\n2. Then create a new repo in your Github or Gitlab account. Copy the URL that points to that new repo in\nyour Github or Gitlab account. This will be known as our \'remote\'.\n\n3. Add the remote (i.e. the new repo URL from your Github or Gitlab account) to your local repository. Run the following command:\n\n```git remote add origin <my github/gitlab URL>```\n\nWhen you push to your repo, note that the default branch is called \'main\'.\n\n\n## Optional Configurations\n\n## Precommit\n\nInstall pre-commit hooks:\n\n```pre-commit install```\n\nTo run pre-commit on all your files, run this command:\n\n```pre-commit run --all-files```\n\nIf you have precommit installed and you want to ignore running the commit hooks\nevery time you run a commit, include the `--no-verify` flag in your commit. The following\nis an example:\n\n```git commit -m "Some message" --no-verify```\n\n# Development\n\nIf you want to use a local version of [volttron-core](https://github.com/VOLTTRON/volttron-core) instead of installing it from PyPi, modify the \'[tool.poetry.dependencies]\' section\nof pyproject.toml to use a local version. To do this, you can run the following command:\n\n```\n# form of the command\n# poetry add <path to my local version of volttron-core> --editable\n\n# example; note that the \'volttron-core\' is located one directory up from the current directory\npoetry add ../volttron-core/ --editable\n```\n\n# Documentation\n\nTo build the docs, navigate to the \'docs\' directory and build the documentation:\n\n```shell\ncd docs\nmake html\n```\n\nAfter the documentation is built, view the documentation in html form in your browser.\nThe html files will be located in `~/<path to agent project directory>/docs/build/html`.\n\n**PROTIP: To open the landing page of your documentation directly from the command line, run the following command:**\n\n```shell\nopen <path to agent project directory>/docs/build/html/index.html\n```\n\nThis will open the documentation landing page in your default browsert (e.g. Chrome, Firefox).\n',
    'author': 'Mark Bonicillo',
    'author_email': 'volttron@pnnl.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eclipse-volttron/volttron-lib-base-driver',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
