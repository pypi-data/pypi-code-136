# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_face_server_py_sdk', 'kilroy_face_server_py_sdk.resources']

package_data = \
{'': ['*']}

install_requires = \
['kilroy-face-py-shared>=0.5,<0.6', 'kilroy-server-py-utils>=0.3,<0.4']

setup_kwargs = {
    'name': 'kilroy-face-server-py-sdk',
    'version': '0.8.1',
    'description': 'SDK for kilroy face servers in Python 🧰',
    'long_description': '<h1 align="center">kilroy-face-server-py-sdk</h1>\n\n<div align="center">\n\nSDK for kilroy face servers in Python 🧰\n\n[![Lint](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/lint.yaml)\n[![Tests](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/test-multiplatform.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-face-server-py-sdk\n```\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-face-server-py-sdk',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
