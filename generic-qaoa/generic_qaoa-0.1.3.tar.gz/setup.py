# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['generic_qaoa',
 'generic_qaoa.clause',
 'generic_qaoa.qaoa',
 'generic_qaoa.vqf_helper']

package_data = \
{'': ['*']}

install_requires = \
['jupyter>=1.0.0,<2.0.0',
 'qiskit-ibm-runtime>=0.6.2,<0.7.0',
 'qiskit>=0.37.1,<0.38.0']

setup_kwargs = {
    'name': 'generic-qaoa',
    'version': '0.1.3',
    'description': '',
    'long_description': 'None',
    'author': 'Snir Bachar',
    'author_email': 'snir@quantum-machines.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
