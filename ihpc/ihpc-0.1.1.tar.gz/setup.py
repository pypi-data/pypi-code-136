# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hpc',
 'hpc.base',
 'hpc.impl',
 'hpc.mngr',
 'hpc.mngr.lsf',
 'hpc.mngr.lsf.extra']

package_data = \
{'': ['*']}

install_requires = \
['paramiko>=2.11.0,<3.0.0', 'typing-extensions>=4.3.0,<5.0.0']

setup_kwargs = {
    'name': 'ihpc',
    'version': '0.1.1',
    'description': 'Designed to Operate HPC Servers',
    'long_description': '<!-- Template from https://github.com/othneildrew/Best-README-Template -->\n<div id="top"></div>\n\n\n\n<!-- PROJECT LOGO -->\n<br />\n<div align="center">\n  <a href="https://github.com/iydon/hpc">\n    🔵⬜⬜⬜🟦<br />\n    🟦🟦⬜🟦🟦<br />\n    🟦⬜🟦⬜🟦<br />\n    🟦🟦⬜🟦🟦<br />\n    🟦⬜⬜⬜🟦<br />\n  </a>\n\n  <h3 align="center">iHPC</h3>\n\n  <p align="center">\n    Designed to Operate HPC Servers\n    <br />\n    <a href="https://github.com/iydon/hpc"><strong>Explore the docs »</strong></a>\n    <br />\n    <br />\n    <a href="https://github.com/iydon/hpc">View Demo</a>\n    ·\n    <a href="https://github.com/iydon/hpc/issues">Report Bug</a>\n    ·\n    <a href="https://github.com/iydon/hpc/issues">Request Feature</a>\n  </p>\n</div>\n',
    'author': 'Iydon Liang',
    'author_email': 'liangiydon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/iydon/hpc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
