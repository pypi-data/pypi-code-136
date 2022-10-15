# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_access_advisor']

package_data = \
{'': ['*']}

install_requires = \
['aws-authenticator>=2022.10.1.0,<2023.0.0.0']

setup_kwargs = {
    'name': 'aws-access-advisor',
    'version': '2022.10.2.0',
    'description': 'Generate IAM actions list from AWS Access Advisor reports.',
    'long_description': '======================\n**aws-access-advisor**\n======================\n\nOverview\n--------\n\nGenerate IAM actions list from AWS Access Advisor reports.\n\nPrerequisites\n-------------\n\n- *Python >= 3.6*\n- *aws-authenticator (https://pypi.org/project/aws-authenticator/) >= 2022.10.1.0*\n\nRequired Arguments\n------------------\n\n- AWS entity ARN (role, user, etc. to use for report generation)\n- AWS authentication method (profile, iam, or sso)\n\nConditional Arguments\n---------------------\n\nIf authenticating with named profiles:\n\n- AWSCLI profile name\n\nIf authenticating with IAM acccess key credentials:\n\n- AWS access key id\n- AWS secret access key\n\nIf authenticating with SSO:\n\n- AWS account ID\n- AWS SSO Permission Set (role) name\n- AWS SSO login URL\n\nUsage\n-----\n\nInstallation:\n\n.. code-block:: BASH\n\n   pip3 install aws-access-advisor\n   # or\n   python3 -m pip install aws-access-advisor\n\nIn Python3 authenticating with named profiles:\n\n.. code-block:: PYTHON\n\n   import aws_access_advisor as access\n\n   report = access.get_report(\n      "<entity_arn>",\n      "profile",\n      profile_name="<profile_name>",\n    )\n   print(\n      f\'Job status: {report["JobStatus"]} after {report["processing_time"]} second(s).\'\n   )\n   print("\\n".join(access.parse(report)))\n\nIn Python3 authenticating with IAM access key credentials:\n\n.. code-block:: PYTHON\n\n   import aws_access_advisor as access\n\n   report = access.get_report(\n      "<entity_arn>",\n      "iam"\n      access_key_id="<access_key_id>",\n      secret_access_key="<secret_access_key>",\n    )\n   print(\n      f\'Job status: {report["JobStatus"]} after {report["processing_time"]} second(s).\'\n   )\n   print("\\n".join(access.parse(report)))\n\nIn Python3 authenticating with SSO:\n\n.. code-block:: PYTHON\n\n   import aws_access_advisor as access\n\n   report = access.get_report(\n      "<entity_arn>",\n      "sso"\n      sso_url="<sso_url>",\n      sso_role_name="<sso_role_name>",\n      sso_account_id="<sso_account_id>",\n    )\n   print(\n      f\'Job status: {report["JobStatus"]} after {report["processing_time"]} second(s).\'\n   )\n   print("\\n".join(access.parse(report)))\n\nIn BASH authenticating with named profiles:\n\n.. code-block:: BASH\n\n   python [/path/to/module/]aws_access_advisor \\\n   -e <entity_arn> \\\n   -m profile \\\n   -p <profile_name>\n\nIn BASH authenticating with IAM access key credentials:\n\n.. code-block:: BASH\n\n   python [/path/to/module/]aws_access_advisor \\\n   -e <entity_arn> \\\n   -m iam \\\n   -k <access_key_id> \\\n   -s <secret_access_key>\n\nIn BASH authenticating with SSO:\n\n.. code-block:: BASH\n\n   python [/path/to/module/]aws_access_advisor \\\n   -e <entity_arn> \\\n   -m sso \\\n   -a <sso_account_id> \\\n   -r <sso_role_name> \\\n   -u <sso_url>\n',
    'author': 'Ahmad Ferdaus Abd Razak',
    'author_email': 'ahmad.ferdaus.abd.razak@ni.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fer1035/pypi-aws_access_advisor',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
