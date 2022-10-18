# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numparser', 'numparser.fsm']

package_data = \
{'': ['*']}

install_requires = \
['fastnumbers>=3.2.1,<4.0.0', 'networkx>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'numparser2',
    'version': '1.0.0',
    'description': 'Parsing numbers from noisy text',
    'long_description': '# numparser\n\nParsing numbers from noisy text\n\n## Installation\n\n```bash\npip install numparser2  # not numparser\n```\n',
    'author': 'Binh Vu',
    'author_email': 'binh@toan2.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/binh-vu/numparser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
