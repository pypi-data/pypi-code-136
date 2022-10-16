# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nginxproxymanager', 'nginxproxymanager.types']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'nginxproxymanager',
    'version': '0.1.0',
    'description': '',
    'long_description': "# nginxproxymanager-py (`nginxproxymanager` on PyPI)\n\nnginxproxymanager-py is a Python wrapper/scraper for the backend [Nginx Proxy Manager](https://nginxproxymanager.com/) API.\n\nSupports both sync and async calls to each function.\n\nRight now, this package only supports the following functions:\n* Authentication\n* Proxy host management\n* User management\n* Settings management\n* API Status\n\nIn the future, the following features are planned. (Be warned- I'll probably add these as I need them in projects. Who knows how long that will take.)\n* Redirection host management\n* Dead host management\n* Stream Management\n* Access List Management\n* SSL Certificate Management\n",
    'author': 'Parker Wahle',
    'author_email': 'regulad@regulad.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/regulad/nginxproxymanager-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
