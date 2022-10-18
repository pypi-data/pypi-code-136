# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tgcf', 'tgcf.bot', 'tgcf.plugins', 'tgcf.web_ui', 'tgcf.web_ui.pages']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'Telethon==1.25.1',
 'aiohttp>=3.8.3,<4.0.0',
 'cryptg>=0.3.1,<0.4.0',
 'hachoir>=3.1.3,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'pytesseract>=0.3.7,<0.4.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0',
 'streamlit>=1.13.0,<2.0.0',
 'tg-login>=0.0.3,<0.0.4',
 'typer>=0.6.1,<0.7.0',
 'verlat>=0.1.0,<0.2.0',
 'watermark.py>=0.0.3,<0.0.4']

entry_points = \
{'console_scripts': ['tgcf = tgcf.cli:app', 'tgcf-web = tgcf.web_ui.run:main']}

setup_kwargs = {
    'name': 'tgcf',
    'version': '0.3',
    'description': 'The ultimate tool to automate custom telegram message forwarding.',
    'long_description': '<!-- markdownlint-disable -->\n\n<p align="center">\n<a href = "https://github.com/aahnik/tgcf" > <img src = "https://user-images.githubusercontent.com/66209958/115183360-3fa4d500-a0f9-11eb-9c0f-c5ed03a9ae17.png" alt = "tgcf logo"  width=120> </a>\n</p>\n\n<h1 align="center"> tgcf </h1>\n\n<p align="center">\nThe ultimate tool to automate custom telegram message forwarding.\n</p>\n\n<p align="center">\n<a href="https://github.com/aahnik/tgcf/blob/main/LICENSE"><img src="https://img.shields.io/github/license/aahnik/tgcf" alt="GitHub license"></a>\n<a href="https://github.com/aahnik/tgcf/stargazers"><img src="https://img.shields.io/github/stars/aahnik/tgcf?style=social" alt="GitHub stars"></a>\n<a href="https://github.com/aahnik/tgcf/issues"><img src="https://img.shields.io/github/issues/aahnik/tgcf" alt="GitHub issues"></a>\n<img src="https://img.shields.io/pypi/v/tgcf" alt="PyPI">\n<a href="https://twitter.com/intent/tweet?text=Wow:&amp;url=https%3A%2F%2Fgithub.com%2Faahnik%2Ftgcf"><img src="https://img.shields.io/twitter/url?style=social&amp;url=https%3A%2F%2Fgithub.com%2Faahnik%2Ftgcf" alt="Twitter"></a>\n</p>\n<p align="center">\n<a href="https://github.com/aahnik/tgcf/actions/workflows/quality.yml"><img src="https://github.com/aahnik/tgcf/actions/workflows/quality.yml/badge.svg" alt="Code Quality"></a>\n</p>\n<!-- markdownlint-enable -->\n\nLive-syncer, Auto-poster, backup-bot, cloner, chat-forwarder, duplicator, ...\n\nCall it whatever you like! tgcf can fulfill your custom needs.\n\n',
    'author': 'aahnik',
    'author_email': 'daw@aahnik.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aahnik/tgcf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
