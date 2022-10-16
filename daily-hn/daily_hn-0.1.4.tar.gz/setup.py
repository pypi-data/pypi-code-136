# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['daily_hn']
install_requires = \
['beautifulsoup4>=4.10.0,<5.0.0', 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['daily_hn = daily_hn:main']}

setup_kwargs = {
    'name': 'daily-hn',
    'version': '0.1.4',
    'description': 'A command line tool for displaying and opening links to the current best stories from news.ycombinator.com (Hacker News)',
    'long_description': '# <img alt="daily_hn" src="https://github.com/Rolv-Apneseth/daily_hn/blob/1f191fe1cb9f81892794d2d0b7d0173923df7da9/assets/daily_hn.png" width="400px"/>\n\n![Tests](https://github.com/Rolv-Apneseth/daily_hn/actions/workflows/tests.yml/badge.svg)\n![Linux](https://img.shields.io/badge/-Linux-grey?logo=linux)\n![OSX](https://img.shields.io/badge/-OSX-black?logo=apple)\n![Python](https://img.shields.io/badge/Python-v3.9%5E-green?logo=python)\n![Version](https://img.shields.io/github/v/tag/rolv-apneseth/daily_hn?label=version)\n[![PyPi](https://img.shields.io/pypi/v/daily_hn?label=pypi)](https://pypi.org/project/daily-hn/)\n![Black](https://img.shields.io/badge/code%20style-black-000000.svg)\n\n![daily_hn demo](https://user-images.githubusercontent.com/69486699/161394178-a6030503-f481-481e-999b-b027ea4bba96.png)\n\n\n## Description\n\nA command line tool for displaying and opening links to the current best stories from [news.ycombinator.com](https://news.ycombinator.com) (Hacker News).\n\nYou can find the best stories page this program parses [here!](https://news.ycombinator.com/best)\n\n## Dependencies\n\n- [Python](https://www.python.org/downloads/) v3.9+\n- [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/)\n- [Requests](https://pypi.org/project/requests/)\n- If you are on Windows: [windows-curses](https://pypi.org/project/windows-curses/) (Python)\n\n## Installation\n\n### Pypi\n\n> Install or update to latest version\n\n```bash\npython3 -m pip install daily-hn --upgrade\n```\n\n> If you are on Windows, also install `windows-curses`\n\n```bash\npip install windows-curses daily-hn --upgrade\n```\n\n## Manual Installation\n\n> Make sure you have `python3` and `git` installed\n\n> Install Python requirements\n\n```bash\npython3 -m pip install requests beautifulsoup4\n```\n\n> Install\n\n```bash\ngit clone https://github.com/Rolv-Apneseth/daily_hn.git\ncd daily_hn\nsudo make install\n```\n\n> Uninstall\n\n```bash\nsudo make uninstall\n```\n\n## Usage\n\nAfter installation, the program can be launched from your terminal by running `daily_hn` (on Windows, use `python -m daily_hn` unless you added the `site-packages` folder to your `Path`).\n\nWith the `curses` UI (default), you can open up stories (uses the default browser) by pressing the shortcut key to the left of that story. Navigate up and down using either `j` and `k` for fine movements or `{` and `}` for bigger jumps. To quit, press `q`.\n\nTo simply print out a list of stories (links being clickable depends on your terminal emulator), provide the `-p` flag i.e. `daily_hn -p`.\n\n## License\n\n[MIT](https://github.com/Rolv-Apneseth/daily_hn/blob/2d40839e6e625c55075430bde5fef337a08e89ba/LICENSE)\n',
    'author': 'Rolv-Apneseth',
    'author_email': 'rolv.apneseth@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Rolv-Apneseth/daily_hn/',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0.0',
}


setup(**setup_kwargs)
