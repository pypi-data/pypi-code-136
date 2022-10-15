# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsonapi_pydantic', 'jsonapi_pydantic.v1_0', 'jsonapi_pydantic.v1_0.resource']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'jsonapi-pydantic',
    'version': '0.1.2',
    'description': 'JSON:API implementation with pydantic.',
    'long_description': '# jsonapi-pydantic\n\n<p align="center">\n  <em><a href="https://jsonapi.org" target="_blank">JSON:API</a> implementation with <a href="https://pydantic-docs.helpmanual.io" target="_blank">Pydantic.</a>\n  </em>\n</p>\n<p align="center">\n  <a href="https://pypi.org/project/jsonapi-pydantic/" target="_blank">\n      <img src="https://img.shields.io/pypi/v/jsonapi-pydantic" alt="PyPI">\n  </a>\n  <a href="https://github.com/impocode/jsonapi-pydantic/blob/master/license.md" target="_blank">\n      <img src="https://img.shields.io/github/license/impocode/jsonapi-pydantic.svg" alt="License">\n  </a>\n</p>\n\n## Description\n\n`jsonapi-pydantic` provides a suite of Pydantic models matching the JSON:API specification.\n\n## Install\n\n```shell\n$ pip install jsonapi-pydantic\n```\n\nOr use your python package manager.\n\n## Usage\n\nObject with primary data:\n\n```python\nfrom jsonapi_pydantic.v1_0 import TopLevel\n\nexternal_data = {\n    "data": [\n        {\n            "type": "articles",\n            "id": "1",\n            "attributes": {\n                "title": "JSON:API paints my bikeshed!",\n                "body": "The shortest article. Ever.",\n                "created": "2015-05-22T14:56:29.000Z",\n                "updated": "2015-05-22T14:56:28.000Z",\n            },\n            "relationships": {"author": {"data": {"id": "42", "type": "people"}}},\n        }\n    ],\n    "included": [\n        {"type": "people", "id": "42", "attributes": {"name": "John", "age": 80, "gender": "male"}}\n    ],\n}\n\ntop_level = TopLevel(**external_data)\n\nprint(top_level.dict(exclude_unset=True))\n"""\n{\n    "data": [\n        {\n            "type": "articles",\n            "id": "1",\n            "attributes": {\n                "title": "JSON:API paints my bikeshed!",\n                "body": "The shortest article. Ever.",\n                "created": "2015-05-22T14:56:29.000Z",\n                "updated": "2015-05-22T14:56:28.000Z",\n            },\n            "relationships": {"author": {"data": {"id": "42", "type": "people"}}},\n        }\n    ],\n    "included": [\n        {"type": "people", "id": "42", "attributes": {"name": "John", "age": 80, "gender": "male"}}\n    ],\n}\n"""\nprint(top_level.data)\n"""\n[\n    Resource(\n        type="articles",\n        id="1",\n        attributes={\n            "title": "JSON:API paints my bikeshed!",\n            "body": "The shortest article. Ever.",\n            "created": "2015-05-22T14:56:29.000Z",\n            "updated": "2015-05-22T14:56:28.000Z",\n        },\n        relationships={\n            "author": Relationship(\n                links=None, data=ResourceIdentifier(id="42", type="people", meta=None), meta=None\n            )\n        },\n        links=None,\n        meta=None,\n    )\n]\n"""\n```\n\n## License\n\nSee [license.md](https://github.com/impocode/jsonapi-pydantic/blob/master/license.md).\n',
    'author': 'impocode',
    'author_email': 'impocode@impocode.com',
    'maintainer': 'impocode',
    'maintainer_email': 'impocode@impocode.com',
    'url': 'https://github.com/impocode/jsonapi-pydantic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
