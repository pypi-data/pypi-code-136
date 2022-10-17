# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cryptocom', 'cryptocom.exchange']

package_data = \
{'': ['*']}

install_requires = \
['aiolimiter>=1.0.0,<2.0.0',
 'async-timeout>=4.0.2,<5.0.0',
 'cached-property>=1.5.2,<2.0.0',
 'httpx>=0.23.0,<0.24.0',
 'websockets>=10.3,<11.0']

setup_kwargs = {
    'name': 'cryptocom-exchange',
    'version': '0.12.0',
    'description': 'Python 3.7+ async library for crypto.com/exchange API using httpx and websockets',
    'long_description': '# Python 3.7+ async library for crypto.com/exchange API using httpx and websockets\n\n[![Docs Build Status](https://readthedocs.org/projects/cryptocom-exchange/badge/?version=latest&style=flat)](https://readthedocs.org/projects/cryptocom-exchange)\n![Test workflow](https://github.com/goincrypto/cryptocom-exchange/actions/workflows/test_release.yml/badge.svg)\n[![Maintainability](https://api.codeclimate.com/v1/badges/8d7ffdae54f3c6e86b5a/maintainability)](https://codeclimate.com/github/goincrypto/cryptocom-exchange/maintainability)\n[![Test Coverage](https://api.codeclimate.com/v1/badges/8d7ffdae54f3c6e86b5a/test_coverage)](https://codeclimate.com/github/goincrypto/cryptocom-exchange/test_coverage)\n[![PyPI implementation](https://img.shields.io/pypi/implementation/cryptocom-exchange.svg)](https://pypi.python.org/pypi/cryptocom-exchange/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/cryptocom-exchange.svg)](https://pypi.python.org/pypi/cryptocom-exchange/)\n[![PyPI license](https://img.shields.io/pypi/l/cryptocom-exchange.svg)](https://pypi.python.org/pypi/cryptocom-exchange/)\n[![PyPI version fury.io](https://badge.fury.io/py/cryptocom-exchange.svg)](https://pypi.python.org/pypi/cryptocom-exchange/)\n[![PyPI download month](https://img.shields.io/pypi/dm/cryptocom-exchange.svg)](https://pypi.python.org/pypi/cryptocom-exchange/)\n[![Gitter](https://badges.gitter.im/goincrypto/cryptocom-exchange.svg)](https://gitter.im/goincrypto/cryptocom-exchange?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)\n\nDocumentation: [https://cryptocom-exchange.rtfd.io](https://cryptocom-exchange.rtfd.io)\n\nExchange original API docs: [https://exchange-docs.crypto.com](https://exchange-docs.crypto.com)\n\n### Description\n\n`pip install cryptocom-exchange` or `poetry add cryptocom-exchange`\n\n- provides all methods to access crypto.com/exchange API (except for websockets temporary)\n- full test coverage on real exchange with real money\n- simple async methods with custom retries and timeouts\n\n**Please do not use secret keys, they used only for test purposes**\n',
    'author': 'Morty Space',
    'author_email': 'morty.space@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
