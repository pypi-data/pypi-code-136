# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xash', 'xash.charts']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.4,<2.0.0', 'scipy>=1.9.1,<2.0.0', 'xotl.tools>=2.2.5,<3.0.0']

extras_require = \
{'all': ['matplotlib>=3.6.0,<4.0.0',
         'scikit-learn>=1.1.2,<2.0.0',
         'seaborn>=0.12.0,<0.13.0',
         'plotly>=5.10.0,<6.0.0',
         'cufflinks>=0.17.3,<0.18.0',
         'kaleido==0.2.1',
         'openpyxl>=3.0.10,<4.0.0',
         'plotly-geo>=1.0.0,<2.0.0',
         'dash>=2.6.2,<3.0.0',
         'dash-bootstrap-components>=1.2.1,<2.0.0',
         'dash-daq>=0.5.0,<0.6.0',
         'jupyter-dash>=0.4.2,<0.5.0'],
 'dash': ['plotly>=5.10.0,<6.0.0',
          'cufflinks>=0.17.3,<0.18.0',
          'kaleido==0.2.1',
          'dash>=2.6.2,<3.0.0',
          'dash-bootstrap-components>=1.2.1,<2.0.0',
          'dash-daq>=0.5.0,<0.6.0'],
 'data': ['scikit-learn>=1.1.2,<2.0.0', 'seaborn>=0.12.0,<0.13.0'],
 'geo': ['plotly-geo>=1.0.0,<2.0.0'],
 'notebooks': ['matplotlib>=3.6.0,<4.0.0'],
 'office': ['openpyxl>=3.0.10,<4.0.0'],
 'plotly-notebooks': ['jupyter-dash>=0.4.2,<0.5.0'],
 'stats': ['seaborn>=0.12.0,<0.13.0']}

setup_kwargs = {
    'name': 'xash',
    'version': '0.1.0',
    'description': 'Data Science, Data Analysis, Plotting, ...',
    'long_description': 'Xash Project!\n=============\n\nData science, data analysis, graph visualization, ...\n\n\nInstall\n-------\n\nDevelopment Stage:\n\n  Check `ADR-5`_ on project `xint` about how to use poetry_ to manage how to\n  evolve projects on development stages.\n\n.. _adr-5: https://github.com/med-merchise/xint/blob/main/docs/source/adrs/adr-0005-poetry-for-development-stage.rst\n.. _poetry: https://python-poetry.org\n\nProduction Stage:\n\n  *This section is under construction*\n\nAfter installation tasks:\n\n  Each of our projects should have a ``backlog-0001`` document with task to\n  execute after a project is installed.  This document must be located in the\n  ``docs/source/backlog`` directory.\n\n\nDocumentation\n-------------\n\nTo manage the documentation of this project you must install it locally with\nthe ``docs`` group enabled::\n\n  poetry install --with docs\n\n\n*This section is under construction*\n',
    'author': 'Medardo Antonio Rodriguez',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/med-merchise/xash',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
