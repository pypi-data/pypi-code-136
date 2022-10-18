# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_module_py_shared', 'kilroy_module_py_shared.resources']

package_data = \
{'': ['*']}

install_requires = \
['betterproto>=2.0.0b5,<3.0.0',
 'jsonschema>=4.7,<5.0',
 'pydantic>=1.9,<2.0',
 'pyhumps>=3.7,<4.0']

setup_kwargs = {
    'name': 'kilroy-module-py-shared',
    'version': '0.6.1',
    'description': 'shared code for kilroy module SDKs in Python 🤝',
    'long_description': '<h1 align="center">kilroy-module-py-shared</h1>\n\n<div align="center">\n\nshared code for kilroy module SDKs in Python 🤝\n\n[![Lint](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/lint.yaml)\n[![Tests](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/test-multiplatform.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\nTODO\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-module-py-shared\n```\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-module-py-shared',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
