# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.kronos']

package_data = \
{'': ['*']}

install_requires = \
['pytz>=2022.1,<2023.0']

setup_kwargs = {
    'name': 'kronos-daterange',
    'version': '0.0.1',
    'description': 'Kronos makes date ranges easier.',
    'long_description': '\n# Kronos\n\n\n<div align="center">\n\n[![PyPI - Version](https://img.shields.io/pypi/v/kronos.svg)](https://pypi.python.org/pypi/kronos)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kronos.svg)](https://pypi.python.org/pypi/kronos)\n[![Tests](https://github.com/nat5142/kronos/workflows/tests/badge.svg)](https://github.com/nat5142/kronos/actions?workflow=tests)\n[![Codecov](https://codecov.io/gh/nat5142/kronos/branch/main/graph/badge.svg)](https://codecov.io/gh/nat5142/kronos)\n[![Read the Docs](https://readthedocs.org/projects/kronos/badge/)](https://kronos.readthedocs.io/)\n[![PyPI - License](https://img.shields.io/pypi/l/kronos.svg)](https://pypi.python.org/pypi/kronos)\n\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n\n\n</div>\n\n\nKronos makes dateranges easier.\n\n\n* GitHub repo: <https://github.com/nat5142/kronos.git>\n* Documentation: <https://kronos.readthedocs.io>\n* Free software: BSD\n\n\n## Features\n\n* TODO\n\n## Quickstart\n\nTODO\n\n## Credits\n\nThis package was created with [Cookiecutter][cookiecutter] and the [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.\n\n[cookiecutter]: https://github.com/cookiecutter/cookiecutter\n[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage\n',
    'author': 'Nick Tulli',
    'author_email': 'ntulli.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nat5142/kronos',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
