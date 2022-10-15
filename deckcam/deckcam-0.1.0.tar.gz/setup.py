# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deckcam']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'deckcam',
    'version': '0.1.0',
    'description': '',
    'long_description': '## deckcam ##\n\nCustom software to manage a StreamDeck with Companion, an ATEM switch, and up to three cameras.\n\n## developer notes ##\n\nConfiguration setup up by loosely following the articles here:\n\n* https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-1\n* https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2\n* https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-3',
    'author': 'Joe Marley',
    'author_email': 'joe.marley@live.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
