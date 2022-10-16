# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_storages']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.6.1,<4.0.0']

setup_kwargs = {
    'name': 'async-storages',
    'version': '0.1.0',
    'description': 'Async file storages for Python',
    'long_description': '# Async storages\n\nAsync file storages for Python\n\n![PyPI](https://img.shields.io/pypi/v/async_storages)\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alex-oleshkevich/async_storages/Lint)\n![GitHub](https://img.shields.io/github/license/alex-oleshkevich/async_storages)\n![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/async_storages)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/async_storages)\n![GitHub Release Date](https://img.shields.io/github/release-date/alex-oleshkevich/async_storages)\n\n## Installation\n\nInstall `async_storages` using PIP or poetry:\n\n```bash\npip install async_storages\n# or\npoetry add async_storages\n```\n\n## Features\n\n- simple abstraction over local filesystem, s3, or memory driver\n- S3 integration\n- Spooled In-memory driver for unit tests\n\n## Quick start\n\nSee example application in [examples/](examples/) directory of this repository.\n',
    'author': 'Alex Oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alex-oleshkevich/async_storages',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.0,<4.0.0',
}


setup(**setup_kwargs)
