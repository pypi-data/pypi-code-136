# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['serverless_crud',
 'serverless_crud.actions',
 'serverless_crud.appsync',
 'serverless_crud.aws',
 'serverless_crud.builders',
 'serverless_crud.dynamodb',
 'serverless_crud.graphql',
 'serverless_crud.rest']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.4,<3.0',
 'aws-lambda-powertools[pydantic]>=1.24,<2.0',
 'graphene-pydantic>=0.3.0,<0.4.0',
 'graphene>=3.0,<4.0',
 'inflect>=5.3.0,<6.0.0',
 'stringcase>=1.2.0,<2.0.0']

extras_require = \
{'sentry': ['sentry-sdk>=1.5,<2.0']}

setup_kwargs = {
    'name': 'python-serverless-crud',
    'version': '1.3.1',
    'description': 'Simple and powerful tool for quick serverless data management via API. ',
    'long_description': '# python-serverless-crud\n\n## The idea \n\nSimple and powerful tool for quick serverless data management via API. \n\n## Key concepts\n\n- Don\'t Repeat Yourself - easy model definition with schema and cloud formation generation support\n- Best practices applied by default (created with AWS LambdaPower Tools)\n- Flexibility - enable, extend and modify what is needed\n- One ring to rule them all - support for REST API, GraphQL (via API Gateway), AppSync GraphQL (direct resolvers)\n\n\n## Features\n\n- Full CRUD support with validation\n- Native support for DynamoDB (including CloudFormation creation via troposphere)\n  - GlobalSecondaryIndex support\n  - LocalSecondaryIndex support\n  - Primary Key with and without sort keys\n- Support for Scan, Query operations on the tables and indexes\n- Virtual List method on the table or index\n- Integrated record owner feature with KeyCondition and FilterCondition support (auto-detect)\n\n# Documentation\n\n## Sample service\n\n```python\nfrom aws_lambda_powertools import Tracer\nfrom aws_lambda_powertools.logging import correlation_paths\nfrom serverless_crud import api\nfrom serverless_crud.dynamodb import annotation as db\nfrom serverless_crud.model import BaseModel\nfrom serverless_crud.logger import logger\n\ntracer = Tracer()\n\n\n@db.Model(\n    key=db.PrimaryKey(id=db.KeyFieldTypes.HASH),\n    indexes=(\n            db.GlobalSecondaryIndex("by_user", user=db.KeyFieldTypes.HASH, created=db.KeyFieldTypes.RANGE),\n    ),\n    owner_field="user"\n)\nclass Device(BaseModel):\n    id: str\n    created: int\n    user: str = None\n\n\napi.rest.registry(Device, alias="device")\n\n\n@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)\n@tracer.capture_lambda_handler\ndef rest_handler(event, context):\n    return api.rest.handle(event, context)\n```\n\nWith just a few lines of the code we are able to create `Device` model service which then can be extended. \nIn this example we:\n\n1. Defined our `Device` model with some extra metadata, used by our generators. That includes:\n   1. Table key definition\n   2. GlobalSecondaryIndex\n   3. Definition of the field which will hold `owner` of the record (identity provided by cognito)\n2. Registered our `Device` model into rest API under `device` alias\n3. Created rest handler which then can be referred in our `serverless.yml` file \n\nA few notes here:\n- we need to define `rest_handler` function if we would like to use it as a target for local execution with serverless freamework\n- Lambda Power Tools are build around functions and they don\'t work properly with object methods\n- We use one function per API type, and we relay on internal router provided by each API implementation \n\n### Serverless integration\n\nIf you use (serverless-builder)[https://github.com/epsyhealth/serverless-builder] you can create your `serverless.yml` with just a few lines of code (including DynamodbTables)\n\n```python\nfrom serverless import Service, Configuration\nfrom serverless.aws.features import XRay\nfrom serverless.aws.functions.http import HTTPFunction\nfrom serverless.plugins import PythonRequirements, Prune\nfrom serverless.provider import AWSProvider\nfrom troposphere import dynamodb\n\nfrom timemachine_api.handlers import api\n\nservice = Service(\n    "timemachine-api",\n    "Collect events in chronological order",\n    AWSProvider(),\n    config=Configuration(\n        domain="epsy.app"\n    )\n)\nservice.provider.timeout = 5\n\nservice.plugins.add(Prune())\nservice.plugins.add(PythonRequirements(layer=False, useStaticCache=False, dockerSsh=True))\n\nservice.enable(XRay())\n\nfor name, table_specification in api.dynamodb_table_specifications().items():\n    service.resources.add(dynamodb.Table(name, **table_specification))\n\nauthorizer = dict(name="auth",\n                  arn="arn:aws:cognito-idp:us-east-1:772962929486:userpool/us-east-1_FCl7gKtHC")\n\nservice.builder.function.http("rest", "Time machine REST API", "/rest/{proxy+}", HTTPFunction.ANY,\n                              handler="timemachine_api.handlers.rest_handler", authorizer=authorizer)\n\n\nservice.render()\n```\n\n## Internals\n\n### Annotations\n\n`serverless-crud` project provides one annotation which must be used for all managed models.\n\n```python\nfrom serverless_crud.dynamodb import annotation as db\n@db.Model(\n    key=db.PrimaryKey(name=db.KeyFieldTypes.HASH),\n    indexes=(\n        db.GlobalSecondaryIndex(...),\n        db.LocalSecondaryIndex(...)\n    ),\n    owner_field="field"\n)\n```\n\nModel annotation accepts:\n- `key` - primary key definition, in form of `kwargs` where name of parameter would be a field name which should \n be used  in key, and value should be a value of `KeyFieldTypes` enum\n- `indexes` - list of indexes GlobalSecondaryIndex|LocalSecondaryIndex. Indexes are defined in same way as primary key\n- `owner_field` - name of the field which should be used for data filtering (based on the cognito identity)\n\n\n### Data owner \n\n`serverless-crud` can enforce some base data filtering on all kind of operations using Dynamodb conditional operations. \nIf you would like to use this feature you must set `owner_field` on each model you would like to use this feature.\n\nLibrary will use this field for:\n- setting its value on model creation / update (it will overwrite any value provided by user)\n- as an extra `ConditionExpression` during `GET` and `DELETE` operations\n- as a part of either `FilterExpression` or `KeyExpression` for Scan, Query and List operations\n\n\n### Model registration\n\nTo be able to manage given model, you must first register it with specific API. \nThis can be done with a single line of code:\n\n```python\napi.rest.registry(Device, alias="device")\n```\n\nYou need to provide only a model type to `registry` method, all other parameters are optional. \nIf you like, you can omit `alias` parameter, in that case framework will use model class name.\n\n### Customizing endpoint behaviour\n\nFramework defines a set of classes located in `serverless_crud.actions`:\n- CreateAction\n- DeleteAction\n- GetAction\n- ScanAction, ListAction, QueryAction\n- UpdateAction\n\nall those classes are subclasses of `serverless_crud.actions.base.Action` class and can be extended if needed. \n\nYou may need to execute custom logic after object creation, that can be done with custom `CreateAction` subclass\n```python\n\nfrom serverless_crud.actions import CreateAction\n\nclass CreateDeviceAction(CreateAction):\n    def handle(self, event: APIGatewayProxyEvent, context):\n        super().handle(event, context)\n        \n        # custom logic\n\n\napi.rest.registry(Device, create=CreateDeviceAction)\n```\n\nYou can set custom handlers for each supported operation:\n\n```python\ndef registry(self, model, alias=None, get=GetAction, create=CreateAction, update=UpdateAction, delete=DeleteAction,\n             lookup_list=ListAction, lookup_scan=ScanAction, lookup_query=QueryAction):\n```\n\nAs you can see, all actions are defined by default. That also means that all actions are enabled by default, but\neach action can be disabled.\n\nIf you need to disable action you need to set action handler to `None`, that will prevent framework from creating\nroute for given action, and it will disable whole logic behind it. \n\n### Routes\n\nREST API specific feature. \n\nFramework will create multiple routes for each register model, using `alias` as a URL namespace. \nGenerated routes: \n\n- GET /rest/{alias}/{pk} - fetch object by PK (see notes about PK below)\n- POST /rest/{alias} - create new record\n- PUT /rest/{alias}/{pk} - update record with given PK \n- DELETE /rest/{alias}/{pk} - delete record with given PK \n- GET /rest/lookup/{alias}/list - list all the records of given type using Query on the table\n- GET /rest/lookup/{alias}/list/{index_name} - list all the records of the given type using Query on specific index\n- POST /rest/lookup/{alias}/query - perform a query on given table\n- POST /rest/lookup/{alias}/query/{index_name} - perform a query on given index\n- POST /rest/lookup/{alias}/scan - perform a scan on given table\n- POST /rest/lookup/{alias}/scan/{index_name} - perform a scan on given index\n\n#### Primary Keys\n> *Please remember that with DynamoDB key is a Partition Key with optional Sort Key. \nIn case you define Sort Key DynamoDB will require a value for it while getting / deleting key.\nIn that case framework will modify routes to include sort key as an extra path parameter* \n\n\n## Endpoints\n',
    'author': 'Epsy',
    'author_email': 'engineering@epsyhealth.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/epsylabs/python-serverless-crud',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
