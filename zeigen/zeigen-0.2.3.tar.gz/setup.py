# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src', 'rcsbsearch': 'src/rcsbsearch'}

packages = \
['rcsbsearch', 'zeigen']

package_data = \
{'': ['*'], 'rcsbsearch': ['resources/*'], 'zeigen': ['templates/*']}

install_requires = \
['attrs>=21.4.0',
 'biopython>=1.79',
 'colorama>=0.4.4',
 'dotli>=1.1',
 'dynaconf>=3.1.7',
 'gemmi>=0.5.2',
 'gql[all]>=3.0.0',
 'jsonschema>=4.16.0,<5.0.0',
 'loguru>=0.6.0',
 'matplotlib>=3.5.1',
 'numpy>=1.22.1',
 'pandas>=1.4.0',
 'pint>=0.18',
 'pyarrow>=9.0.0',
 'requests>=2.28.1,<3.0.0',
 'schema>=0.7.5',
 'scipy>=1.7.3',
 'statsdict>=0.1.5',
 'tabulate>=0.8.9',
 'toml>=0.10.2',
 'tqdm>=4.64.1',
 'typer>=0.4.0',
 'uncertainties>=3.1.6']

entry_points = \
{'console_scripts': ['zeigen = zeigen.__main__:main']}

setup_kwargs = {
    'name': 'zeigen',
    'version': '0.2.3',
    'description': 'Find water networks in atomic-resolution crystal structures',
    'long_description': "# Zeigen - Show Water Networks\n\n[![PyPI](https://img.shields.io/pypi/v/zeigen.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/zeigen)][pypi status]\n[![Docs](https://img.shields.io/readthedocs/zeigen/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/hydrationdynamics/zeigen/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/hydrationdynamics/zeigen/branch/main/graph/badge.svg)][codecov]\n[![Repo](https://img.shields.io/github/last-commit/hydrationdynamics/zeigen)][repo]\n[![Downloads](https://pepy.tech/badge/zeigen)][downloads]\n[![Dlrate](https://img.shields.io/pypi/dm/zeigen)][dlrate]\n[![Codacy](https://app.codacy.com/project/badge/Grade/3e29ba5ba23d48888372138790ab26f3)][codacy]\n[![Snyk Health](https://snyk.io/advisor/python/zeigen/badge.svg)][snyk]\n\n[pypi status]: https://pypi.org/project/zeigen/\n[read the docs]: https://zeigen.readthedocs.io/\n[tests]: https://github.com/hydrationdynamics/zeigen/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/hydrationdynamics/zeigen\n[repo]: https://github.com/hydrationdynamics/zeigen\n[downloads]: https://pepy.tech/project/zeigen\n[dlrate]: https://github.com/hydrationdynamics/zeigen\n[codacy]: https://www.codacy.com/gh/hydrationdynamics/zeigen?utm_source=github.com&utm_medium=referral&utm_content=hydrationdynamics/zeigen&utm_campaign=Badge_Grade\n[snyk]: https://snyk.io/advisor/python/zeigen\n\n[![logo](https://raw.githubusercontent.com/hydrationdynamics/zeigen/main/docs/_static/logo.png)][logo license]\n\n[logo license]: https://raw.githubusercontent.com/hydrationdynamics/zeigen/main/LICENSE.logo.txt\n\n## Features\n\n_Zeigen_ finds networks of water in PDB structures.\nThe PDB query is highly configurable through the `zeigen.conf`\nconfiguration file that is placed in the config\ndirectory upon first program run. The query results are\nplaced in a TSV file, with global stats to a JSON file.\n\n_Zeigen_ uses _rcsbsearch_ to query the PDB. Currently the\n_rcsbsearch_ package is broken, as it uses the obsolete v1\nquery. _Zeigen_ includes a copy of _rcsbsearch_ which has\nbeen patched for v2 queries.\n\n## Requirements\n\n_Zeigen_ has been developed under Python 3.10 and\ntested on Python 3.9 and 3.10 on Linux. Works on MacOS, but\nnot tested due to energy costs.\n\n## Installation\n\nYou can install _Zeigen_ via [pip] from [PyPI]:\n\n```console\n$ pip install zeigen\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [BSD 3-Clause license][license],\n_Zeigen_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\n_Zeigen_ was written by Joel Berendzen.\n\n_rcsbsearch_ was written by Spencer Bliven.\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/hydrationdynamics/zeigen/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/hydrationdynamics/zeigen/blob/main/LICENSE\n[contributor guide]: https://github.com/hydrationdynamics/zeigen/blob/main/CONTRIBUTING.md\n[command-line reference]: https://zeigen.readthedocs.io/en/latest/usage.html\n",
    'author': 'Joel Berendzen',
    'author_email': 'joel@generisbio.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hydrationdynamics/zeigen',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.1,<3.11',
}


setup(**setup_kwargs)
