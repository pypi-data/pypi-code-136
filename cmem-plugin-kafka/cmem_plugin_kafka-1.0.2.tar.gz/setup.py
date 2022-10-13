# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cmem_plugin_kafka', 'cmem_plugin_kafka.workflow']

package_data = \
{'': ['*']}

install_requires = \
['cmem-plugin-base>=2.1.0,<3.0.0',
 'confluent-kafka==1.8.2',
 'defusedxml>=0.7.1,<0.8.0']

setup_kwargs = {
    'name': 'cmem-plugin-kafka',
    'version': '1.0.2',
    'description': 'Send messages to Apache Kafka.',
    'long_description': '# cmem-plugin-kafka\n\nSend messages to Apache Kafka.\n\nThis is a plugin for [eccenca](https://eccenca.com) [Corporate Memory](https://documentation.eccenca.com).\n\nYou can install it with the [cmemc](https://eccenca.com/go/cmemc) command line\nclients like this:\n\n```\ncmemc admin workspace python install cmem-plugin-kafka\n```\n\n',
    'author': 'eccenca GmbH',
    'author_email': 'cmempy-developer@eccenca.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eccenca/cmem-plugin-kafka',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
