# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['opPrint']
install_requires = \
['PyYAML>=6.0,<7.0']

setup_kwargs = {
    'name': 'opprint',
    'version': '1.0.1',
    'description': 'Override print formatter',
    'long_description': 'python3 override print() formatting\n',
    'author': 'rapid537',
    'author_email': 'rapid537@zoho.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rapid537/op.git',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
