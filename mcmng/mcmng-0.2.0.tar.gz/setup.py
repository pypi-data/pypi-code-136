# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mcmng']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'mcstatus>=9.4.2,<10.0.0']

setup_kwargs = {
    'name': 'mcmng',
    'version': '0.2.0',
    'description': 'Command line based minecraft server manager for individual admins.',
    'long_description': '# mcmng\n\nCommand line based [minecraft](https://www.minecraft.net/en-us) server manager for individual admins.\n\n## Installation\n\n- Install [python 3.10](https://www.python.org/downloads/) or higher\n- `pip install mcmng`\n\n## Development\n\n- Install [python 3.10](https://www.python.org/downloads/) or higher\n- Install [poetry](https://python-poetry.org/)\n- `poetry install`\n',
    'author': 'Technomunk',
    'author_email': 'thegriffones@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/technomunk/mcmng',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
