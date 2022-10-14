# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['noveldown', 'noveldown.sources']

package_data = \
{'': ['*']}

install_requires = \
['EbookLib>=0.17.1,<0.18.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'httpx>=0.23.0,<0.24.0',
 'lxml>=4.8.0,<5.0.0',
 'requests>=2.27.1,<3.0.0',
 'typer>=0.5.0,<0.6.0']

entry_points = \
{'console_scripts': ['noveldown = noveldown.cli:main']}

setup_kwargs = {
    'name': 'noveldown',
    'version': '1.2.0',
    'description': 'Webnovel downloader and EPUB converter',
    'long_description': '# Noveldown\n\n![Supported Python versions](https://img.shields.io/pypi/pyversions/noveldown)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n[![Download from PyPI](https://img.shields.io/pypi/v/noveldown)](https://pypi.org/project/noveldown)\n[![Download from the AUR](https://img.shields.io/aur/version/noveldown-git)](https://aur.archlinux.org/packages/noveldown-git)\n[![Latest release](https://img.shields.io/github/v/release/potatoeggy/noveldown?display_name=tag)](https://github.com/potatoeggy/noveldown/releases/latest)\n[![License](https://img.shields.io/github/license/potatoeggy/noveldown)](/LICENSE)\n\nWebnovel downloader and converter to EPUB (with metadata!) as a Python library and command line application.\n\n## Supported stories\n\nTo request a new story, please file a [new issue](https://github.com/potatoeggy/noveldown/issues/new).\n\n- [The Wandering Inn](https://wanderinginn.com) - pirate aba\n- [A Practical Guide to Evil](https://practicalguidetoevil.wordpress.com) - ErraticErrata\n- [Pale](https://palewebserial.wordpress.com/) - Wildbow\n\n## Installation\n\nInstall the package from PyPI:\n\n```\npip3 install noveldown\n```\n\nArch Linux users may also install the package from the [AUR](https://aur.archlinux.org/packages/noveldown-git.git):\n\n```\ngit clone https://aur.archlinux.org/noveldown-git.git\nmakepkg -si\n```\n\nOr, to build from source:\n\nNoveldown depends on [poetry](https://github.com/python-poetry/poetry) for building.\n\n```\ngit clone https://github.com/potatoeggy/noveldown.git\npoetry install\npoetry build\npip3 install dist/noveldown*.whl\n```\n\n## Usage\n\nTo download the novel as an EPUB:\n\n```\nnoveldown <ID>\n\n# for example:\nnoveldown WanderingInn\n```\n\nIDs can be found through `noveldown --supported-ids`\n\nAppend the `--start` and `--end` options to limit the number of chapters downloaded.\n\nRun `noveldown --help` for more info.\n\n## Library Usage\n```python\nimport noveldown\n\nnoveldown.download("WanderingInn", "./")\n```\n',
    'author': 'Daniel Chen',
    'author_email': 'danielchen04@hotmail.ca',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/potatoeggy/noveldown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
