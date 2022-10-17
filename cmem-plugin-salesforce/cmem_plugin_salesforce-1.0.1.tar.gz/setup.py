# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cmem_plugin_salesforce',
 'cmem_plugin_salesforce.helper',
 'cmem_plugin_salesforce.workflow']

package_data = \
{'': ['*']}

install_requires = \
['cmem-plugin-base>=2.1.0,<3.0.0',
 'python-soql-parser>=0.1.11,<0.2.0',
 'simple-salesforce>=1.11.6,<2.0.0']

setup_kwargs = {
    'name': 'cmem-plugin-salesforce',
    'version': '1.0.1',
    'description': 'Send or receive data from your organization´s Salesforce account.',
    'long_description': '# cmem-plugin-salesforce\n\nSend or receive data from your organization´s Salesforce account.\n\nThis is a plugin for [eccenca](https://eccenca.com) [Corporate Memory](https://documentation.eccenca.com).\n\nYou can install it with the [cmemc](https://eccenca.com/go/cmemc) command line\nclients like this:\n\n```\ncmemc admin workspace python install cmem-plugin-salesforce\n```\n\n',
    'author': 'Sai Ranga Reddy Nukala',
    'author_email': 'rangareddy.nukala@eccenca.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eccenca/cmem-plugin-salesforce',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
