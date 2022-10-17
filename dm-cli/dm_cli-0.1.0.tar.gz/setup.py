# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['app']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'dmss-api>=0.3.21,<0.4.0',
 'progress>=1.6,<2.0',
 'pyperclip>=1.8.2,<2.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'dm-cli',
    'version': '0.1.0',
    'description': 'CLI tool for the development framework',
    'long_description': "[![PyPi version](https://img.shields.io/pypi/v/dm-cli)](https://pypi.org/project/dm-cli)\n[![PyPi downloads](https://img.shields.io/pypi/dm/dm-cli)](https://pypi.org/project/dm-cli)\n![Visitors](https://api.visitorbadge.io/api/visitors?path=equinor%2Fdm-cli&countColor=%23263759&style=flat)\n\n# Data Modelling CLI Tool\n\n### Requirements\nThis package requires Python 3.\n\n### Installing\nTo install this CLI tool you can run the below command\n```sh\n$ pip3 install dm-cli\n```\n\nAlternatively, you clone this repo and then run this command from within the repository folder\n```sh\n$ pip3 install .\n```\n\nBoth the above commands would install the package globally and `dm` will be available on your system.\n\n### Usage\n\n```sh\n$ dm --help\nUsage: python -m dm [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -t, --token TEXT  Token for authentication against DMSS.\n  -u, --url TEXT    URL to the Data Modelling Storage Service (DMSS).\n  -h, --help        Show this message and exit.\n\nCommands:\n  ds     Subcommand for working with data sources\n  init   Initialize the data sources and import all packages.\n  pkg    Subcommand for working with packages\n  reset  Reset all data sources (deletes and reuploads packages)\n```\n\nFor each of the `commands` listed above, you can run `dm <COMMAND> --help` to see subcommand-specific help messages, e.g. `dm ds import --help` or `dm pkg --help`\n\n#### Expected directory structure\nCertain commands expect a specific directory structure, such as the commands `dm reset`, `dm init`, and `dm ds reset`.\nFor these commands, the `path` argument must be the path to a directory with two subdirectories, `data_sources` and `data`.\n\n```sh\n$ tree app\napp\n├── data\n│\xa0\xa0 └── DemoApplicationDataSource\n│\xa0\xa0     ├── instances\n│\xa0\xa0     │\xa0\xa0 └── demoApplication.json\n│\xa0\xa0     └── models\n│\xa0\xa0         └── DemoApplication.json\n└── data_sources\n    └── DemoApplicationDataSource.json\n```\n\n#### General\nInitialize the data sources\n\n*i.e. import datasources and their packages*\n\n```sh\n$ dm init [<path>]\n# By default, the `PATH` argument is set to the current working directory\n$ dm init\n# Optionally specify a path to the directory containing data sources and data\n$ dm init app/\n```\n\nReset all data sources\n\n*i.e. delete all datasources and packages, before reuploading them*\n\n```sh\n# Reset all datasources and their packages\n$ dm reset [<path>]\n# By default, the `path` argument is set to the current working directory\n$ dm reset\n# Optionally specify a path to the directory containing data sources and data\n$ dm reset app/\n```\n\n#### Datasources\nImport a datasource\n\n```sh\n# Import a datasource, where <path> is the path to a data source definition (JSON)\n$ dm ds import <path>\n$ dm ds import app/data_sources/DemoApplicationDataSource.json\n```\n\nImport all datasources\n\n```sh\n# Import all datasources found in the directory given by 'path'\n$ dm ds import-all <path>\n$ dm ds import-all app/data_sources\n```\n\nReset a datasource\n\n*i.e. reset the given data source, deleting all packages and reuploading them*\n\n```sh\n$ dm ds reset <data_source> [<path>]\n# By default, the `path` argument is set to the current working directory\n$ dm ds reset DemoApplicationDataSource\n# Optionally specify a path to the directory containing data sources and data\n$ dm ds reset DemoApplicationDataSource app/\n```\n\n#### Packages\nImport a package\n> Note that importing a package will delete any preexisting package with the same name, if present in DMSS\n\n```sh\n# Import the package <path> to the given data source\n$ dm pkg import <path> <data_source>\n# Import the package 'models' from app/data/DemoApplicationDataSource'\n$ dm pkg import app/data/DemoApplicationDataSource/models DemoApplicationDataSource\n```\n\nImport all packages\n\n```sh\n# Import all packages found in the directory given by <path>\n$ dm pkg import-all <path> <data_source>\n# Import all packages in 'app/data/DemoApplicationDataSource'\n$ dm pkg import-all app/data/DemoApplicationDataSource DemoApplicationDataSource\n```\n\nDelete a package\n\n```sh\n# Delete the package from the datasource in DMSS\n$ dm pkg delete <data_source> <package_name>\n# Delete the package 'models' from 'DemoApplicationDataSource'\n$ dm pkg delete DemoApplicationDataSource models\n```\n\nDelete all packages\n> Note that this will only delete packages which are present in the directory <path>, so any package present in DMSS but absent in the given directory will not be removed.\n\n```sh\n# Delete all packages found in the directory given by <path>\n$ dm pkg delete-all <data_source> <path>\n$ dm pkg delete-all DemoApplicationDataSource app/data/DemoApplicationDataSource\n```\n\n### Development\n> You need to have DMSS running locally.\n\n```sh\n$ python3 -m venv .venv\n$ source .venv/bin/activate\n$ pip3 install -e .\n$ dm init\n```\n\n#### Testing\n\n1. Install the dev dependencies: `pip3 install -r dev-requirements.txt`\n2. Run the tests: `pytest`\n\n### Feedback\nPlease feel free to leave feedback in issues/PRs.",
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
