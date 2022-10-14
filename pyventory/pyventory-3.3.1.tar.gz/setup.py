# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyventory']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.1.0,<23.0.0', 'ordered-set>=4.0.2,<5.0.0']

setup_kwargs = {
    'name': 'pyventory',
    'version': '3.3.1',
    'description': 'Ansible Inventory implementation that uses Python syntax',
    'long_description': "[![CI Status](https://github.com/lig/pyventory/workflows/CI/badge.svg)](https://github.com/lig/pyventory/actions)\n\n# Pyventory\n\nAnsible Inventory implementation that uses Python syntax\n\n## Install\n\n```shell\npip3 install pyventory\n```\n\n## Features\n\n* Modular inventory.\n* Assests inheritance using Python classes.\n* Support for multiple inheritance.\n* Support for mixins.\n* Support for vars templating using [Python string formatting](https://docs.python.org/3/library/string.html#format-specification-mini-language).\n* Python 3 (>=3.6) support.\n* Python 2 is not supported.\n\n## Usage\n\nCreate `hosts.py` and make it executable.\n\nA short example of the `hosts.py` contents:\n\n```python\n#!/usr/bin/env python3\nfrom pyventory import Asset, ansible_inventory\n\nclass All(Asset):\n    run_tests = False\n    use_redis = False\n    redis_host = 'localhost'\n    minify = False\n    version = 'develop'\n\nclass Staging(All):\n    run_tests = True\n\nstaging = Staging()\n\nansible_inventory(locals())\n```\n\nConsider a [more complex example](tests/example) which passes the following [json output](tests/example.json) to Ansible.\n\nRun Ansible playbook with the `-i hosts.py` key:\n\n```shell\nansible-playbook -i hosts.py site.yml\n```\n\nNotice that you need to have your inventory package in `PYTHONPATH`.\n",
    'author': 'Serge Matveenko',
    'author_email': 'lig@countzero.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lig/pyventory',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
