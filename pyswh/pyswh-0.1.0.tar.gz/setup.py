# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyswh']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pyswh',
    'version': '0.1.0',
    'description': 'A Python wrapper for the Software Heritage API',
    'long_description': '<!--\nSPDX-FileCopyrightText: 2022 Stephan Druskat <pyswh@sdruskat.net>\n\nSPDX-License-Identifier: CC-BY-4.0\n-->\n\n# *pyswh* - a Python wrapper library for the Software Heritage API\n\n*pyswh* aims to wrap interactions with the [Software Heritage REST API](https://archive.softwareheritage.org/api/1/) into a comfortable Python API.\n\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sdruskat_pyswh&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=sdruskat_pyswh)\n[![Docs build](https://readthedocs.org/projects/pyswh/badge/?version=latest)](https://pyswh.readthedocs.io/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/sdruskat/pyswh/branch/develop/graph/badge.svg?token=8IDQ3BXC4M)](https://codecov.io/gh/sdruskat/pyswh)\n[![REUSE status](https://api.reuse.software/badge/github.com/sdruskat/pyswh)](https://api.reuse.software/info/github.com/sdruskat/pyswh)\n\n## Getting started\n\nInstall `pyswh` via pip:\n\n```bash\npip install pyswh\n```\n\nInclude `pyswh` in your project by adding a respective dependency to your project, e.g.,\n\n```bash\n# requirements.txt\npyswh==0.1.0\n```\n\n```toml\n# Poetry pyproject.toml\n[tool.poetry.dependencies]\npyswh = "^0.1.0"\n```\n\nYou can now use `pyswh`:\n\n```python\nfrom pyswh import swh\nfrom pyswh import errors as swh_errors\n\ntry:\n    swh.save(\'https://github.com/sdruskat/pyswh\', False, \'SWH-API-AUTH-TOKEN\')\nexcept swh_errors.SwhSaveError as sse:\n    raise sse\n```\n\nRefer to the [complete documentation](https://pyswh.readthedocs.io/en/latest/) to learn more about using `pyswh`.\n\n## Set up for development\n\n**Requirements:** Python >= 3.10.0.\n\n1. Install [Poetry](https://python-poetry.org).\n\n2. Clone the repository:\n\n```bash\ngit clone git@github.com:sdruskat/pyswh.git\n```\n\n3. Create a virtual environment in `.venv`:\n```bash\npython3.10 -m venv .venv \n```\n\n4. Activate the Poetry shell and install project:\n\n```bash\npoetry shell\npoetry install\n```\n\n## Testing\n\n`pyswh` uses `pytest` for testing. To run all tests, do:\n\n```bash\npoetry shell\npoetry run pytest test/\n```\n\n## Building documentation locally\n\nInitialize the Poetry virtual environment with `poetry shell`, go into the `docs/` folder and run `make html`.\n\n## Licensing\n\nSee [`LICENSE.md`](LICENSE.md)',
    'author': 'Stephan Druskat',
    'author_email': 'pyswh@sdruskat.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sdruskat/pyswh',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
