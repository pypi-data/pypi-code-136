# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['knada_gsm']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-secret-manager>=2.12.5,<3.0.0']

setup_kwargs = {
    'name': 'knada-gsm',
    'version': '0.1.2',
    'description': '',
    'long_description': 'None',
    'author': 'nada',
    'author_email': 'nada@nav.no',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
