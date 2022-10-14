# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gh_py', 'gh_py.internal', 'gh_py.scaffolding']

package_data = \
{'': ['*']}

install_requires = \
['cleo>=1.0.0a,<2.0.0']

entry_points = \
{'console_scripts': ['gh-py = gh_py.cli:run']}

setup_kwargs = {
    'name': 'gh-py',
    'version': '1.2.0',
    'description': 'Write GH Extensions with Python',
    'long_description': '# GH-PY\n\n[![Build Status](https://github.com/JessicaTegner/gh-py/actions/workflows/ci.yaml/badge.svg)](https://github.com/JessicaTegner/gh-py/actions/workflows/ci.yaml)\n[![GitHub Releases](https://img.shields.io/github/tag/JessicaTegner/gh-py.svg)](https://github.com/JessicaTegner/gh-py/releases)\n[![gh-py PyPI Version](https://img.shields.io/pypi/v/gh-py?label=gh-py+pypi+version)](https://pypi.org/project/gh-py/)\n[![Development Status](https://img.shields.io/pypi/status/gh-py.svg)](https://pypi.python.org/pypi/gh-py/)\n[![gh-py Python version](https://img.shields.io/pypi/pyversions/gh-py.svg)](https://pypi.python.org/pypi/gh-py/)\n![License](https://img.shields.io/pypi/l/gh-py.svg)\n\n\ngh-py gh extensions, now made easy in python.\n\ngh-py makes it possible to write gh extensions, and interact with the gh cli directly from python.\n\n### Installation\n\ngh-py can be installed in a few different ways.\n\n#### From GH.\n\nTo use this method, you\'ll have to have at least gh version 2.0.0 or newer installed.\n\n```\ngh extension install JessicaTegner/gh-py\n```\n\n\n#### from pip\n\ngh-py is also available on pip.\n\n```\n$ pip install gh-py\n```\n\n\n\n#### From GitHub\n\nYou can also clone and install gh-py from GitHub, useful if you want to contribute to gh-py development.\n\n```\n$git clone https://github.com/JessicaTegner/gh-py.git\n$ cd gh-py\n$ poetry install\n```\n\n### Usage:\n\n#### Creating your extension\n\nTo get started, create your extension scaffolding.\n\n```\n$ gh py create gh-example\n# or if you installed through pip\n$ gh-py create gh-example\nInstalling extension environment.\nExtension environment installed.\nCreating extension gh-example\nCreating scaffolding...\nCreated extension gh-example\n````\n\nThen go into your newly created directory, and take a look.\n\n* extension.py - Here is the entry point to your extension.\n* gh-example (or what ever else you called your extension) - This is the file that is the bridge between ghs extension system and our python world.\n* pyproject.toml - Basic pyproject.toml file, used to describe our project to poetry.\n\n\n#### Useful tips while developing your extension\n\nWhen using gh-py\'s scaffolding, you have the full power of [poetry](https://python-poetry.org/) at your disposal.  \nThat means you can add, update, change or remove dependencies as you wish.  \n\nThe way to do it here, is to use the build in poetry command in the scaffolding, like so:\n\n```\n# Here\'s some examples.\n# Note the "gh-example" is the executable for your extension.\n\n$ gh-example poetry add requests\n$ gh-example poetry remove requests\n\n```\n\nWhen you update your extension down the line, the scaffolding will take care to update the extension environment, when the end user updates your extension.  \nNote: For this to work, it is important to **not** commit the generated **poetry.lock** file.\n\n\n#### Publishing your Extension\n\nAfter writing your python code, the way to publish your extension, is as with any other.\n\n```\n# setup a git repository\n$ git init -b main\n$ git add .\n$ git commit -m "Initial extension code."\n# then create the repository on GitHub\n$ gh repo create\n```\n\n\n### Contributing\n\nContributions are welcome. When opening a PR, please keep the following guidelines in mind:\n\n1. Before implementing, please open an issue for discussion.\n2. Make sure you have tests for the new logic.\n3. Add yourself to contributors at `README.md` unless you are already there. In that case tweak your contributions.\n\n\n#### Contributors\n\n* [Jessica Tegner](https://github.com/JessicaTegner) - Maintainer\n\n\n### License\n\nPy-GH is available under MIT license. See LICENSE for more details.\n',
    'author': 'JessicaTegner',
    'author_email': 'jessica.tegner@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JessicaTegner/gh-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
