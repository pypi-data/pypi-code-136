# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xit', 'xit.books']

package_data = \
{'': ['*']}

install_requires = \
['sphinx-autodoc-annotation>=1.0.post1,<2.0', 'sphinx>=5.2.3,<6.0.0']

extras_require = \
{'all': ['matplotlib>=3.6.0,<4.0.0',
         'jupyterlab[docs]>=3.4.5,<4.0.0',
         'myst-nb>=0.16.0,<0.17.0',
         'jupytext>=1.14.1,<2.0.0',
         'jupyterlab-code-formatter>=1.5.3,<2.0.0',
         'numpydoc>=1.4.0,<2.0.0',
         'pydata-sphinx-theme>=0.10.1,<0.11.0',
         'sphinx-rtd-theme>=1.0.0,<2.0.0',
         'voila>=0.3.6,<0.4.0',
         'sphinx-issues>=3.0.1,<4.0.0'],
 'data': ['matplotlib>=3.6.0,<4.0.0',
          'numpydoc>=1.4.0,<2.0.0',
          'pydata-sphinx-theme>=0.10.1,<0.11.0'],
 'devops': ['sphinx-issues>=3.0.1,<4.0.0'],
 'docs': ['sphinx-rtd-theme>=1.0.0,<2.0.0'],
 'notebooks': ['matplotlib>=3.6.0,<4.0.0',
               'jupyterlab[docs]>=3.4.5,<4.0.0',
               'myst-nb>=0.16.0,<0.17.0',
               'jupytext>=1.14.1,<2.0.0',
               'jupyterlab-code-formatter>=1.5.3,<2.0.0'],
 'web': ['voila>=0.3.6,<0.4.0']}

setup_kwargs = {
    'name': 'xit-books',
    'version': '0.1.0',
    'description': "Documentation manager based on 'Sphinx' and some extensions.",
    'long_description': "Xit Projects (Books)!\n=====================\n\nDocumentation manager and generator based on 'Sphinx'.\n\n.. note::\n\n   The project is currently in development and is not ready for production\n   use.\n\n\nInstall\n-------\n\nDevelopment Stage:\n\n  Check `ADR-4 <xit-adr-4_>`__ on base namespace project about how to use\n  poetry_ to manage how to evolve projects on development stages.\n\n  *This section is under construction*\n\n.. _xit-adr-4: https://github.com/med-merchise/xit/blob/main/docs/source/adrs/adr-0004-poetry-for-development-stage.rst\n.. _poetry: https://python-poetry.org\n\nProduction Stage:\n\n  *This section is under construction*\n\nAfter installation tasks:\n\n  Each of our projects should have a ``backlog-0001`` document with task to\n  execute after a project is installed.  This document must be located in the\n  ``docs/source/backlog`` directory.\n\n\nDocumentation\n-------------\n\n**Note** that because the purpose of this project is to be a documentation\nmanager, it will be usualy installed in other projects as a development\ndependency.\n\n*This section is under construction*\n",
    'author': 'Medardo Antonio Rodriguez',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/med-merchise/xit.books',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
