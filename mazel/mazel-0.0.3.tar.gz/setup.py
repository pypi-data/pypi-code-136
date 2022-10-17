# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mazel', 'mazel.commands', 'mazel.contrib', 'mazel.runtimes']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'tomlkit>=0.11.5,<0.12.0']

extras_require = \
{'yaml': ['ruamel.yaml>=0.17.21,<0.18.0']}

entry_points = \
{'console_scripts': ['mazel = mazel.main:cli']}

setup_kwargs = {
    'name': 'mazel',
    'version': '0.0.3',
    'description': 'Simple bazel-inspired Makefile runner for monorepos',
    'long_description': "# mazel: make helpers for monorepos\n\n>  bazel(-ish) for Makefiles = **mazel**\n\n`mazel` is a simple [bazel](https://bazel.build/)-inspired Makefile-based build system for monorepos.\n\nThe goal is to not create another build system, rather we provide simple helpers around GNU `make`, along with common (though not required) Makefile patterns.\n\nmazel provides:\n1. Ability to execute make targets in one or more subpaths.\n2. Dependency graph to allow execution of targets in a logical order. Either parsed from the package manager (e.g. poetry's `pyproject.toml` or npm's `package.json`).\n\n\n```\nmazel test //libs/py/common          # Runs `make test` for the common library\nmazel test                           # Runs tests for any packages under the current directory\nmazel format //libs/py               # Code formats all code under libs/py\nmazel run //tools/docker/base:image  # Builds the base docker image\n```\n\nSee https://mazel.readthedocs.io/ for more info\n",
    'author': 'John Paulett',
    'author_email': 'john.paulett@equium.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/equium-io/mazel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
