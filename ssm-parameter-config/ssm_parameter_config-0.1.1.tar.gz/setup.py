# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ssm_parameter_config']

package_data = \
{'': ['*']}

install_requires = \
['boto3',
 'botocore',
 'pydantic',
 'python-dotenv',
 'ruamel.yaml',
 'signed-pickle>=1']

setup_kwargs = {
    'name': 'ssm-parameter-config',
    'version': '0.1.1',
    'description': 'Description',
    'long_description': '# Ssm Parameter Config\n\n[![Checks][checks-shield]][checks-url]\n[![Codecov][codecov-shield]][codecov-url]\n\n\n\n[codecov-shield]: https://img.shields.io/codecov/c/github/mumblepins/ssm-parameter-config\n[codecov-url]: https://app.codecov.io/gh/mumblepins/ssm-parameter-config\n\n[checks-shield]: https://img.shields.io/github/workflow/status/mumblepins/ssm-parameter-config/Python%20Publish?style=flat-square\n[checks-url]: https://github.com/mumblepins/ssm-parameter-config/actions/workflows/python-publish.yml\n',
    'author': 'Daniel Sullivan',
    'author_email': 'daniel.j.sullivan@state.mn.us',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mumblepins/ssm-parameter-config/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
