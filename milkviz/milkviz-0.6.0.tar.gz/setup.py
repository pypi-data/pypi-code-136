# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['milkviz']

package_data = \
{'': ['*']}

install_requires = \
['legendkit>=0.2.4,<0.3.0', 'matplotlib>=3.5,<4.0', 'pandas>=1.5.0,<2.0.0']

extras_require = \
{'all': ['networkx>=2.8.6,<3.0.0', 'matplotlib-venn>=0.11.7,<0.12.0']}

setup_kwargs = {
    'name': 'milkviz',
    'version': '0.6.0',
    'description': 'Self-opinionated miscellaneous visualizations library in python',
    'long_description': "# MilkViz\n\n[![Documentation Status](https://img.shields.io/readthedocs/milkviz?logo=readthedocs&logoColor=white&style=flat-square)](https://milkviz.readthedocs.io/en/latest?badge=latest)\n![Build&Test](https://img.shields.io/github/workflow/status/Mr-Milk/milkviz/Build?style=flat-square&logo=github)\n![pypi version](https://img.shields.io/pypi/v/milkviz?color=blue&logo=python&logoColor=white&style=flat-square)\n\nMr-Milk's own visualization library. \nSome commonly used visualizations in my own research.\nBut not available out there.\n\n[Gallery](https://milkviz.readthedocs.io/en/latest/gallery_examples/index.html)\n\nCopyright © 2022, Mr-Milk\n",
    'author': 'Mr-Milk',
    'author_email': 'yb97643@um.edu.mo',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Mr-Milk/milkviz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
