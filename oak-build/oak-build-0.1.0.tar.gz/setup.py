# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['oak_build', 'oak_build.tools']

package_data = \
{'': ['*']}

install_requires = \
['colorlog>=6.7.0,<7.0.0', 'rusty-results>=1.1.1,<2.0.0', 'toposort>=1.7,<2.0']

entry_points = \
{'console_scripts': ['oak = oak_build.main:main']}

setup_kwargs = {
    'name': 'oak-build',
    'version': '0.1.0',
    'description': '',
    'long_description': '# oak-buil\n\nA make-like build system written on python\n',
    'author': 'Kirill Sulim',
    'author_email': 'kirillsulim@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
