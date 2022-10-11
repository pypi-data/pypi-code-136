# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['odd_models', 'odd_models.api_client']

package_data = \
{'': ['*']}

install_requires = \
['pydantic==1.8.2', 'requests==2.27.1', 'sqlparse==0.4.2']

setup_kwargs = {
    'name': 'odd-models',
    'version': '2.0.7',
    'description': 'Open Data Discovery Models',
    'long_description': "# Open Data Discovery models package\n\nModels automatically generated by `datamodel-code-generator` from [ODD OpenApi specification](https://github.com/opendatadiscovery/opendatadiscovery-specification)\n\n\n## Usage example:\n```python\nfrom odd_models.models import DataEntityList\n\ndata_entity_list = DataEntityList(data_source_oddrn='/postgresql/host/localhost/databases/opendatadiscovery', items=[])\n```",
    'author': 'Open Data Discovery',
    'author_email': 'pypi@opendatadiscovery.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/opendatadiscovery/odd-models-packager',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
