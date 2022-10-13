# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cdcstream']

package_data = \
{'': ['*']}

install_requires = \
['numpy',
 'packaging',
 'pandas',
 'python-javabridge',
 'python-weka-wrapper3>=0.2,<0.3']

setup_kwargs = {
    'name': 'cdcstream',
    'version': '0.1.6',
    'description': "Implementation of Ienco's algorithm CDCStream",
    'long_description': "Implementation of an augmented version of Dino Ienco's algorithm **CDCStream** (Change Detection in Categorical Evolving Data Streams) ([https://doi.org/10.1145/2554850.2554864](https://doi.org/10.1145/2554850.2554864)).\n\nCite as TODO(Bibtex info).\n\n## Acknowledgements\nThis software was developed at the FZI Research Center for Information Technology.\nThe associated research was funded by the German Federal Ministry of Education and Research (grant number: 02K18D033) within the context of the project SEAMLESS.\n",
    'author': 'Martin Trat',
    'author_email': 'trat@fzi.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fzi-forschungszentrum-informatik/cdcstream',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
