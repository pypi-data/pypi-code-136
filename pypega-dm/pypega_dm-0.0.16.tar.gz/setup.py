# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypega_dm']

package_data = \
{'': ['*']}

install_requires = \
['pypega>=0.0.40,<0.0.41']

setup_kwargs = {
    'name': 'pypega-dm',
    'version': '0.0.16',
    'description': 'Python package for orchestrating Pega environments',
    'long_description': '# Pega Deployment Manager (Python)\n\nThis is a simple example package. You can use\n[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)\nto write your content.',
    'author': 'Rob Smart',
    'author_email': 'rob.smart@pega.com',
    'maintainer': 'Rob Smart',
    'maintainer_email': 'rob.smart@pega.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
