# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tom_alertstreams',
 'tom_alertstreams.alertstreams',
 'tom_alertstreams.management.commands',
 'tom_alertstreams.migrations']

package_data = \
{'': ['*']}

install_requires = \
['gcn-kafka>=0.2,<0.3',
 'hop-client>=0.7,<0.8',
 'psycopg2-binary>=2.9,<3.0',
 'tomtoolkit>=2.10,<3.0']

setup_kwargs = {
    'name': 'tom-alertstreams',
    'version': '0.1.0',
    'description': 'Reusable TOMToolkit app for listening to kafka streams.',
    'long_description': '',
    'author': 'TOM Toolkit Project',
    'author_email': 'tomtoolkit@lco.global',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TOMToolkit/tom-alertstreams',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
