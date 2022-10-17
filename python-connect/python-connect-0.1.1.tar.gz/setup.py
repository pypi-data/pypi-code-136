# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyconn',
 'pyconn.client',
 'pyconn.client.db',
 'pyconn.client.lake',
 'pyconn.constant',
 'pyconn.errors',
 'pyconn.model',
 'pyconn.ops',
 'pyconn.ops.io',
 'pyconn.ops.sync',
 'pyconn.utils']

package_data = \
{'': ['*']}

install_requires = \
['Humre>=0.2.0,<0.3.0',
 'addict>=2.4.0,<3.0.0',
 'pampy>=0.3.0,<0.4.0',
 'pendulum>=2.1.2,<3.0.0',
 'pydantic>=1.10.1,<2.0.0',
 'sqlmodel>=0.0.8,<0.0.9',
 'toml>=0.10.2,<0.11.0']

extras_require = \
{'aws': ['s3>=3.0.0,<4.0.0', 'boto3>=1.24.69,<2.0.0'],
 'google': ['google-cloud-bigquery>=3.3.2,<4.0.0',
            'google-cloud-storage>=2.5.0,<3.0.0'],
 'mysql': ['aiomysql>=0.1.1,<0.2.0'],
 'pgsql': ['psycopg[binary]>=3.1.2,<4.0.0', 'asyncpg>=0.26.0,<0.27.0']}

setup_kwargs = {
    'name': 'python-connect',
    'version': '0.1.1',
    'description': 'python database manipulation with advanced features',
    'long_description': None,
    'author': 'Thompson',
    'author_email': '51963680+thompson0012@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
