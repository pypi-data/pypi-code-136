# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tiny_thumbnail_engine',
 'tiny_thumbnail_engine.server',
 'tiny_thumbnail_engine.storage']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.1.0,<23.0.0']

extras_require = \
{'server': ['pyvips>=2.2.1,<3.0.0', 'boto3>=1.24.89,<2.0.0']}

setup_kwargs = {
    'name': 'tiny-thumbnail-engine',
    'version': '0.2.0',
    'description': 'Tiny Thumbnail Engine',
    'long_description': "# Tiny Thumbnail Engine\n\n[![PyPI](https://img.shields.io/pypi/v/tiny-thumbnail-engine.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/tiny-thumbnail-engine.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/tiny-thumbnail-engine)][python version]\n[![License](https://img.shields.io/pypi/l/tiny-thumbnail-engine)][license]\n\n[![Read the documentation at https://tiny-thumbnail-engine.readthedocs.io/](https://img.shields.io/readthedocs/tiny-thumbnail-engine/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/john-parton/tiny-thumbnail-engine/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/john-parton/tiny-thumbnail-engine/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/tiny-thumbnail-engine/\n[status]: https://pypi.org/project/tiny-thumbnail-engine/\n[python version]: https://pypi.org/project/tiny-thumbnail-engine\n[read the docs]: https://tiny-thumbnail-engine.readthedocs.io/\n[tests]: https://github.com/john-parton/tiny-thumbnail-engine/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/john-parton/tiny-thumbnail-engine\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Tiny Thumbnail Engine_ via [pip] from [PyPI]:\n\n```console\n$ pip install tiny-thumbnail-engine\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Tiny Thumbnail Engine_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/john-parton/tiny-thumbnail-engine/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/john-parton/tiny-thumbnail-engine/blob/main/LICENSE\n[contributor guide]: https://github.com/john-parton/tiny-thumbnail-engine/blob/main/CONTRIBUTING.md\n[command-line reference]: https://tiny-thumbnail-engine.readthedocs.io/en/latest/usage.html\n",
    'author': 'John Parton',
    'author_email': 'john.parton.iv@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/john-parton/tiny-thumbnail-engine',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
