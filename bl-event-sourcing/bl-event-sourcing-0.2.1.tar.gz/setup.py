# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bl_event_sourcing']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bl-event-sourcing',
    'version': '0.2.1',
    'description': 'Event sourcing library',
    'long_description': '# An event sourcing library\n',
    'author': 'Tanguy Le Carrour',
    'author_email': 'tanguy@bioneland.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.easter-eggs.org/bioneland/bl-event-sourcing',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
