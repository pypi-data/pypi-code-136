# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['doccano_client',
 'doccano_client.beta',
 'doccano_client.beta.controllers',
 'doccano_client.beta.models',
 'doccano_client.beta.tests',
 'doccano_client.beta.tests.controllers',
 'doccano_client.beta.tests.controllers.mock_api_responses',
 'doccano_client.beta.tests.utils',
 'doccano_client.beta.utils',
 'doccano_client.cli',
 'doccano_client.models',
 'doccano_client.repositories',
 'doccano_client.services',
 'doccano_client.usecase']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.7,<0.6.0',
 'pydantic>=1.9.2,<2.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.28.1,<3.0.0']

extras_require = \
{':extra == "whisper"': ['ffmpeg-python[whisper]>=0.2.0,<0.3.0'],
 'spacy': ['spacy>=3.4.1,<4.0.0',
           'spacy-partial-tagger>=0.9.1,<0.10.0',
           'tqdm>=4.64.1,<5.0.0'],
 'whisper': ['tqdm>=4.64.1,<5.0.0']}

entry_points = \
{'console_scripts': ['docli = doccano_client.cli.commands:main']}

setup_kwargs = {
    'name': 'doccano-client',
    'version': '1.2.2',
    'description': 'A simple client for doccano API.',
    'long_description': "# doccano client\n\n[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cf90190126b948e09362048b63600b06)](https://www.codacy.com/gh/doccano/doccano-client/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=doccano/doccano-client&amp;utm_campaign=Badge_Grade) [![Tests](https://github.com/doccano/doccano-client/actions/workflows/ci.yml/badge.svg)](https://github.com/doccano/doccano-client/actions/workflows/ci.yml)\n\nA simple client for the doccano API.\n\n## Installation\n\nTo install `doccano-client`, simply run:\n\n```bash\npip install doccano-client\n```\n\n## Usage\n\n```python\nfrom doccano_client import DoccanoClient\n\n# instantiate a client and log in to a Doccano instance\nclient = DoccanoClient('http://doccano.example.com')\nclient.login(username='username', password='password')\n\n# get basic information about the authorized user\nuser = client.get_profile()\n\n# list all projects\nprojects = client.list_projects()\n```\n\nPlease see the [documentation](https://doccano.github.io/doccano-client/) for further details.\n\n## Doccano API BETA Client\n\nWe're introducing a newly revamped Doccano API Client that features more Pythonic interaction as well as more testing and documentation. It also adds more regulated compatibility with specific Doccano release versions.\n\nYou can find the documentation on usage of the beta client [here](doccano_client/beta/README.md).\n",
    'author': 'Hironsan',
    'author_email': 'hiroki.nakayama.py@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/doccano/doccano-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
