# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ankamantatra', 'ankamantatra.commands', 'ankamantatra.models']

package_data = \
{'': ['*']}

install_requires = \
['click-help-colors>=0.9.1,<0.10.0', 'click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['ankamantatra = ankamantatra.__main__:main']}

setup_kwargs = {
    'name': 'ankamantatra',
    'version': '1.0.0',
    'description': 'A simple CLI quizz game',
    'long_description': '# 🤔 ankamantatra\n**Techzara WCC2 final week**\n\nA simple CLI quizz game.\n\nThe name *ankamantatra* is a malagasy word that means *riddle*.\n\nThe user can play within a specific category or mix them all.\nA game session consists of 4 questions, each of different type.\nA the end of a session, the user is prompted whether he wants to play again or not.\n\n![preview.gif](preview.gif)\n\n## ⚒️ Installation\nTo install from [pypi](https://pypi.org/project/ankamantatra/), type in the terminal:\n```sh\npip install ankamantatra\n```\nOr you can clone this repository and install it manually using [poetry](https://python-poetry.org/),  a tool for dependency management and packaging in Python, by following the following steps :\n```sh\ngit clone https://github.com/twisty-team/ankamantatra.git\n```\n```sh\npip install poetry\n```\n```sh\n# in the project root directory\npoetry build && poetry install\n```\nIn some cases you may get a `KeyringLocked` error that you can bypass by typing :\n```sh\nexport PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring\n```\n## 🏃 How to run\nIf you installed the package with pip, you can run the game by typing in the terminal :\n```sh\nankamantatra\n```\nIf you installed it manually using poetry, you can run the game by typing :\n```sh\npoetry run python -m ankamantatra\n```\n## ▶ Usage\n```\nUsage: ankamantatra [OPTIONS] COMMAND [ARGS]...\n\n  A simple quizz game CLI\n\nOptions:\n  --version  Show the version and exit.\n  --help     Show this message and exit.\n\nCommands:\n  list  List all available questions to play with.\n  play  Use to play quiz game\n\n```\n\n```\nUsage: python -m ankamantatra play [OPTIONS]\n\n  Use to play quiz game\n\nOptions:\n  -c, --categorie TEXT  Specify Quiz categorie\n  --help                Show this message and exit.\n```\n\n```\nUsage: python -m ankamantatra list [OPTIONS]\n\n  List all available questions to play with.\n\nOptions:\n  -c, --category TEXT   Filter by TEXT\n  -sa, --show-answer\n  -sc, --show-category\n  --category-only       Show only the categories and hide questions\n  --help                Show this message and exit.\n```\n\n## 🚀 Features\n- Play quizz\n- List questions or categories\n\n## Authors\n\n* [tbgracy](https://github.com/tbgracy)\n\n* [rhja](https://github.com/radoheritiana)\n',
    'author': 'Tsierenana Bôtramanagna Gracy',
    'author_email': 'gtsierenana@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
