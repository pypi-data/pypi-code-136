# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_access_advisor']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.78,<2.0.0']

setup_kwargs = {
    'name': 'aws-access-advisor',
    'version': '2022.10.1.1',
    'description': 'Generate IAM actions list from AWS Access Advisor reports.',
    'long_description': '======================\n**aws_access_advisor**\n======================\n\nOverview\n--------\n\nGenerate IAM actions list from AWS Access Advisor reports.\n\nPrerequisites\n-------------\n\n- *Python >= 3.6*\n- *aws_ssooidc >= 2021.1.1.1* (installed as a dependency)\n- *boto3 >= 1.17.78* (installed as a dependency)\n\nRequired Arguments\n------------------\n\n- AWS account ID\n- AWS entity ARN (role, user, etc. to use for report generation)\n- AWS SSO Permission Set name for login purposes\n- AWS SSO login URL\n\nUsage\n-----\n\nInstallation:\n\n.. code-block:: BASH\n\n   pip3 install aws_access_advisor\n   # or\n   python3 -m pip install aws_access_advisor\n\nIn Python3:\n\n.. code-block:: BASH\n\n   import <file_name_without_.py>\n   auth = <file_name_without_.py>.login("<account_id>", "<sso_url>", "<admin_role_name>")\n   report = <file_nafile_name_without_.pyme>.get_report(\n      "<entity_role_arn>",\n      auth["roleCredentials"]["accessKeyId"],\n      auth["roleCredentials"]["secretAccessKey"],\n      auth["roleCredentials"]["sessionToken"]\n   )\n   print(\n      f\'Job status: {report["JobStatus"]} after {report["processing_time"]} second(s).\'\n   )\n   for obj in report["ServicesLastAccessed"]:\n      if "LastAuthenticatedEntity" in obj:\n         try:\n               for obj_in in obj["TrackedActionsLastAccessed"]:\n                  if "LastAccessedEntity" in obj_in:\n                     print(f\'"{obj["ServiceNamespace"]}:{obj_in["ActionName"]}",\')\n         except Exception as e:\n               print(f\'"{obj["ServiceNamespace"]}:*",\')\n\nIn BASH:\n\n.. code-block:: BASH\n\n   python <file_name_with_.py> \\\n   -a <account_id> \\\n   -e <entity_role_arn> \\\n   -r <admin_role_name> \\  # [OPTIONAL]\n   -u <sso_url> \\  # [OPTIONAL]\n   > <output_path>\n',
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
