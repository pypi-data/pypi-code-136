# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['lbfi = src.lbfi:__main__']}

setup_kwargs = {
    'name': 'lbfi',
    'version': '0.3.4',
    'description': 'lbfi stands for Linux Bangla Font Installer. You can avail the fonts for your linux desktop easily with this tool. The main purpose of this tool is to easy installation of different and useful bangla fonts for your linux system.',
    'long_description': '# lbfi\n**lbfi** or **Linux Bangla Font Installer** is a useful tool to help you acquire useful bangla fonts for your linux machine.\nIt is tested or maintained only for Debian based distributions like Ubuntu, Debian, Linux Mint, Deepin etc.\n\n## Installation\n\n### Linux - Debian Based\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install **lbfi**.\n\n```bash\n$ pip3 install lbfi\n```\n\nsuggested command to install\n```bash\n$ pip3 install --upgrade lbfi\n```\n\n## Usage\n\n```bash\n$ lbfi --install yes\n```\n\nIt will install the fonts in your home directory.\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\n### For developers\nMake a fork and clone the source locally. Make sure you have -\n\n- Installed poetry build tool\n- Properly wrote the changes and did test\n- Give a good branch name and commit message\n- Give a Pull request\n\n#### Dependency\n\n- click\n- poetry (Development Dependency)\n- requests\n\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)',
    'author': 'fahadahammed',
    'author_email': 'iamfahadahammed@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
