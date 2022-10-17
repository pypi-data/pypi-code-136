# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ur_py_ctl']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.0,<2.0']}

setup_kwargs = {
    'name': 'ur-py-ctl',
    'version': '0.1.6',
    'description': 'Python wrapper around URScript (for Universal Robotics robots).',
    'long_description': '# ur_py_ctl\n\n[![PyPI version](https://badge.fury.io/py/ur-py-ctl.svg)](https://pypi.org/project/ur-py-ctl/)\n[![CI Pipeline status](https://gitlab.control.lth.se/robotlab/ur_py_ctl/badges/main/pipeline.svg)](https://gitlab.control.lth.se/robotlab/ur_py_ctl/-/pipelines)\n[![Documentation Status](https://readthedocs.org/projects/ur-py-ctl/badge/?version=latest)](https://ur-py-ctl.readthedocs.io/en/latest/?badge=latest)\n\n* [Documentation](https://ur-py-ctl.readthedocs.io/)\n\n## Install\n\n[Installation instructions](https://ur-py-ctl.readthedocs.io/latest/installation.html)\n\n## Develop\n\n1. [Install poetry](https://python-poetry.org/docs/#installation)\n1. Install package and dependencies: `poetry install`\n1. Set up pre-commit: `poetry run pre-commit install`\n',
    'author': 'Anton Tetov',
    'author_email': 'anton@tetov.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.control.lth.se/robotlab/ur_py_ctl',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
