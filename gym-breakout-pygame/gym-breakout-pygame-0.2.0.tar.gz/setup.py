# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gym_breakout_pygame', 'gym_breakout_pygame.wrappers']

package_data = \
{'': ['*']}

install_requires = \
['gym>=0.26.2,<0.27.0', 'numpy>=1.23.3,<2.0.0', 'pygame>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'gym-breakout-pygame',
    'version': '0.2.0',
    'description': 'Gym Breakout environment using Pygame.',
    'long_description': '<h1 align="center">\n  <b>gym-breakout-pygame</b>\n</h1>\n\n<p align="center">\n  <a href="https://pypi.org/project/gym-breakout-pygame">\n    <img alt="PyPI" src="https://img.shields.io/pypi/v/gym-breakout-pygame">\n  </a>\n  <a href="https://pypi.org/project/gym-breakout-pygame">\n    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/gym-breakout-pygame" />\n  </a>\n  <a href="">\n    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/gym-breakout-pygame" />\n  </a>\n  <a href="">\n    <img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/gym-breakout-pygame">\n  </a>\n  <a href="">\n    <img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/gym-breakout-pygame">\n  </a>\n  <a href="https://github.com/whitemech/gym-breakout-pygame/blob/master/LICENSE">\n    <img alt="GitHub" src="https://img.shields.io/github/license/whitemech/gym-breakout-pygame">\n  </a>\n</p>\n<p align="center">\n  <a href="">\n    <img alt="test" src="https://github.com/whitemech/gym-breakout-pygame/workflows/test/badge.svg">\n  </a>\n  <a href="">\n    <img alt="lint" src="https://github.com/whitemech/gym-breakout-pygame/workflows/lint/badge.svg">\n  </a>\n  <a href="">\n    <img alt="docs" src="https://github.com/whitemech/gym-breakout-pygame/workflows/docs/badge.svg">\n  </a>\n  <a href="https://codecov.io/gh/whitemech/gym-breakout-pygame">\n    <img alt="codecov" src="https://codecov.io/gh/whitemech/gym-breakout-pygame/branch/master/graph/badge.svg?token=FG3ATGP5P5">\n  </a>\n</p>\n\n\nGym Breakout environment using Pygame.\n\n## Install\n\nInstall with `pip`:\n\n    pip3 install gym_breakout_pygame\n    \nOr, install from source:\n\n    git clone https://github.com/whitemech/gym-breakout-pygame.git\n    cd gym-breakout-pygame\n    pip install .\n\n\n## Development\n\n- clone the repo:\n\n        git clone https://github.com/whitemech/gym-breakout-pygame.git\n        cd gym-breakout-pygame\n    \n- Create/activate the virtual environment (using Poetry):\n\n        poetry shell\n        poetry install\n    \n- Run a short demo:\n\n        python gym_breakout_pygame --random --record\n      \nCheck for an `.mp4` file in `videos/`. You should get:\n\n<p align="center">\n  <img width="260" height="480" src="https://raw.githubusercontent.com/whitemech/gym-breakout-pygame/develop/docs/breakout-example.gif"></p>\n\n\n- Enable fire:\n\n        python gym_breakout_pygame --fire\n\n<p align="center">\n  <img width="260" height="480" src="https://raw.githubusercontent.com/whitemech/gym-breakout-pygame/develop/docs/breakout-example-fire.gif">\n</p>\n\n\n## Tests\n\nTo run tests: `tox`\n\nTo run only the code tests: `tox -e py3.10`\n\nTo run only the linters: \n- `tox -e flake8`\n- `tox -e mypy`\n- `tox -e black-check`\n- `tox -e isort-check`\n\nPlease look at the `tox.ini` file for the full list of supported commands. \n\n## Docs\n\nTo build the docs: `mkdocs build`\n\nTo view documentation in a browser: `mkdocs serve`\nand then go to [http://localhost:8000](http://localhost:8000)\n\n## License\n\ngym-breakout-pygame is released under the GNU General Public License v3.0 or later (GPLv3+).\n\nCopyright 2019-2022 Marco Favorito, Luca Iocchi\n\n## Authors\n\n- [Marco Favorito](https://marcofavorito.me/)\n- [Luca Iocchi](https://github.com/iocchi)\n\nThe code is largely inspired by [RLGames](https://github.com/iocchi/RLGames.git)\n\n',
    'author': 'Marco Favorito',
    'author_email': 'favorito@diag.uniroma1.it',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://whitemech.github.io/gym-breakout-pygame',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
