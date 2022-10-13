# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baseblock']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==6.0', 'cryptography==37.0.4', 'unicodedata2']

setup_kwargs = {
    'name': 'baseblock',
    'version': '0.1.30',
    'description': 'Base Block of Common Enterprise Python Utilities',
    'long_description': '# Base Block (baseblock)\n\nBase Block of Common Enterprise Python Utilities\n',
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/climate-bot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
