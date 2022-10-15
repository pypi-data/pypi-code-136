# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['souswift_core',
 'souswift_core.exc',
 'souswift_core.filters',
 'souswift_core.future',
 'souswift_core.future.providers',
 'souswift_core.providers',
 'souswift_core.utils']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.41,<2.0.0',
 'aiomysql>=0.1.1,<0.2.0',
 'context-handler>=5.0.0,<6.0.0',
 'fastapi>=0.85.0,<0.86.0',
 'orjson>=3.8.0,<4.0.0',
 'pydantic[email]>=1.10.2,<2.0.0',
 'tzdata>=2022.4,<2023.0']

setup_kwargs = {
    'name': 'souswift-core',
    'version': '2.0.2',
    'description': '',
    'long_description': 'None',
    'author': 'Gustavo Correa',
    'author_email': 'self.gustavocorrea@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
