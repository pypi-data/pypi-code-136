# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ascend',
 'ascend.auth',
 'ascend.external',
 'ascend.external.protoc_gen_swagger.options',
 'ascend.log',
 'ascend.openapi',
 'ascend.openapi.openapi.openapi_client',
 'ascend.openapi.openapi.openapi_client.api',
 'ascend.protos.api',
 'ascend.protos.ascend',
 'ascend.protos.component',
 'ascend.protos.connection',
 'ascend.protos.content_encoding',
 'ascend.protos.core',
 'ascend.protos.environment',
 'ascend.protos.expression',
 'ascend.protos.external',
 'ascend.protos.fault',
 'ascend.protos.format',
 'ascend.protos.function',
 'ascend.protos.io',
 'ascend.protos.metrics',
 'ascend.protos.operator',
 'ascend.protos.pattern',
 'ascend.protos.preview',
 'ascend.protos.resource',
 'ascend.protos.resources',
 'ascend.protos.schema',
 'ascend.protos.task',
 'ascend.protos.text',
 'ascend.protos.worker',
 'ascend.sdk',
 'ascend.sdk.drd']

package_data = \
{'': ['*'], 'ascend.sdk': ['poetry/*', 'templates/v1/*', 'templates/v2/*']}

install_requires = \
['Jinja2>=3.1.1,<4.0.0',
 'chardet==3.0.4',
 'glog>=0.3.1,<0.4.0',
 'googleapis-common-protos==1.56.4',
 'idna==2.10',
 'networkx>=2.5,<3.0',
 'protobuf==3.20.1',
 'python-dateutil>=2.8.1,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'retry>=0.9.2,<0.10.0',
 'six==1.16.0',
 'toml==0.10.1',
 'urllib3>=1.26.5,<2.0.0']

setup_kwargs = {
    'name': 'ascend-io-sdk',
    'version': '0.2.50',
    'description': 'The Ascend.io SDK for Python',
    'long_description': '.. raw::html\n    <hidden>test</hidde>\n\n==============================\nThe Ascend.io Python SDK\n==============================\n\nThis package contains the `Ascend Python SDK <https://developer.ascend.io/docs/python-sdk>`_. This SDK is used to script the management of the\n`Ascend.io <https://www.ascend.io>`_ Data Automation Platform. The SDK can be used to create your own customizations of the\nplatform configuration, integrate with   CI/CD or other tools, as well as fully automate your environment.\n\n* **Automation.** Integrate Ascend with any combination of workflow and/or CI/CD tools your organization uses on a daily basis.\n* **Transparency.** Ascend deploys within your Cloud tenant (GCP, AWS, Azure) so you can see everything the platform is doing.\n* **Control.** Manage your Ascend Platform, build dataflows, extract metadata, and more in a completely programmatic way\n\n---------------\nGet Started\n---------------\nYou will need access to an Ascend.io installation. Developers can `sign up for a free trial <https://www.ascend.io/signup/>`_.\nIf you are already an Ascend customer, have your administrator add you to the platform.\n\nOnce you have access to the Platform, `create your developer API Access Keys <https://developer.ascend.io/docs/developer-keys>`_\nand `configure your local authentication file <https://developer.ascend.io/docs/python-sdk#authorization>`_. Remember to change\nthe word *trial* in your local authentication file to the name of your Ascend.io instance.\n\n\nInstall the python library using `pip <https://pip.pypa.io/en/latest/>`_::\n\n    $ pip3 install ascend-io-sdk\n\nStart writing your automations with the `Python Client <https://developer.ascend.io/docs/python-sdk-client-ref>`_.\n\n------------------\nRun the Examples\n------------------\nIf running some sample code works for you, try out the Ascend Python SDK by listing the dataflows\nwithin your Ascend instance::\n\n    from ascend.sdk.client import Client\n    from tabulate import tabulate\n\n    hostname = \'my-host-name\'\n    client = Client(hostname)\n    services = []\n    for ds in client.list_data_services().data:\n        services.append([ds.id, ds.name, ds.created_at, ds.updated_at])\n\n    print(tabulate(sorted(services, key=lambda x: x[1]), headers=["id", "name", "created at"]))\n\nWe release updates to the SDK all the time. If some features are missing, you get stuck, or you find\nsomething that you don\'t think is right, please let us know. We\'re here to make the developer experience\nas easy and enjoyable as possible. We know that fabulous Developer Relations is key!\n\n---------------\nRead the Docs\n---------------\n* `Ascend.io Python SDK Documentation <https://developer.ascend.io/docs/python-sdk>`_\n* `Ascend Developer Hub <https://developer.ascend.io>`_\n* `Ascend.io <https://www.ascend.io>`_\n\n',
    'author': 'Ascend.io Engineering',
    'author_email': 'support@ascend.io',
    'maintainer': 'Ascend.io Engineering',
    'maintainer_email': 'support@ascend.io',
    'url': 'https://www.ascend.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
