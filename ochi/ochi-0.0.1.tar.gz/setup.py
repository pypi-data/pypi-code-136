# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ochi', 'ochi.models']

package_data = \
{'': ['*']}

install_requires = \
['asyncclick>=8.1.3.4,<9.0.0.0',
 'httpx>=0.23.0,<0.24.0',
 'rich>=12.5.1,<13.0.0',
 'textual>=0.1.18,<0.2.0']

entry_points = \
{'console_scripts': ['ochi = ochi.cli:run']}

setup_kwargs = {
    'name': 'ochi',
    'version': '0.0.1',
    'description': 'A simple CLI to read Hacker News in the terminal.',
    'long_description': '# Ochi\n\n![PyPI - License](https://img.shields.io/pypi/l/ochi?style=flat-square)\n\nOchi is a simple CLI to navigate Hacker News in the terminal made with the [Textualize/rich](https://github.com/Textualize/rich) and [pallets/click](https://github.com/pallets/click) packages. In the future, when the awesome [Textualize/textual](https://github.com/Textualize/textual) package launches its documentation I will update this project with a complete TUI.\n\n[![asciicast](https://asciinema.org/a/527446.svg)](https://asciinema.org/a/527446)\n\n## Installation\n`ochi` is hosted on [PyPi](https://pypi.org/project/ochi/). So you can install it with:\n\n```bash\npip install ochi\n```\n\nOr install it from its GitHub repository:\n\n```bash\npip install git+https://github.com/daniarlert/ochi.git\n```\n\n> Note that you may need to run `pip3` instead of `pip` or use `python -m` depending on your setup.\n\n## Usage\n\n### Basic usage\n\nThe most simple way to start using `ochi` is by just running:\n\n```bash\nochi\n```\n\n> To see all the flags `ochi` has available, use the `--help` flag.\n\nBy default, `ochi` fetchs and displays the latest 500 stories on the selected category which in this case is `top` (*topstories*). So a better way to start may be:\n\n```bash\nochi --max 10\n\n# Or\n\nochi -m 10\n```\n\n### Categories\n\nTo get stories from other categories just use the `-c` or `--category` flag:\n\n```bash\nochi --category new\n\n# Or\n\nochi -m 10 -c job\n```\n\n### Order by\n\nYou can order stories by its ID, Score or posted date and reverse its order if you want to:\n\n```bash\nochi -m 10 --order-by date\n\n# Or\n\nochi -m 10 --order-by date --reverse\n```\n\n## Futures\n- Bookmarks/save stories.\n- Configuration for colorschemes and defaults.\n- View post with comments.\n- View user profile.\n',
    'author': 'daniarlert',
    'author_email': 'arlertdaniel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
