# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nagata']

package_data = \
{'': ['*']}

install_requires = \
['amos>=0.1.5,<0.2.0', 'miller>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'nagata',
    'version': '0.1.1',
    'description': 'python file management using a common, intuitive syntax',
    'long_description': '\n\nnagata is highly internally documented so that users and developers can easily make amos work with their projects. It is designed for Python coders at all levels. Beginners should be able to follow the readable code and internal documentation to understand how it works. More advanced users should find complex and tricky problems addressed through efficient code.',
    'author': 'WithPrecedent',
    'author_email': 'coreyrayburnyung@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
