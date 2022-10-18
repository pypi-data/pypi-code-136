# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_module_pytorch_py_sdk',
 'kilroy_module_pytorch_py_sdk.generator',
 'kilroy_module_pytorch_py_sdk.modules',
 'kilroy_module_pytorch_py_sdk.optimizers',
 'kilroy_module_pytorch_py_sdk.resources',
 'kilroy_module_pytorch_py_sdk.samplers',
 'kilroy_module_pytorch_py_sdk.schedulers']

package_data = \
{'': ['*']}

install_requires = \
['kilroy-module-server-py-sdk>=0.9,<0.10', 'numpy>=1,<2', 'torch>=1,<2']

setup_kwargs = {
    'name': 'kilroy-module-pytorch-py-sdk',
    'version': '0.7.1',
    'description': 'SDK for kilroy modules using PyTorch 🧰',
    'long_description': '<h1 align="center">kilroy-module-pytorch-py-sdk</h1>\n\n<div align="center">\n\nSDK for kilroy modules using PyTorch 🧰\n\n[![Lint](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/lint.yaml)\n[![Tests](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/test-multiplatform.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-module-pytorch-py-sdk\n```\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-module-pytorch-py-sdk',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
