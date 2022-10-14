# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alto_anomaly_detection']

package_data = \
{'': ['*']}

install_requires = \
['azure-cosmos>=4.3.0,<5.0.0',
 'crate>=0.27.2,<0.28.0',
 'numpy>=1.23.4,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'plotly>=5.10.0,<6.0.0',
 'sklearn>=0.0,<0.1',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'alto-anomaly-detection',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'mcvoramet',
    'author_email': 'vc2543@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
