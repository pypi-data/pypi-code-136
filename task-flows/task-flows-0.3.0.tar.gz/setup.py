# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['task_flows', 'task_flows.models']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.35,<2.0.0',
 'alert-msgs>=0.1.1,<0.2.0',
 'click>=8.1.3,<9.0.0',
 'docker>=5.0.3,<6.0.0',
 'dynamic-imports>=0.2.0,<0.3.0',
 'psycopg2>=2.9.3,<3.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'ready-logger>=0.1.4,<0.2.0',
 'tqdm>=4.64.0,<5.0.0']

entry_points = \
{'console_scripts': ['tasks = task_flows.admin:cli']}

setup_kwargs = {
    'name': 'task-flows',
    'version': '0.3.0',
    'description': 'Python task management, scheduling, alerts.',
    'long_description': None,
    'author': 'Dan',
    'author_email': 'kelleherjdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
