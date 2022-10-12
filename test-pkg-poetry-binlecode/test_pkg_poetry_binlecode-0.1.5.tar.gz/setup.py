# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_pkg_poetry_binlecode']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'test-pkg-poetry-binlecode',
    'version': '0.1.5',
    'description': '',
    'long_description': '# test package build with poetry\n\nComparing to setuptools, poetry is all-in-one shop and with less manual\nconfiguration in python package development cycle.\nFor example, `pyproject.toml` is created by poetry with format of PEP 518\npackage specs with `poetry new` command.\n\n```sh\npyenv shell 3.9.11\npython -m venv ./venv\nsource venv/bin/activate\npython -m pip install --upgrade pip\npip install poetry\n```\n\n## package initialization\n\nUse poetry to initialzes a package under project root:\n\n```sh\npoetry new test_pkg_poetry_binlecode\n```\n\nUse poetry to add dependencies, they are added to pyproject.toml by poetry\nautomatically.\n\n```sh\n# add pytest as dev dependency\npoetry add pytest --dev\n# show dependency tree\npoetry show --tree\n# generate lock file\npoetry lock\n\n# The install command reads the pyproject.toml file from the current project,\n# resolves the dependencies, and installs them.\n# If poetry.lock exists, the lock file is used instead of resolving dependencies.\npoetry install\n\npoetry export --output requirements.txt\n```\n\n## testing with pytest\n\nRun pytest at project root level, it will scan tests folder and test scripts.\n\n```sh\npoetry run pytest\n```\n\n## source code formatting with black\n\n```sh\npoetry run black .\n```\n\n## build distribution and publish\n\nCheck package and build distribution. Poetry builds both source and wheel\ndistributions.\n\n```sh\npoetry check\npoetry build\n```\n\nTo publish to pypi, config api token first.\n\n```sh\npoetry config pypi-token.pypi <my-token>\n```\n\nPoetry can use token to publish:\n\n```sh\npoetry publish\n\nPublishing test-pkg-poetry-binlecode (0.1.0) to PyPI\n - Uploading test-pkg-poetry-binlecode-0.1.0.tar.gz 100%\n - Uploading test_pkg_poetry_binlecode-0.1.0-py3-none-any.whl 100%\n```\n',
    'author': 'Bin Le',
    'author_email': 'bin.le.code@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/binlecode/example-python-poetry',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
