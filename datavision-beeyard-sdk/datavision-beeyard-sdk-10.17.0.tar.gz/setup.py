# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datavision_beeyard_sdk',
 'datavision_beeyard_sdk.api',
 'datavision_beeyard_sdk.api.cell',
 'datavision_beeyard_sdk.api.document',
 'datavision_beeyard_sdk.api.event',
 'datavision_beeyard_sdk.api.file',
 'datavision_beeyard_sdk.api.health',
 'datavision_beeyard_sdk.api.image',
 'datavision_beeyard_sdk.api.overlay',
 'datavision_beeyard_sdk.api.statistics',
 'datavision_beeyard_sdk.api.version',
 'datavision_beeyard_sdk.api.workspace',
 'datavision_beeyard_sdk.models']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.2.0,<22.0.0', 'httpx>=0.15.4,<0.19.0']

setup_kwargs = {
    'name': 'datavision-beeyard-sdk',
    'version': '10.17.0',
    'description': 'BeeYard Python SDK',
    'long_description': None,
    'author': 'DataVision',
    'author_email': 'support@datavision.software',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://docs.beeyard.services/docs/reference/sdk/python/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
