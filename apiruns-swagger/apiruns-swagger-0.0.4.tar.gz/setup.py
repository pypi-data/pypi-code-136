# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apiruns_swagger', 'apiruns_swagger.swagger']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0']

setup_kwargs = {
    'name': 'apiruns-swagger',
    'version': '0.0.4',
    'description': 'Swagger documentation for Apiruns projects.',
    'long_description': '# apiruns-swagger\n\nSwagger documentation for Apiruns projects\n\nInstall\n\n```bash\npip install apiruns-swagger\n```\n\nUsing\n```python\nfrom apiruns_swagger import json_to_swagger\n\napiruns_schema = {\n    "path": "/users",\n    "schema": {\n        "name": "anybody",\n        "last_name": "anybody",\n    }\n}\n\nservers = [{"url": "https://api.cloud.apiruns.com"}]\n\nswagger_schema = json_to_swagger(apiruns_schema, servers=servers)\n```\n',
    'author': 'Jose Salas',
    'author_email': 'jose.salas@apiruns.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/apiruns/apiruns-swagger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
