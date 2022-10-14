# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mobilex',
 'mobilex.cache',
 'mobilex.screens',
 'mobilex.sessions',
 'mobilex.sessions.backends',
 'mobilex.utils']

package_data = \
{'': ['*']}

install_requires = \
['phonenumbers>=8.12.51,<9.0.0',
 'redis>=4.3.4,<5.0.0',
 'typing-extensions>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'mobilex',
    'version': '0.0.1',
    'description': 'USSD and SMS exchange framework',
    'long_description': '# Python Mobilex\n\n\n[![PyPi version][pypi-image]][pypi-link]\n[![Supported Python versions][pyversions-image]][pyversions-link]\n[![Build status][ci-image]][ci-link]\n[![Coverage status][codecov-image]][codecov-link]\n\n\nA USSD and SMS exchange framework for Python \n\n\n## Installation\n\nInstall from [PyPi](https://pypi.org/project/mobilex/)\n\n```\npip install mobilex\n```\n\n## Documentation\n\nFull documentation is available [here][docs-link].\n\n\n\n## Production\n\n__This package is still in active development and should not be used in production environment__\n\n\n\n\n[docs-link]: https://davidkyalo.github.io/python-mobilex/\n[pypi-image]: https://img.shields.io/pypi/v/mobilex.svg?color=%233d85c6\n[pypi-link]: https://pypi.python.org/pypi/mobilex\n[pyversions-image]: https://img.shields.io/pypi/pyversions/mobilex.svg\n[pyversions-link]: https://pypi.python.org/pypi/mobilex\n[ci-image]: https://github.com/davidkyalo/python-mobilex/actions/workflows/workflow.yaml/badge.svg?event=push&branch=main\n[ci-link]: https://github.com/davidkyalo/python-mobilex/actions?query=workflow%3ACI%2FCD+event%3Apush+branch%3Amaster\n[codecov-image]: https://codecov.io/gh/davidkyalo/python-mobilex/branch/main/graph/badge.svg\n[codecov-link]: https://codecov.io/gh/davidkyalo/python-mobilex\n\n\nSee this release on GitHub: [v0.0.1](https://github.com/davidkyalo/python-mobilex/releases/tag/0.0.1)\n',
    'author': 'David Kyalo',
    'author_email': 'davidmkyalo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/davidkyalo/python-mobilex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
