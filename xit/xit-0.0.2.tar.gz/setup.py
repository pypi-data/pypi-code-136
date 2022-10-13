# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xit',
    'version': '0.0.2',
    'description': 'A namespace for a group of related projects.',
    'long_description': 'Xit Projects!\n=============\n\nThis repository is a namespace for a group of related projects.  Also, it is\nthe base library for this namespace.\n\n.. note::\n\n   The project is currently in development and is not ready for production\n   use.\n\n\nInstall\n-------\n\nDevelopment Stage:\n\n  Check `ADR-4`_ about how to use poetry_ to manage how to evolve projects on\n  development stages.\n\n  *This section is under construction*\n\n.. _adr-4: https://github.com/med-merchise/xit/blob/main/docs/source/adrs/adr-0004-poetry-for-development-stage.rst\n.. _poetry: https://python-poetry.org\n\nProduction Stage:\n\n  *This section is under construction*\n\nAfter installation tasks:\n\n  Each of our projects should have a ``backlog-0001`` document with task to\n  execute after a project is installed.  This document must be located in the\n  ``docs/source/backlog`` directory.\n',
    'author': 'Medardo Antonio Rodriguez',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/med-merchise/xit',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
