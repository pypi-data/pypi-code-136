# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_authenticator']

package_data = \
{'': ['*']}

install_requires = \
['aws-ssooidc>=2021.1.1.1,<2022.0.0.0', 'boto3>=1.17.78,<2.0.0']

setup_kwargs = {
    'name': 'aws-authenticator',
    'version': '2022.10.1.0',
    'description': 'Login to AWS using CLI named profiles, IAM access key credentials, or SSO.',
    'long_description': '=====================\n**aws-authenticator**\n=====================\n\nOverview\n--------\n\nLogin to AWS using CLI named profiles, IAM access key credentials, or SSO.\n\nPrerequisites\n-------------\n\n- *Python >= 3.6*\n- *aws-ssooidc (https://pypi.org/project/aws-ssooidc/) >= 2021.1.1.1*\n- *boto3 (https://pypi.org/project/boto3/) >= 1.17.78*\n\nConditional Arguments\n---------------------\n\nIf authenticating with named profiles:\n\n- AWSCLI profile name\n\nIf authenticating with IAM acccess key credentials:\n\n- AWS access key id\n- AWS secret access key\n\nIf authenticating with SSO:\n\n- AWS account ID\n- AWS SSO Permission Set (role) name\n- AWS SSO login URL\n\nUsage\n-----\n\nInstallation:\n\n.. code-block:: BASH\n\n   pip3 install aws-authenticator\n   # or\n   python3 -m pip install aws-authenticator\n\nIn Python3 authenticating with named profiles:\n\n.. code-block:: PYTHON\n\n   import aws_authenticator\n\n   auth = aws_authenticator.AWSAuthenticator(\n      profile_name="<profile-name>",\n   )\n   session = auth.profile()\n   client = session.client("<client-name>")\n\nIn Python3 authenticating with IAM access key credentials:\n\n.. code-block:: PYTHON\n\n   import aws_authenticator\n\n   auth = aws_authenticator.AWSAuthenticator(\n      access_key_id="<access-key-id>",\n      secret_access_key="<secret-access-key>",\n   )\n   session = auth.iam()\n   client = session.client("<client-name>")\n\nIn Python3 authenticating with SSO:\n\n.. code-block:: PYTHON\n\n   import aws_authenticator\n\n   auth = aws_authenticator.AWSAuthenticator(\n      sso_url="<sso-url>",\n      sso_role_name="<sso-role-name>",\n      ssp_account_id="<ssp-account-id>",\n   )\n   session = auth.sso()\n   client = session.client("<client-name>")\n\nTesting profile-based login as a script in BASH:\n\n.. code-block:: BASH\n\n   python [/path/to/]aws_authenticator \\\n   -m profile \\\n   -p <profile-name>\n',
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
