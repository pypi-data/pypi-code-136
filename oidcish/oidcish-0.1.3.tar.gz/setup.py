# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['oidcish']

package_data = \
{'': ['*']}

install_requires = \
['StrEnum>=0.4.8,<0.5.0',
 'background>=0.2.1,<0.3.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'cryptography>=38.0.2,<39.0.0',
 'httpx>=0.23.0,<0.24.0',
 'pendulum>=2.1.2,<3.0.0',
 'pkce>=1.0.3,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'python-jose>=3.3.0,<4.0.0']

setup_kwargs = {
    'name': 'oidcish',
    'version': '0.1.3',
    'description': 'Obtain authentication tokens from OIDC providers.',
    'long_description': '# oidcish\n\n- "Oh I Don\'t Care If Something Happens"\n- "OIDC Is Definitely Cool If Someone Helps"\n\n## What?\n\nLibrary to connect to your OIDC provider via:\n\n- Authentication code flow\n- Device code flow\n\n## Usage\n\n```python\n>>> from oidcish import DeviceFlow, CodeFlow\n>>> auth = DeviceFlow(host="https://example.idp.com")\nVisit https://idp.example.com/device?userCode=594658190 to complete sign-in.\n# Or\n# auth = CodeFlow(host="https://example.idp.com")\n>>> print(auth.credentials.access_token)\neyJhbGciOiJSU...\n```\n\n## Options\n\nDevice flow can be used with the following options:\n\n| Option | Default | Description |\n|-|-|-|\n| client_id | *No default* | The client id. |\n| client_secret | *No default* | The client secret. |\n| scope | openid profile offline_access | A space separated, case-sensitive list of scopes. |\n| audience | *No default* | The access claim was designated for this audience. |\n\nCode flow can be used with the following options:\n\n| Option | Default | Description |\n|-|-|-|\n| client_id | *No default* | The client id. |\n| client_secret | *No default* | The client secret. |\n| redirect_uri | http://localhost | Must exactly match one of the allowed redirect URIs for the client. |\n| username | *No default* | The user name. |\n| password | *No default* | The user password. |\n| scope | openid profile offline_access | A space separated, case-sensitive list of scopes. |\n| audience | *No default* | The access claim was designated for this audience. |\n',
    'author': 'Erik G. Brandt',
    'author_email': 'erik.brandt@shaarpec.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
