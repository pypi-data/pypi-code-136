# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cmem_plugin_auth', 'cmem_plugin_auth.workflow']

package_data = \
{'': ['*']}

install_requires = \
['cmem-plugin-base>=2.1.0,<3.0.0', 'requests-oauthlib>=1.3.1,<2.0.0']

setup_kwargs = {
    'name': 'cmem-plugin-auth',
    'version': '1.0.0',
    'description': 'Authenticate to services and provide the OAuth2 access token for other tasks.',
    'long_description': '# cmem-plugin-auth\n\nAuthenticate to services and provide the OAuth2 access token for other tasks.\n\nThis is a plugin for [eccenca](https://eccenca.com) [Corporate Memory](https://documentation.eccenca.com).\n\nYou can install it with the [cmemc](https://eccenca.com/go/cmemc) command line\nclients like this:\n\n```\ncmemc admin workspace python install cmem-plugin-auth\n```\n\n',
    'author': 'eccenca GmbH',
    'author_email': 'cmempy-developer@eccenca.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
