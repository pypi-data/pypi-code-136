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
    'version': '0.0.1',
    'description': 'flake8 plugin for check num of positional args.',
    'long_description': 'None',
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
