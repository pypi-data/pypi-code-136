# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pnwapi']

package_data = \
{'': ['*']}

install_requires = \
['pnwkit-py>=2.5.4,<3.0.0', 'tortoise>=0.1.1,<0.2.0']

setup_kwargs = {
    'name': 'pnwapi',
    'version': '0.1.0',
    'description': '',
    'long_description': '# pnwapi\n\nPnwapi is a Python library for accessing the Politics and War API. It uses a simple, object-oriented approach to accessing the API, caching data, and handling errors. Pnwapi is designed around the concept of keeping a local copy of important data in a database, allowing for faster access, less reliance on the API and more advanced queries.\n\n## Installation\n\nPython 3.10 or higher is required. Pnwapi is available on PyPI and can be installed with pip:\n\n```bash\npip install pnwapi\n```\n\n## Usage\n\n```python\nimport pnwapi\n\npnw = pnwapi.init("YOUR_API_KEY", "YOUR_BOT_KEY", "DB_CONNECTION_STRING")\n```\n\n## Documentation\n\nDocumentation can be found at [pnwapi.readthedocs.io](https://pnwapi.readthedocs.io/en/latest/).\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Christian',
    'author_email': '59421913+Cikmo@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
