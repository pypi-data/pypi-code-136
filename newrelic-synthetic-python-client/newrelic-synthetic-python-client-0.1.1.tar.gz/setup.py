# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['newrelic',
 'newrelic.cli',
 'newrelic.nerdgraph',
 'newrelic.nerdgraph.synthetic',
 'newrelic.synthetic',
 'newrelic.utils']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['newrelic = newrelic.cli.entrypoint:main']}

setup_kwargs = {
    'name': 'newrelic-synthetic-python-client',
    'version': '0.1.1',
    'description': 'NewRelic CLI',
    'long_description': None,
    'author': 'Junkai Zhang',
    'author_email': 'junkai.zhang@watchguard.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
