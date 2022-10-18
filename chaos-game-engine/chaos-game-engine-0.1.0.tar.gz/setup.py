# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chaos_game', 'chaos_game.toolchain']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'chaos-game-engine',
    'version': '0.1.0',
    'description': "A parameterized exploration of the 'chaos game'.",
    'long_description': '# **Chaos Game**\n*An exploration of procedural fractal generation.*\n\n<br />\n\n## **Welcome to REPO!**\nHello world.\n\n<br />\n\n### **Table of Contents** 📖\n<hr>\n\n  - [Welcome](#welcome-to-REPO)\n  - [**Get Started**](#get-started-)\n  - [Usage](#usage-)\n  - [Technologies](#technologies-)\n  - [Contribute](#Contribute-)\n  - [Acknowledgements](#acknowledgements-)\n  - [License/Stats/Author](#license-stats-author-)\n\n<br />\n\n## **Get Started 🚀**\n<hr>\n\nHello world.\n\n<br />\n\n## **Usage ⚙**\n<hr>\n\nHello world.\n\n<br />\n\n## **Technologies 🧰**\n<hr>\n\n  - [flip.js](https://google.com)\n  - [flop.js](https://google.com)\n  - [flap.js](https://google.com)\n\n<br />\n\n## **Contribute 🤝**\n<hr>\n\nHello world.\n\n<br />\n\n## **Acknowledgements 💙**\n<hr>\n\nA special thanks to professor *Jim Pantaleone* at University of Alaska Anchorage for introducing this to me in his *Chaos & Nonlinear Dynamics* course amidst my physics degree. A memorably brilliant educator who gave mathematical physics attitude.\n\nRead more about "*The Chaos Game*" [here](https://en.wikipedia.org/wiki/Chaos_game).\n\n<br />\n\n## **License, Stats, Author 📜**\n<hr>\n\n<img align="right" alt="example image tag" src="https://i.imgur.com/jtNwEWu.png" width="200" />\n\n<!-- badge cluster -->\n\n[SHIELD](https://shields.io/)\n\n<!-- / -->\nSee [License](https://google.com) for the full license text.\n\nThis repository was authored by *Isaac Yep*.\n\n[Back to Table of Contents](#table-of-contents-)',
    'author': 'anthonybench',
    'author_email': 'anthonybenchyep@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anthonybench/chaos-game',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
