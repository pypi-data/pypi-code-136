# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src',
 'google': 'src/google',
 'google.api': 'src/google/api',
 'protoc_gen_openapiv2': 'src/protoc_gen_openapiv2',
 'protoc_gen_openapiv2.options': 'src/protoc_gen_openapiv2/options'}

packages = \
['aserto',
 'aserto.authorizer.v2',
 'aserto.authorizer.v2.api',
 'google',
 'google.api',
 'protoc_gen_openapiv2',
 'protoc_gen_openapiv2.options']

package_data = \
{'': ['*']}

install_requires = \
['certifi>=2021.5.30,<2022.0.0', 'typing-extensions>=3.10.0,<4.0.0']

setup_kwargs = {
    'name': 'aserto-authorizer',
    'version': '0.0.2',
    'description': 'gRPC client for Aserto Authorizer service instances',
    'long_description': '# Aserto Authorizer gRPC client\nThis is an automatically generated client for interacting with Aserto\'s [Authorizer service](https://docs.aserto.com/docs/authorizer-guide/overview) using the gRPC protocol.\n\n## Installation\n### Using Pip\n```sh\npip install aserto-authorizer\n```\n### Using Poetry\n```sh\npoetry add aserto-authorizer\n```\n## Usage\n```py\nfrom aserto_authorizer.aserto.authorizer.v2.api import (\n    IdentityContext,\n    IdentityType,\n    PolicyContext,\n)\nfrom aserto_authorizer.aserto.authorizer.v2 import (\n    AuthorizerStub,\n    DecisionTreeOptions,\n    DecisionTreeResponse,\n    PathSeparator,\n)\nfrom grpclib.client import Channel\n\n\nasync with Channel(host=host, port=port, ssl=True) as channel:\n    headers = {\n        "authorization": f"basic {ASERTO_API_KEY}"\n    }\n\n    client = AuthorizerStub(channel, metadata=headers)\n\n    response = await client.decision_tree(\n        policy_context=PolicyContext(\n            name=ASERTO_POLICY_NAME,\n            path=ASERTO_POLICY_PATH_ROOT,\n            decisions=["visible", "enabled", "allowed"],\n        ),\n        identity_context=IdentityContext(type=IdentityType.IDENTITY_TYPE_NONE),\n        resource_context=Proto.Struct(),\n        options=DecisionTreeOptions(\n            path_separator=PathSeparator.PATH_SEPARATOR_DOT,\n        ),\n    )\n\n    assert response == DecisionTreeResponse(\n        path_root=ASERTO_POLICY_PATH_ROOT,\n        path=Proto.Struct(\n            fields={\n                "GET.your.policy.path": Proto.Value(\n                    struct_value=Proto.Struct(\n                        fields={\n                            "visible": Proto.Value(bool_value=True),\n                            "enabled": Proto.Value(bool_value=True),\n                            "allowed": Proto.Value(bool_value=False),\n                        },\n                    ),\n                ),\n            },\n        ),\n    )\n```',
    'author': 'Aserto, Inc.',
    'author_email': 'pypi@aserto.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aserto-dev/python-authorizer',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
