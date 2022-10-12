# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['flake8_num_positionl_args']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=5.0.4,<6.0.0']

entry_points = \
{'flake8.extension': ['X = flake8_num_positionl_args:NumPositionalArgsChecker']}

setup_kwargs = {
    'name': 'flake8-num-positionl-args',
    'version': '0.0.2',
    'description': 'flake8 plugin for check num of positional args.',
    'long_description': '# Flake8 num of positional args plugin\n\nCheck for num of positional args.\nThis module provides a plugin for `flake8`, the Python code checker.\n\n\n## Installation\n\nYou can install or upgrade `flake8-num-positionl-args` with these commands\n\n```bash\npip install flake8-num-positionl-args\n```\n\n\n## Plugin for Flake8\n\nWhen both `flake8` and `flake8-num-positionl-args` are installed, the plugin is available in `flake8`',
    'author': 'Yasu_umi',
    'author_email': 'yasu.umi.19910101@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
