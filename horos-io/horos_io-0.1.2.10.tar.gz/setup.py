# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['horos_io', 'tests']

package_data = \
{'': ['*'], 'tests': ['horos_dummy/*']}

install_requires = \
['click',
 'decorator>=5.1.1,<6.0.0',
 'matplotlib>=3.5.3,<4.0.0',
 'opencv-python>=4.6.0.66,<5.0.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pydicom>=2.3.0,<3.0.0',
 'scipy>=1.9.1,<2.0.0',
 'tk>=0.1.0,<0.2.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['horos_io = horos_io.cli:main']}

setup_kwargs = {
    'name': 'horos-io',
    'version': '0.1.2.10',
    'description': 'small package to deal with data exported from Horos',
    'long_description': '========\nhoros_io\n========\n\n\n.. image:: https://img.shields.io/pypi/v/horos_io.svg\n        :target: https://pypi.python.org/pypi/horos_io\n\n.. image:: https://img.shields.io/travis/santomon/horos_io.svg\n        :target: https://travis-ci.com/santomon/horos_io\n\n.. image:: https://readthedocs.org/projects/horos-io/badge/?version=latest\n        :target: https://horos-io.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\n\n\nhandling .xml files when exported from horos; some dataset functionality\n\n\n* Free software: MIT\n* Documentation: https://horos-io.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `briggySmalls/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage\n',
    'author': 'Quang Anh Le Hong',
    'author_email': 'qa12_8@yahoo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/santomon/horos_io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
