# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['swarm_pretalx']

package_data = \
{'': ['*'],
 'swarm_pretalx': ['locale/de_DE/LC_MESSAGES/*',
                   'locale/fr_FR/LC_MESSAGES/*',
                   'static/swarm_pretalx/*',
                   'templates/swarm_pretalx/*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'swarm-pretalx',
    'version': '0.1.5',
    'description': 'A Pretalx plugin that exports the agenda on Swarm',
    'long_description': None,
    'author': 'cmdctrlesc',
    'author_email': 'alanxyz210@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
