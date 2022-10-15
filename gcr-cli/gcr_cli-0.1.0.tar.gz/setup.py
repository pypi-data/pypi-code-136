# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gcr_cli']

package_data = \
{'': ['*']}

install_requires = \
['pygithub>=1.56,<2.0', 'rich>=12.6.0,<13.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['gcr = gcr_cli.gcr:app']}

setup_kwargs = {
    'name': 'gcr-cli',
    'version': '0.1.0',
    'description': 'A helper for working with GitHub classroom.',
    'long_description': '# gcr\n\nA helper command for working with GitHub classroom repositories.\n',
    'author': 'James Turk',
    'author_email': 'dev@jamesturk.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
