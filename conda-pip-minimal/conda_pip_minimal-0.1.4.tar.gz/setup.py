# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['conda_pip_minimal']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=5.0.0,<6.0.0',
 'loguru>=0.6.0,<0.7.0',
 'more-itertools>=8.14.0,<9.0.0',
 'ruamel-yaml>=0.17.21,<0.18.0',
 'semver>=2.13.0,<3.0.0',
 'trio>=0.22.0,<0.23.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['conda-cpm = conda_pip_minimal.cli:app']}

setup_kwargs = {
    'name': 'conda-pip-minimal',
    'version': '0.1.4',
    'description': 'Conda+Pip minimal env exports',
    'long_description': '# conda cpm\n\nSimple tool to generate minimal versions of Conda environments, also including\n`pip` dependencies, for cross-platform sharing.\n\nBuilt on top of [`conda tree`](https://github.com/conda-incubator/conda-tree) and [`pipdeptree`](https://github.com/tox-dev/pipdeptree). Inspired by [`conda minify`](https://github.com/jamespreed/conda-minify).\n\n## Why use `conda cpm`?\n\n-   Conda (especially with mamba) is a great tool to manage Python virtual\n    environments, especially if you need to install some non-Python dependencies,\n    or use compiled dependencies like CUDA. See\n    <https://aseifert.com/p/python-environments/> for more on this.\n\n-   I use Conda preferentially to install any packages available through it; and\n    provide my virtualenv&rsquo;s Python version through Conda.\n\n-   Some packages are not easily accessible on Conda, and I use `pip` or `poetry`\n    (or `hatch` or your other tool of choice) to pull those packages in.\n\n-   This approach works remarkably well, but when it is time to share my\n    environment with others, there are several ways to do it, and they are subtly\n    different in capabilities and issues.\n\n    e.g\n\n    -   `conda env export`, `conda env export --from-history`, `conda list --export`\n\n    -   For pip-installed packages, `pip freeze`, `pip list --freeze`, or whatever\n        your favorite Python package manager provides.\n\n    -   conda-lock, pipenv, and other lock file generating tools\n\n-   If the exported file is too specific, specifying every dependency and build\n    identifier, it often cannot be reproduced on a different platform because\n    these are not portable.\n\n-   If you use both `conda` and `pip`, these tools will typically be unaware of\n    each other, generating overlapping requirements files.\n\n## How does `conda cpm` solve this?\n\n-   `conda cpm` constructs a minimal `environment.yml` file, with only the\n    "leaves" of the dependency tree, both for `pip` and `conda`.\n\n-   It retains information about which packages came from Conda and which came\n    from Pip, but does not include dependencies in the export.\n\n-   It specifies exact versions by default, but it can optionally relax the\n    version requirements to being flexible at the patch level or minor level\n    (semver).\n\n-   It can optionally include info about which Conda channel a package came from,\n    the Python version, or any manually specified packages.\n\n-   It does not include system-specific information like the Conda environment\n    prefix.\n\n## Installation\n\n### via pip\n\n```console\npip install conda-pip-minimal\n```\n\n### via pipx\n\n```console\npipx install conda-pip-minimal\n```\n\n### Run without installing\n\n```console\npipx run conda-pip-minimal --help\n```\n\n## Usage\n\nThe script for this package is named `conda-cpm`; so it can be run like `conda cpm`\n\n```console\n$ conda cpm [OPTIONS]\n```\n\n### Options:\n\n  * `-p, --prefix PATH`: Conda env prefix\n  * `-n, --name TEXT`: Conda env name\n  * `--pip / --no-pip`: Include pip dependencies  [default: True]\n  * `--relax [none|major|minor|full]`: [default: full]\n  * `--include TEXT`: Packages to always include  [default: python, pip]\n  * `--exclude TEXT`: Packages to always exclude  [default: ]\n  * `--channel / --no-channel`: Add channel to conda dependencies  [default: False]\n  * `--debug / --no-debug`: [default: False]\n  * `--help`: Show this message and exit.\n\n## Examples\n\nHere are a few example runs for this package:\n\n### From within the conda environment:\n\n``` shell\n❯ conda cpm\ndependencies:\n- python=3.8.13\n- pip=22.2.2\n- pip:\n  - conda-pip-minimal==0.1.0\n  - ipython==8.5.0\n  - snoop==0.4.2\n  - trio-typing==0.7.0\nname: /home/venky/dev/conda-pip-minimal/.venv\n```\n\n### Specifying the conda environment\n\n``` shell\n❯ conda cpm --prefix ~/dev/conda-pip-minimal/.venv\ndependencies:\n- pip=22.2.2\n- python=3.8.13\n- pip:\n  - conda-pip-minimal==0.1.0\n  - ipython==8.5.0\n  - snoop==0.4.2\n  - trio-typing==0.7.0\nname: /home/venky/dev/conda-pip-minimal/.venv\n```\n\n### Exclude packages\n\n``` shell\n❯ conda cpm --prefix ~/dev/conda-pip-minimal/.venv --exclude snoop --exclude trio-typing\ndependencies:\n- python=3.8.13\n- pip=22.2.2\n- pip:\n  - conda-pip-minimal==0.1.0\n  - ipython==8.5.0\nname: /home/venky/dev/conda-pip-minimal/.venv\n```\n\n### Include a normally-excluded dependency\n\n``` shell\n❯ conda cpm --prefix ~/dev/conda-pip-minimal/.venv --include trio\ndependencies:\n- trio=0.22.0\n- pip:\n  - conda-pip-minimal==0.1.0\n  - ipython==8.5.0\n  - snoop==0.4.2\n  - trio-typing==0.7.0\nname: /home/venky/dev/conda-pip-minimal/.venv\n```\n\n### Specify conda channels\n\n``` shell\n❯ conda cpm --prefix ~/dev/conda-pip-minimal/.venv --channel\ndependencies:\n- conda-forge::python=3.8.13\n- conda-forge::pip=22.2.2\n- pip:\n  - conda-pip-minimal==0.1.0\n  - ipython==8.5.0\n  - snoop==0.4.2\n  - trio-typing==0.7.0\nname: /home/venky/dev/conda-pip-minimal/.venv\n```\n\n### Relax versions\n\n``` shell\n❯ conda cpm --prefix ~/dev/conda-pip-minimal/.venv --relax minor\ndependencies:\n- python=3.8.*\n- pip=22.2.*\n- pip:\n  - conda-pip-minimal==0.1.*\n  - ipython==8.5.*\n  - snoop==0.4.*\n  - trio-typing==0.7.*\nname: /home/venky/dev/conda-pip-minimal/.venv\n```\n\n### Skip pip dependencies\n\nWhy would you want to do this, though?\n\n``` shell\n❯ conda cpm --prefix ~/dev/conda-pip-minimal/.venv --no-pip\ndependencies:\n- pip=22.2.2\n- python=3.8.13\nname: /home/venky/dev/conda-pip-minimal/.venv\n```\n',
    'author': 'Venky Iyer',
    'author_email': 'indigoviolet@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/indigoviolet/conda-pip-minimal',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
