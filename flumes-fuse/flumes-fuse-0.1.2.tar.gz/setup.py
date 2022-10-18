# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flumes_fuse']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.26,<2.0.0',
 'flumes>=0.1.4,<0.2.0',
 'fuse-python>=1.0.4,<2.0.0']

entry_points = \
{'console_scripts': ['flumes-fuse = flumes_fuse.fs:run']}

setup_kwargs = {
    'name': 'flumes-fuse',
    'version': '0.1.2',
    'description': 'Tool that generates a userspace filesystem off of a flumes created database',
    'long_description': '<div align="center">\n  <h1>Flumes-fuse\n  <h4>Generate a filesystem from a database created by flumes</h4>\n<div align="center">\n  \n  [![Maintenance](https://img.shields.io/maintenance/yes/2022.svg?style=for-the-badge)](https://img.shields.io/maintenance/yes/2022)\n  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n  [![Pull requests](https://img.shields.io/github/issues-pr-raw/fluendo/flumes-fuse.svg?style=for-the-badge)](https://img.shields.io/github/issues-pr-raw/fluendo/flumes-fuse)\n  [![Contributors](https://img.shields.io/github/contributors/fluendo/flumes-fuse.svg?style=for-the-badge)](https://img.shields.io/github/contributors/fluendo/flumes-fuse)\n  [![License](https://img.shields.io/github/license/fluendo/flumes-fuse.svg?style=for-the-badge)](https://github.com/fluendo/flumes-fuse/blob/master/LICENSE.LGPL)\n  \n</div>\n</div><br>\n  \n# Table of Contents\n- [About the project](#about_the_project)\n    - [Features](#features)\n- [Getting started](#getting_started)\n  - [Supported platforms](#supported_platforms)\n  - [System requirements](#system_requirements)\n  - [Installation](#installation)  \n- [Usage](#usage)\n  - [Tree mode](#tree_mode)\n  - [Search mode](#search_mode)\n- [Development](#development)\n  - [New releases](#new_releases)\n  - [Tagging](#tagging)\n  - [Testing](#testing)\n- [License](#license)\n- [References](#references)\n\n# About the project <a name = "about_the_project"></a>\nFlumes-fuse is a tool that utilises [Fuse](https://github.com/libfuse/libfuse) (Filesystem in Userspace) to generate and mount filesystems out of databases created by [flumes](https://github.com/fluendo/flumes/) tool. The purpose is to provide uncomplicated access to data via basic terminal commands.\n\n## Features <a name = "features"></a>\n* Tree mode: representation of each database file entry and its properties in tree-style hierarchy\n* Search mode: database representation facilitating search by file entry property\n* Direct content access: read media content directly from the filesystem\n\n# Getting started <a name = "getting_started"></a>\n## Supported platforms <a name = "supported_platforms"></a>\nWe depend upon [libfuse](https://github.com/libfuse/libfuse) supported platforms which are the following\n* Linux\n* BSD (partial)\n\n## System requirements <a name = "system_requirements"></a>\n* [Python >=3.9](https://www.python.org/downloads/)\n\n## Installation <a name = "installation"></a>\nFor a successful and complete installation we recommend you to use [*poetry*](https://python-poetry.org/docs/) package manager.\n\n* Install poetry\n```\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -\n```\n\nMake sure you are on the root path of the project repository before running the following commands.\n\n* Install project dependencies\n```\npoetry install\n```\n\n# Usage <a name = "usage"></a>\n\nMount the corresponding *flumes* database by running\n```\nflumes-fuse -s <MOUNT DIR> -o uri=sqlite:///(<RELATIVE PATH TO DB> OR /<ABSOLUTE PATH TO DB>) -f\n```\nNote that directory <MOUNT DIR> should exist, otherwise the command will throw an error. `-f` calls the process in foreground mode.\n\n## Tree Mode <a name = "tree_mode"></a>\nYou can navigate over `flumes` files and read the fields and relationships\n![Tree mode example](rsc/tree-mode.svg)\n\n## Search Mode <a name = "search_mode"></a>\nYou can navigate over `flumes` files by generating queries in the filesystem through paths\n![Search mode example](rsc/search-mode.svg)\n\n# Development <a name = "development"></a>\nThe project is based in `poetry` dependency management and packaging system.\n\n* Install development pre-commit hooks\n```\npoetry run pre-commit install\n```\n\n* Update package dependencies in poetry.lock\n\nThe following command simply updates poetry.lock with the latest versions of the dependencies\n```\npoetry update --lock\n```\nIf you also want poetry to install the latest versions in your local environment\n```\npoetry update\n```\n\n**New releases** <a name = "new_releases"></a>\n\nTo generate a new release you must update the version number. The following files will need to be updated: \n* init file\n* tests/test_flumes_fuse.py\n* pyproject.toml\n\nOnce it is merged, tagging must be done in order to distribute the new version correctly.\n\n**Tagging** <a name = "tagging"></a>\n\n```\ngit tag -a <version> -m "Release <version>"\n```\n```\ngit push origin --tags\n```\n\n## Testing <a name = "testing"></a>\nAll tests are located in the `tests` folder. The framework used is [*pytest*](https://docs.pytest.org/). \n* Run all tests with poetry \n```\npoetry run pytest\n```\n\n# License <a name = "license"></a>\nSee `LICENSE.LGPL` for more information.\n\n# References <a name = "references"></a>\n* [Flumes](https://github.com/fluendo/flumes)\n* [Poetry Template](https://github.com/yunojuno/poetry-template)\n* [Asciinema](https://asciinema.org/)\n* [Svg-term-cli](https://github.com/marionebl/svg-term-cli)\n',
    'author': 'Jorge Zapata',
    'author_email': 'jorgeluis.zapata@gmail.com',
    'maintainer': 'Michalis Dimopoulos',
    'maintainer_email': 'mdimopoulos@fluendo.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
