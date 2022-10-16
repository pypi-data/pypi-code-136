# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['eth', 'eth.codecs', 'eth.codecs.abi']

package_data = \
{'': ['*']}

install_requires = \
['pysha3>=1.0.2,<2.0.0']

setup_kwargs = {
    'name': 'eth-stdlib',
    'version': '0.2.2',
    'description': 'Ethereum Standard Library for Python',
    'long_description': '# The Ethereum Standard Library\n\n[![GitHub](https://img.shields.io/github/license/skellet0r/eth-stdlib)](https://github.com/skellet0r/eth-stdlib/blob/master/COPYING)\n[![Codecov](https://img.shields.io/codecov/c/github/skellet0r/eth-stdlib)](https://app.codecov.io/gh/skellet0r/eth-stdlib)\n[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/skellet0r/eth-stdlib/test?label=test%20suite)](https://github.com/skellet0r/eth-stdlib/actions/workflows/test.yaml)\n[![Read the Docs](https://img.shields.io/readthedocs/eth-stdlib)](https://eth-stdlib.readthedocs.io/en/latest/)\n[![PyPI](https://img.shields.io/pypi/v/eth-stdlib)](https://pypi.org/project/eth-stdlib/)\n\nThe Ethereum Standard Library is a collection of libraries for developers building on the EVM.\n\n## Installation\n\n### Using pip\n\n```bash\n$ pip install eth-stdlib\n```\n\n### Using poetry\n\n```bash\n$ poetry add eth-stdlib\n```\n\n## Development\n\n### Initializing an Environment\n\nTo start developing/contributing to the eth-stdlib code base follow these steps:\n\n1. Install [poetry](https://python-poetry.org/)\n\n   ```bash\n   $ pipx install poetry\n   ```\n\n2. Clone the eth-stdlib repository\n\n   ```bash\n   $ git clone https://github.com/skellet0r/eth-stdlib.git\n   ```\n\n3. Initialize virtual environment\n\n   ```bash\n   $ poetry install --sync\n   ```\n\nAfterwards the development environment will be complete.\n\n### Testing\n\nTo run the test suite, execute the following command:available in the `html\n\n```bash\n$ poetry run pytest\n```\n\nAfter running the test suite, code coverage results will be displayed in the terminal, as well as exported in html format (in the `htmlcov` directory).\n',
    'author': 'Edward Amor',
    'author_email': 'edward.amor3@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/skellet0r/eth-stdlib',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
