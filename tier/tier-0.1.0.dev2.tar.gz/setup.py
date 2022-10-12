# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tier',
 'tier.cli',
 'tier.cli.subcommands',
 'tier.internal',
 'tier.internal.build_systems',
 'tier.internal.configs',
 'tier.internal.git',
 'tier.internal.versioning']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['tier = tier.main:main']}

setup_kwargs = {
    'name': 'tier',
    'version': '0.1.0.dev2',
    'description': 'Python Versioning CLI',
    'long_description': '# tier\nPython Versioning CLI\n',
    'author': 'Josh Wycuff',
    'author_email': 'Joshua.Wycuff@turner.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
