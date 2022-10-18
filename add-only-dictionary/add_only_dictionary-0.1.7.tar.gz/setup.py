# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['add_only_dictionary']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1']

entry_points = \
{'console_scripts': ['add-only-dictionary = add_only_dictionary.__main__:main']}

setup_kwargs = {
    'name': 'add-only-dictionary',
    'version': '0.1.7',
    'description': 'Add Only Dictionary',
    'long_description': '# Add Only Dictionary\n\n[![PyPI](https://img.shields.io/pypi/v/add-only-dictionary.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/add-only-dictionary.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/add-only-dictionary)][python version]\n[![License](https://img.shields.io/pypi/l/add-only-dictionary)][license]\n\n[![Read the documentation at https://add-only-dictionary.readthedocs.io/](https://img.shields.io/readthedocs/add-only-dictionary/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/maccam912/add-only-dictionary/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/maccam912/add-only-dictionary/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/add-only-dictionary/\n[status]: https://pypi.org/project/add-only-dictionary/\n[python version]: https://pypi.org/project/add-only-dictionary\n[read the docs]: https://add-only-dictionary.readthedocs.io/\n[tests]: https://github.com/maccam912/add-only-dictionary/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/maccam912/add-only-dictionary\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- Create dictionaries that let you continue adding key/value pairs, but never change existing values or remove existing keys. If a value is a dictionary, that will also be updated to have the same behavior. If the value is a list, items can only be added on to the list, but never removed from any position.\n\n## Installation\n\nYou can install _Add Only Dictionary_ via [pip] from [PyPI]:\n\n```console\n$ pip install add-only-dictionary\n```\n\n## Usage\n\n```python\nfrom add_only_dictionary import AODict\n\nregular_dict: Dict = {"a": 1}\nao_dict: AODict = AODict(regular_dict)\n\nao_dict["b"] = 2 # works!\nao_dict["a"] = 3 # Nothing happens...\nao_dict["a"] == 1 # True, since the key already existed.\n```\n\n<!-- ## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Add Only Dictionary_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description. -->\n\n## Credits\n\nThis project was generated from [@cjolowicz]\'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/maccam912/add-only-dictionary/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/maccam912/add-only-dictionary/blob/main/LICENSE\n[contributor guide]: https://github.com/maccam912/add-only-dictionary/blob/main/CONTRIBUTING.md\n[command-line reference]: https://add-only-dictionary.readthedocs.io/en/latest/usage.html\n',
    'author': 'Matt Koski',
    'author_email': 'maccam912@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/maccam912/add-only-dictionary',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
