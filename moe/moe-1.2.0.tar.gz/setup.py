# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moe',
 'moe.library',
 'moe.plugins',
 'moe.plugins.add',
 'moe.plugins.duplicate',
 'moe.plugins.edit',
 'moe.plugins.moe_import',
 'moe.plugins.move',
 'moe.plugins.musicbrainz',
 'moe.plugins.read',
 'moe.plugins.remove',
 'moe.plugins.sync',
 'moe.util',
 'moe.util.cli',
 'moe.util.core']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.15,<2.0.0',
 'Unidecode>=1.2.0,<2.0.0',
 'alembic>=1.4.2,<2.0.0',
 'dynaconf>=3.1.4,<4.0.0',
 'mediafile>=0.9.0,<0.10.0',
 'musicbrainzngs>=0.7.1,<0.8.0',
 'pluggy>=0.13.1,<0.14.0',
 'pyyaml>=5.3.1,<6.0.0',
 'questionary>=1.9.0,<2.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['moe = moe.cli:main']}

setup_kwargs = {
    'name': 'moe',
    'version': '1.2.0',
    'description': 'The ultimate tool for managing your music library.',
    'long_description': "###############\nWelcome to Moe!\n###############\nMoe is our resident Music-Organizer-Extraordinaire who's sole purpose is to give you full control over your music library by streamlining the process between downloading/ripping music to your filesystem and listening to it with your favorite music player.\n\nIn short, Moe maintains a database of your music library that can be updated with various metadata sources, queried, edited, etc. through either an API or command-line interface. All of these features, and more, are made available by a highly extensible plugin ecosystem.\n\nIf you want to learn more, check out the `Getting Started <https://mrmoe.readthedocs.io/en/latest/getting_started.html>`_ docs.\n",
    'author': 'Jacob Pavlock',
    'author_email': 'jtpavlock@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MoeMusic/Moe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
