# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ascii_art', 'ascii_art.toolchain']

package_data = \
{'': ['*'], 'ascii_art': ['lib/*']}

setup_kwargs = {
    'name': 'sleepys-ascii-art-printer',
    'version': '0.1.0',
    'description': 'An ascii art library and output tool for the command line.',
    'long_description': '\ufeff# **ASCII_art**\n*A collection of art assets generated from ascii text*\n\n<br />\n\n### Welcome to ASCII_art!\n<hr>\n\nThis repository hosts an ever growing bucket of ascii art entries. This collection excludes unicode entries, but all creators are welcome to use and contribute!\n\n<br />\n\n### Table of Contents 📖\n<hr>\n\n  - [Welcome](#welcome-to-ascii_art)\n  - [**Get Started**](#get-started-)\n  - [Usage](#usage-)\n  - [Contribute](#Contribute-)\n  - [Acknowledgements](#acknowledgements-)\n  - [License/Stats/Author](#license-stats-author-)\n\n<br />\n\n### Get Started 🚀\n<hr>\n\nNot much to say, just go ahead and copy paste the text for your own use or amusement!\n\n<br />\n\n### Usage ⚙\n<hr>\n\nGreat for school work flaire, or fun personal cli programs. Since this is a dumping ground of art for anyone and everyone though, please don\'t try to claim other people\'s work as your own.\n\n<br />\n\n### Contribute 🤝\n<hr>\n\nI will look through pull requests consistantly, and will reject any if they have already been done, are deemed *nsfw*, contain offensive language, or use *unicode* characters. Other than that, feel free to `fork`, `commit` your own art entry, and submit a `pull request`.\n\n<br />\n\n### Acknowledgements 💙\n<hr>\n\nWill update this section well after `hacktoberfest2020`.\n\n<br />\n\n### License, Stats, Author 📜\n<hr>\n\n<img align="right" alt="example image tag" src="https://i.imgur.com/jtNwEWu.png" width="200" />\n\n<!-- badge cluster -->\n\n![GitHub](https://img.shields.io/github/license/anthonybench/ASCII_art) \n\n<!-- / -->\nSee [License](https://opensource.org/licenses/MIT) for the full license text.\n\nThis repository was authored by *Isaac Yep*.\n\n[Back to Table of Contents](#table-of-contents-)\n',
    'author': 'iyep',
    'author_email': 'iyep@halcyon.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anthonybench/ASCII_art',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
