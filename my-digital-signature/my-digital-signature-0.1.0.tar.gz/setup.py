# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['my_digital_signature']

package_data = \
{'': ['*']}

install_requires = \
['num2words>=0.5.12,<0.6.0']

entry_points = \
{'console_scripts': ['signature = '
                     'my_digital_signature.SIGNATURE:create_signature']}

setup_kwargs = {
    'name': 'my-digital-signature',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'ConstantZero',
    'author_email': 'mrzero@duck.com',
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
