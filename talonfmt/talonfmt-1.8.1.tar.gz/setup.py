# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['talonfmt']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'doc-printer>=0.13.1,<0.14.0',
 'tree-sitter-talon>=1005.3.1.0,<1006.0.0.0']

extras_require = \
{'test': ['bumpver',
          'pytest>=7.1.2,<8.0.0',
          'pytest-benchmark>=3.4.1,<4.0.0',
          'pytest-golden>=0.2.2,<0.3.0']}

entry_points = \
{'console_scripts': ['talonfmt = talonfmt.cli:cli']}

setup_kwargs = {
    'name': 'talonfmt',
    'version': '1.8.1',
    'description': 'A code formatter for Talon files',
    'long_description': '# talonfmt\n\n![GitHub Workflow Status](https://github.com/wenkokke/talonfmt/actions/workflows/build.yml/badge.svg) ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/wenkokke/talonfmt) ![PyPI](https://img.shields.io/pypi/v/talonfmt)\n\nCode formatter for Talon files.\n',
    'author': 'Wen Kokke',
    'author_email': 'wenkokke@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/wenkokke/talonfmt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9.8,<4.0.0',
}


setup(**setup_kwargs)
