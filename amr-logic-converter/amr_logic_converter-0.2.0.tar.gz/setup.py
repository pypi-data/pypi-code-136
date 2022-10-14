# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amr_logic_converter']

package_data = \
{'': ['*']}

install_requires = \
['Penman>=1.2.2,<2.0.0', 'nltk>=3.7,<4.0', 'typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'amr-logic-converter',
    'version': '0.2.0',
    'description': 'Convert Abstract Meaning Representation (AMR) into first-order logic',
    'long_description': 'None',
    'author': 'David Chanin',
    'author_email': 'chanindav@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
