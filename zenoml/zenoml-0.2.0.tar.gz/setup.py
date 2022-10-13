# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zeno', 'zeno.mirror']

package_data = \
{'': ['*'],
 'zeno': ['frontend/*', 'frontend/build/*', 'frontend/build/assets/*']}

install_requires = \
['fastapi>=0.75,<0.86',
 'pandas>=1.4.0,<2.0.0',
 'pyarrow>=9.0.0,<10.0.0',
 'requests>=2.28.1,<3.0.0',
 'scikit-learn>=1.1.2,<2.0.0',
 'tomli>=2.0.1,<3.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'types-setuptools>=65.4.0,<66.0.0',
 'uvicorn>=0.17.5,<0.19.0',
 'websockets>=10.2,<11.0']

entry_points = \
{'console_scripts': ['zeno = zeno.runner:main']}

setup_kwargs = {
    'name': 'zenoml',
    'version': '0.2.0',
    'description': 'Interactive Evaluation Framework for Machine Learning',
    'long_description': '<img src="./frontend/public/zeno.png" width="400px"/>\n\n[![PyPI version](https://badge.fury.io/py/zenoml.svg)](https://badge.fury.io/py/zenoml)\n![Github Actions CI tests](https://github.com/zeno-ml/zeno/actions/workflows/test.yml/badge.svg)\n![Github Actions Docs build](https://github.com/zeno-ml/zenoml.com/actions/workflows/docs.yml/badge.svg)\n[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![Join the chat at https://gitter.im/zeno-ml-eval/community](https://badges.gitter.im/zeno-ml-eval/community.svg)](https://gitter.im/zeno-ml-eval/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n\nZeno is a general-purpose framework for evaluating machine learning models.\nIt combines a **Python API** with an **interactive UI** to allow users to discover, explore, and analyze the performance of their models across diverse use cases.\nZeno can be used for any data type or task with _modular views_ for everything from object detection to audio transcription.\n\n## Getting Started\n\nCheck out the quickstart tutorial and API reference to get started with Zeno:\n\n- [Introduction](http://zenoml.com/docs/intro/) - Learn more about Zeno.\n- [Getting Started](http://zenoml.com/docs/intro/get_started) - Setup Zeno with your own data and models.\n- [CIFAR-10 Example](http://zenoml.com/docs/intro/cifar) - Learn how to use Zeno with a CIFAR-10 classification example.\n- [Documentation & API](http://zenoml.com/docs/intro/) - Full documentation and API reference.\n',
    'author': 'Ángel Alexander Cabrera',
    'author_email': 'alex.cabrera@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://zenoml.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
