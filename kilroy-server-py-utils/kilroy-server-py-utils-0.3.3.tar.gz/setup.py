# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_server_py_utils',
 'kilroy_server_py_utils.parameters',
 'kilroy_server_py_utils.resources']

package_data = \
{'': ['*']}

install_requires = \
['fifolock>=0.0,<0.1',
 'jsonschema>=4.7,<5.0',
 'pydantic>=1.9,<2.0',
 'pyhumps>=3.7,<4.0']

setup_kwargs = {
    'name': 'kilroy-server-py-utils',
    'version': '0.3.3',
    'description': 'utilities for kilroy servers in Python 🔧',
    'long_description': '<h1 align="center">kilroy-server-py-utils</h1>\n\n<div align="center">\n\nutilities for kilroy servers in Python 🔧\n\n[![Lint](https://github.com/kilroybot/kilroy-server-py-utils/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-server-py-utils/actions/workflows/lint.yaml)\n[![Tests](https://github.com/kilroybot/kilroy-server-py-utils/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-server-py-utils/actions/workflows/test-multiplatform.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-server-py-utils/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-server-py-utils/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\nTODO\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-server-py-utils\n```\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-server-py-utils',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
