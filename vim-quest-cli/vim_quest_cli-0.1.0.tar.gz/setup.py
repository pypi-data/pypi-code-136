# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vim_quest_cli', 'vim_quest_cli.executors', 'vim_quest_cli.interfaces']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vim-quest-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': '# VimQuestCLI\n\nTODO : \n\n- Have vim as executor. So I can compare for tests.\n- Have a context that is not a copy but modify itself (for speed).\n- Have a bunch of hooks, and use them to have game modes.\n- Have a command to choose between game modes.\n- See how neovim is made so I can use the same architecture.\n- Syntax highlighting for python.\n- Maybe have syntax highliting for game modes too ?\n- Solve the ANSI speed.\n- Activate the UTF-8, see how I can activate it.\n- Create docker images for website and terminal.\n- \n\nSPLIT projects :\n\n- VimQuestCLI for python cli version.\n- Bundle to have python bundle pypy project.\n- Using bundle and transform it into javascript => deploy onto mpm.\n- Javascript website to deploy.\n\nBUG CORRECTION :\n- Clean codebase.\n- ANSI is blinking.\n- Image location is not working.\n- Size of the terminal is not used.\n- Unicode block behavior is inconsistent.\n  - Maybe having replacement for unicode that include colors.\n',
    'author': 'Mickael Kerbrat',
    'author_email': 'mickael.kerbrat@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
