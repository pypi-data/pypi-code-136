# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sfn_workflow_client']

package_data = \
{'': ['*']}

install_requires = \
['aenum>=3.1.11,<4.0.0',
 'arrow>=1.2.3,<2.0.0',
 'backoff>=2.2.1,<3.0.0',
 'boto3>=1.24.89,<2.0.0']

setup_kwargs = {
    'name': 'sfn-workflow-client',
    'version': '1.1.0',
    'description': 'Enhanced, asyncio-compatible client for AWS Step Functions.',
    'long_description': '# sfn_workflow_client\n\n[![CircleCI](https://circleci.com/gh/NarrativeScience/sfn-workflow-client/tree/master.svg?style=shield)](https://circleci.com/gh/NarrativeScience/sfn-workflow-client/tree/master) [![](https://img.shields.io/pypi/v/sfn_workflow_client.svg)](https://pypi.org/pypi/sfn_workflow_client/) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n\nEnhanced, asyncio-compatible client for AWS Step Functions.\n\nFeatures:\n\n- Trigger new executions\n- Query for state machine execution status\n- Wait for an execution to complete\n- Fetch execution history\n\nTable of Contents:\n\n- [Installation](#installation)\n- [Guide](#guide)\n- [Development](#development)\n\n## Installation\n\nsfn_workflow_client requires Python 3.6 or above.\n\n```bash\npip install sfn_workflow_client\n```\n\n## Guide\n\n```python\nfrom sfn_workflow_client.enums import ExecutionStatus\nfrom sfn_workflow_client.workflow import Workflow\n\n# Initialize a workflow client\nworkflow = Workflow("my-state-machine")\n# Fetch all executions\ncollection = await workflow.executions.fetch()\n# Fetch currently running executions\ncollection = await workflow.executions.fetch(status=ExecutionStatus.running)\n# Start a new execution\nexecution = await workflow.executions.create().start()\n# Start a new execution and wait until it completes (useful for tests)\nexecution = await workflow.executions.start_sync()\n# Find an execution by trace ID (for tests)\nexecution = await workflow.executions.fetch().find_by_trace_id("abc")\n# Fetch the event history of an execution\nevents = await execution.events.fetch()\n```\n\n## Development\n\nTo develop sfn_workflow_client, install dependencies and enable the pre-commit hook:\n\n```bash\npip install pre-commit tox\npre-commit install\n```\n\nTo run functional tests, you need to create an AWS IAM role with permissions to:\n\n- Create/update/delete state machines\n- Start/stop executions\n\nSet the following environment variables:\n\n- `AWS_ACCOUNT_ID`\n- `AWS_ACCESS_KEY_ID`\n- `AWS_SECRET_ACCESS_KEY`\n- `AWS_DEFAULT_REGION`\n- `AWS_IAM_ROLE_ARN`\n\nTo run tests:\n\n```bash\ntox\n```\n',
    'author': 'Jonathan Drake',
    'author_email': 'jdrake@narrativescience.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NarrativeScience/sfn-workflow-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
