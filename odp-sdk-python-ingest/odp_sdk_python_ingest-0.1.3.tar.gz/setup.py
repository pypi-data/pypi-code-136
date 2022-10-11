# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['odp',
 'odp.auth',
 'odp.auth.cdf',
 'odp.auth.odp',
 'odp.auth.prefect',
 'odp.compute',
 'odp.compute.blocks',
 'odp.compute.cli',
 'odp.compute.cli.params',
 'odp.compute.config',
 'odp.compute.deploy',
 'odp.compute.deploy.runtime',
 'odp.compute.deploy.schedule',
 'odp.compute.deploy.storage',
 'odp.compute.flow_state',
 'odp.compute.flow_state.store',
 'odp.compute.lineage',
 'odp.compute.metrics',
 'odp.compute.metrics.client',
 'odp.compute.state_handlers',
 'odp.compute.tasks',
 'odp.compute.tasks.azure',
 'odp.compute.tasks.cdf',
 'odp.compute.tasks.fs',
 'odp.compute.tasks.gcp',
 'odp.compute.tasks.microsoft',
 'odp.compute.tasks.postgres',
 'odp.compute.tasks.rest',
 'odp.compute.watermark',
 'odp.types',
 'odp.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'azure-common>=1.1.28,<2.0.0',
 'azure-identity>=1.11.0,<2.0.0',
 'azure-keyvault-secrets>=4.6.0,<5.0.0',
 'azure-keyvault>=4.2.0,<5.0.0',
 'azure-storage-blob>=12.13.1,<13.0.0',
 'azure-storage-common>=2.1.0,<3.0.0',
 'click>=8.1.3,<9.0.0',
 'decorator>=5.1.1,<6.0.0',
 'docker>=6.0.0,<7.0.0',
 'inflection>=0.5.1,<0.6.0',
 'msal-extensions>=1.0.0,<2.0.0',
 'msal>=1.19.0,<2.0.0',
 'prefect-dask>=0.2.0,<0.3.0',
 'prefect>=2.4.2,<3.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pykube-ng>=22.9.0,<23.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'slugify>=0.0.1,<0.0.2']

setup_kwargs = {
    'name': 'odp-sdk-python-ingest',
    'version': '0.1.3',
    'description': 'ODP ingest SDK',
    'long_description': 'ODP Ingest SDK\n',
    'author': 'Thomas Li Fredriksen',
    'author_email': 'thomas.fredriksen@oceandata.earth',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
