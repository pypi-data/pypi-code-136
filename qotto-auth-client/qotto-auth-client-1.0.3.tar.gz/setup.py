# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qottoauth', 'qottoauth.api']

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
    'version': '1.0.3',
    'description': 'Qotto/QottoAuthClient',
    'long_description': '# Qotto Auth Client\n\nThe python package `qotto-auth-client` is a client for the API `qotto-auth` which will soon be open sourced.\n\nIt allows to manage a scoped permission and authentication system.\n\nMore information coming soon...\n\n## Quickstart\n\nThe `QottoAuthApi` class allows to interact with a `qotto-auth` GraphQL server.\n\n```python\nfrom qottoauth import (\n    QottoAuthService,\n    QottoAuthApi,\n    QottoAuthGrapheneApi,\n    QottoAuthTestApi,\n)\n\n# Create a QottoAuthApi instance\napi: QottoAuthApi\nif TEST:\n    # for offline testing\n    api = QottoAuthTestApi()\nelse:\n    # qotto-auth server running\n    api = QottoAuthGrapheneApi(\n        url=QOTTO_AUTH_URL,\n    )\n\n# Create a QottoAuthService instance\nservice = QottoAuthService(\n    api=api,\n)\n\n# Register this application\nservice.register_application(\n    application_name=APPLICATION_NAME,\n    application_description=APPLICATION_DESCRIPTION,\n)\n\n# ...\n```\n\nYou can extend the `QottoAuthService` class to add your own business logic.\n\nIn the current version (1.0.1), `QottoAuthTestApi` does not provide all queries and mutations, so you might need to\nextend the class if you need to test beahviour depending on these queries and mutations.',
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
