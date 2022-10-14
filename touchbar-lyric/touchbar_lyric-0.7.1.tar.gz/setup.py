# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['touchbar_lyric', 'touchbar_lyric.service', 'touchbar_lyric.utility']

package_data = \
{'': ['*']}

install_requires = \
['applescript>=2021.2.9,<2022.0.0',
 'coverage>=5.5,<6.0',
 'diskcache>=5.2.1,<6.0.0',
 'hanziconv>=0.3.2,<0.4.0',
 'loguru>=0.5.3,<0.6.0',
 'pyaes>=1.6.1,<2.0.0',
 'pycrypto>=2.6.1,<3.0.0',
 'qqmusic-api>=0.1,<0.2',
 'regex>=2021.3.17,<2022.0.0',
 'strsimpy>=0.2.0,<0.3.0',
 'typer>=0.3.2,<0.4.0']

setup_kwargs = {
    'name': 'touchbar-lyric',
    'version': '0.7.1',
    'description': 'Display lyrics on your touchbar with BTT',
    'long_description': '<center><h1>Synced Lyric on TouchBar</h1></center>\n\n[![Codacy Badge](https://api.codacy.com/project/badge/Grade/77de523131f9441997db18c608b3c54e)](https://app.codacy.com/manual/mouchenghao/touchbar-lyric?utm_source=github.com&utm_medium=referral&utm_content=ChenghaoMou/touchbar-lyric&utm_campaign=Badge_Grade_Dashboard) [![Build Status](https://travis-ci.com/ChenghaoMou/touchbar-lyric.svg?branch=master)](https://travis-ci.com/ChenghaoMou/touchbar-lyric) [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/aadeca6117a14aa6b655e21d5bbc09ea)](https://www.codacy.com/manual/mouchenghao/touchbar-lyric?utm_source=github.com&utm_medium=referral&utm_content=ChenghaoMou/touchbar-lyric&utm_campaign=Badge_Coverage) [![PyPI version](https://badge.fury.io/py/touchbar-lyric.svg)](https://badge.fury.io/py/touchbar-lyric)\n\nShow synced lyric in the touch-bar with BetterTouchTool and NetEase/QQ Music APIs. Based on the idea of [Kashi](https://community.folivora.ai/t/kashi-show-current-song-lyrics-on-touch-bar-spotify-itunes-youtube/6301).\n\n![Preview](./lyric_chinese.png)\n![Preview](./lyric_english.png)\n\n## Features\n\n-   **Synced lyrics** from QQ Music and NetEase Music APIs;\n-   Support **Spotify** (Recommended) & **Music** (Only songs in your playlists);\n-   Support for **English/Spanish/Chinese(Simplified/Traditional)/Japanese** and more;\n\n## Instruction\n\n**If you are not familiar with command line, python ecosystem or having problems understanding this tutorial, find a friend to help you. Issues/DMs are not actively monitored for this project.**\n\n### 1. Installation\n```shell\npip3 install touchbar_lyric --upgrade\n```\n\n### 2. Configuration in BetterTouchTool\n\nSame as Kashi:\n\n1.  Copy&paste the content in `lyric.json` in _Meun Bar > Touch Bar_;\n2.  Change the python path `$PYTHONPATH` to your own python path in the script area;\n\n```shell\n$PYTHONPATH -m touchbar_lyric --app Music\n```\n\nor use Spotify(default)\n\n```shell\n$PYTHONPATH -m touchbar_lyric --app Spotify\n```\n\nShow Traditional Chinese lyrics\n\n```shell\n$PYTHONPATH -m touchbar_lyric --app Spotify --traditional\n```\n\n**Be careful with typing double hyphens in BTT. It automatically change it to an em slash. Use copy & paste instead!**',
    'author': 'Chenghao Mou',
    'author_email': 'mouchenghao@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
