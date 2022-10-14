# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tom_alertstreams',
 'tom_alertstreams.alertstreams',
 'tom_alertstreams.management.commands',
 'tom_alertstreams.migrations']

package_data = \
{'': ['*']}

install_requires = \
['gcn-kafka>=0.2,<0.3',
 'hop-client>=0.7,<0.8',
 'psycopg2-binary>=2.9,<3.0',
 'tomtoolkit>=2.10,<3.0']

setup_kwargs = {
    'name': 'tom-alertstreams',
    'version': '0.2.0',
    'description': 'Reusable TOMToolkit app for listening to kafka streams.',
    'long_description': '# tom-alertstreams\n\n`tom-alertstreams` is a reusable TOM Toolkit app for listening to kafka streams.\n\n`tom-alertstreams` provides a management command, `readstreams`. There are no `urlpatterns`,\nno Views, and no templates. The `readstreams` management command reads the `settings.py` `ALERT_STREAMS`\nconfiguration and starts listening to each configured Kafka stream. It is not expected\nto return, and is intended to run along side your TOM\'s server component. The `ALERT_STREAMS`\nconfiguration (see below) tells `readstreams` what streams to access, what topics to listen to,\nand what to do with messages that arrive on a given topic.\n\n## Installation\n\n1. Install the package into your TOM environment:\n    ```bash\n    pip install tom-alertstreams\n   ```\n\n2. In your project `settings.py`, add `tom_alertstreams` to your `INSTALLED_APPS` setting:\n\n    ```python\n    INSTALLED_APPS = [\n        ...\n        \'tom_alertstreams\',\n    ]\n    ```\n\nAt this point you can verify the installation by running `./manage.py` to list the available\nmanagement commands and see\n\n   ```bash\n   [tom_alertstreams]\n       readstreams\n   ```\nin the output.\n\n## Configuration\n\nEach Kafka stream that your TOM (via `readstreams` listens to will have a configuration dictionary\nin your `settings.py` `ALERT_STREAMS`. `ALERT_STREAMS` is a list of configuration dictionaries, one\ndictionary for each Kafka stream. Here\'s an example `ALERT_STREAMS` configuration for two Kafka streams:\n[SCiMMA Hopskotch](https://scimma.org/hopskotch.html) and\n[GCN Classic over Kafka](https://gcn.nasa.gov/quickstart).\n\n```python\nALERT_STREAMS = [\n    {\n        \'ACTIVE\': True,\n        \'NAME\': \'tom_alertstreams.alertstreams.hopskotch.HopskotchAlertStream\',\n        \'OPTIONS\': {\n            \'URL\': \'kafka://kafka.scimma.org/\',\n            \'USERNAME\': os.getenv(\'SCIMMA_AUTH_USERNAME\', None),\n            \'PASSWORD\': os.getenv(\'SCIMMA_AUTH_PASSWORD\', None),\n            \'TOPIC_HANDLER\': {\n                \'sys.heartbeat\': (lambda x: print(x)),\n                \'tomtoolkit.test\': (lambda x: print(x)),\n                \'hermes.test\': (lambda x: print(x)),\n            },\n        },\n    },\n    {\n        \'ACTIVE\': True,\n        \'NAME\': \'tom_alertstreams.alertstreams.gcn.GCNClassicAlertStream\',\n        # The keys of the OPTIONS dictionary become (lower-case) properties of the AlertStream instance.\n        \'OPTIONS\': {\n            # see https://github.com/nasa-gcn/gcn-kafka-python#to-use for configuration details.\n            \'GCN_CLASSIC_CLIENT_ID\': os.getenv(\'GCN_CLASSIC_CLIENT_ID\', None),\n            \'GCN_CLASSIC_CLIENT_SECRET\': os.getenv(\'GCN_CLASSIC_CLIENT_SECRET\', None),\n            \'DOMAIN\': \'gcn.nasa.gov\',  # optional, defaults to \'gcn.nasa.gov\'\n            \'CONFIG\': {  # optional\n                # \'group.id\': \'tom_alertstreams - llindstrom@lco.global\',\n                # \'auto.offset.reset\': \'earliest\',\n                # \'enable.auto.commit\': False\n            },\n            \'TOPIC_HANDLER\': {\n                \'gcn.classic.text.LVC_INITIAL\': (lambda x: print(x)),\n                \'gcn.classic.text.LVC_PRELIMINARY\': (lambda x: print(x)),\n                \'gcn.classic.text.LVC_RETRACTION\': (lambda x: print(x)),\n            },\n        },\n    }\n]\n```\n\nThe configuration dictionary for each `AlertStream` subclass will contain these key-value pairs:\n* `ACTIVE`: Boolean which tells `readstreams` to access this stream. Should be `True`, unless you want to\nkeep a configuration dictionary, but ignore the stream.\n* `NAME`: The name of the `AlertStream` subclass that implements the interface to this Kafka stream. `tom_alertstreams`\nwill provide `AlertStream` subclasses for major astromical Kafka streams. See below for instructions on Subclassing\nthe `AlertStream` base class.\n* `OPTIONS`: A dictionary of key-value pairs specific to the`AlertStream` subclass given by `NAME`. The doc string for\n`AlertStream` subclass should document what is expected. Typically, a URL, authentication information, and a dictionary,\n`TOPIC_HANDLER`, will be required. See "Subclassing `AlertStream`" below.\n\n## Alert Handling\n\ndocumentation coming.\n## Subclassing `AlertStream`\n\ndocumentation coming.',
    'author': 'TOM Toolkit Project',
    'author_email': 'tomtoolkit@lco.global',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TOMToolkit/tom-alertstreams',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
