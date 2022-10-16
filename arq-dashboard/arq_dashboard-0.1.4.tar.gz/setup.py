# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arq_dashboard',
 'arq_dashboard.api',
 'arq_dashboard.api.endpoints',
 'arq_dashboard.core',
 'arq_dashboard.schemas']

package_data = \
{'': ['*'], 'arq_dashboard': ['frontend/*', 'frontend/assets/*']}

install_requires = \
['aiometer>=0.3.0,<0.4.0',
 'arq>=0.24,<0.25',
 'arrow>=1.2.3,<2.0.0',
 'async-cache>=1.1.1,<2.0.0',
 'fastapi>=0.85.1,<0.86.0',
 'loguru>=0.6.0,<0.7.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyhumps>=3.7.3,<4.0.0',
 'uvicorn[standard]>=0.18.3,<0.19.0']

setup_kwargs = {
    'name': 'arq-dashboard',
    'version': '0.1.4',
    'description': 'A dashboard for ARQ built with FastAPI',
    'long_description': '# arq-dashboard\n\n[![PyPI version](https://badge.fury.io/py/arq-dashboard.svg)](https://badge.fury.io/py/arq-dashboard)\n[![Python CI](https://github.com/ninoseki/arq-dashboard/actions/workflows/test.yml/badge.svg)](https://github.com/ninoseki/arq-dashboard/actions/workflows/test.yml)\n\nA dashboard for [ARQ](https://github.com/samuelcolvin/arq) built with [FastAPI](https://github.com/tiangolo/fastapi).\n\n## Screenshots\n\n![img](https://raw.githubusercontent.com/ninoseki/arq-dashboard/main/screenshots/stats.png)\n\n---\n\n![img](https://raw.githubusercontent.com/ninoseki/arq-dashboard/main/screenshots/jobs.png)\n\n## Requirements\n\n- Python 3.8+\n\n## Installation\n\n```bash\npip install arq-dashboard\n```\n\n## Docs\n\n- [Configuration](https://github.com/ninoseki/arq-dashboard/wiki/Configuration)\n- [Usage](https://github.com/ninoseki/arq-dashboard/wiki/Usage)\n- [Advanced Usage](https://github.com/ninoseki/arq-dashboard/wiki/Advanced-Usage)\n\n## Alternatives\n\n- [SlavaSkvortsov/arq-django-admin](https://github.com/SlavaSkvortsov/arq-django-admin): Admin dashboard for arq based on django-rq\n- [long2ice/rearq](https://github.com/long2ice/rearq): A distributed task queue built with asyncio and redis, with built-in web interface\n- [tobymao/saq](https://github.com/tobymao/saq): Simple Async Queues\n',
    'author': 'Manabu Niseki',
    'author_email': 'manabu.niseki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ninoseki/arq-dashboard',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
