# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tetebeche']

package_data = \
{'': ['*']}

install_requires = \
['PyPDF2>=2.11.1,<3.0.0']

entry_points = \
{'console_scripts': ['tetebeche = tetebeche.cmd:main']}

setup_kwargs = {
    'name': 'tetebeche',
    'version': '0.1.0',
    'description': 'Script to generate a tėte-bêche book from two pdfs',
    'long_description': '# tetebeche\n\nThis is a tiny script of use only to eccentric publishers. It uses \n[PyPDF2](https://github.com/py-pdf/PyPDF2) to create a \n[tête-bêche book](https://en.wikipedia.org/wiki/Dos-%C3%A0-dos_binding#T%C3%AAte-b%C3%AAche)\nfrom two input pdfs. The two pdfs are merged, with the second reversed and rotated 180°.\n\nThe user should ensure that the input PDFs have the same page dimensions and that both have\nan even number of pages.\n\n## Usage\n\n    usage: tetebeche [-h] book1 book2 merged\n    \n    positional arguments:\n      book1       path to first (non-reversed) book\n      book2       path to second (reversed) book\n      merged      path to merged output file\n    \n    options:\n      -h, --help  show this help message and exit',
    'author': 'Jacob Smullyan',
    'author_email': 'smulloni@smullyan.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
