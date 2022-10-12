# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qottoauth', 'qottoauth.test']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.0.0',
 'cryptography>=37.0.0',
 'eventy>=3.1.0',
 'gql[requests]>=2.0.0',
 'requests>=2.0.0']

setup_kwargs = {
    'name': 'qotto-auth-client',
    'version': '1.0.1a0',
    'description': 'Qotto/QottoAuthClient',
    'long_description': "# Qotto Auth Client\n\nThe python package `qotto-auth-client` is a client for the API `qotto-auth` which will soon be open sourced.\n\nIt allows to manage a scoped permission and authentication system.\n\nMore information coming soon...\n\n## Quickstart\n\nThe `QottoAuthApi` class allows to interact with a `qotto-auth` GraphQL server.\n\n```python\nfrom qottoauth import QottoAuthApi\n\n# qotto-auth server running\napi = QottoAuthApi('http://localhost:3000')\n```\n\nYou can the use (and extends if necessary) the `QottoAuthService` class.\n\n```python\nfrom qottoauth import QottoAuthService\n\nservice = QottoAuthService(api)\n```\n\n### Testing\n\nTo allow offline testing, you can plug a `QottoAuthTestApi` instance to same service.\n\n```python\nfrom qottoauth import QottoAuthTestApi, QottoAuthService\n\ntest_api = QottoAuthTestApi()\nservice = QottoAuthService(test_api)\n```\n\nYou can then test your application, as if a `qotto-auth` server was running.\n\n```python\n# create a user\nuser = service.create_user(name='John Doe', is_superuser=True)\n\n# ...\n``` \n",
    'author': 'Qotto Dev Team',
    'author_email': 'dev@qotto.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
