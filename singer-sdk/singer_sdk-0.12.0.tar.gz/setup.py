# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['singer_sdk',
 'singer_sdk._singerlib',
 'singer_sdk.cli',
 'singer_sdk.configuration',
 'singer_sdk.helpers',
 'singer_sdk.sinks',
 'singer_sdk.streams']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.4,<3.0',
 'PyYAML>=6.0,<7.0',
 'backoff>=2.0.0,<3.0',
 'click>=8.0,<9.0',
 'cryptography>=3.4.6,<39.0.0',
 'fs>=2.4.16,<3.0.0',
 'inflection>=0.5.1,<0.6.0',
 'joblib>=1.0.1,<2.0.0',
 'jsonpath-ng>=1.5.3,<2.0.0',
 'jsonschema>=4.16.0,<5.0.0',
 'memoization>=0.3.2,<0.5.0',
 'pendulum>=2.1.0,<3.0.0',
 'python-dotenv>=0.20,<0.22',
 'pytz>=2022.2.1,<2023.0.0',
 'requests>=2.25.1,<3.0.0',
 'simplejson>=3.17.6,<4.0.0',
 'sqlalchemy>=1.4,<2.0',
 'typing-extensions>=4.2.0,<5.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'],
 ':python_version < "3.9"': ['importlib-resources>=5.9.0,<6.0.0'],
 'docs': ['sphinx>=4.5,<6.0',
          'sphinx-rtd-theme>=0.5.2,<1.1.0',
          'sphinx-copybutton>=0.3.1,<0.6.0',
          'myst-parser>=0.17.2,<0.19.0',
          'sphinx-autobuild>=2021.3.14,<2022.0.0']}

setup_kwargs = {
    'name': 'singer-sdk',
    'version': '0.12.0',
    'description': 'A framework for building Singer taps',
    'long_description': "# Meltano Singer SDK\n\n[![Python Versions](https://img.shields.io/pypi/pyversions/singer-sdk)](https://pypi.org/project/singer-sdk)\n[![Downloads](https://img.shields.io/pypi/dw/singer-sdk?color=blue)](https://pypi.org/project/singer-sdk)\n[![PyPI Version](https://img.shields.io/pypi/v/singer-sdk?color=blue)](https://pypi.org/project/singer-sdk)\n[![Documentation Status](https://readthedocs.org/projects/meltano-sdk/badge/?version=latest)](https://sdk.meltano.com/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/meltano/sdk/branch/main/graph/badge.svg?token=kS1zkemAgo)](https://codecov.io/gh/meltano/sdk)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/meltano/sdk/main.svg)](https://results.pre-commit.ci/latest/github/meltano/sdk/main)\n\nThe Tap and Target SDKs are the fastest way to build custom data extractors and loaders!\nTaps and targets built on the SDK are automatically compliant with the\n[Singer Spec](https://hub.meltano.com/singer/spec), the\nde-facto open source standard for extract and load pipelines.\n\n## Future-proof extractors and loaders, with less code\n\nOn average, developers tell us that they write about 70% less code by using the SDK, which\nmakes learning the SDK a great investment. Furthermore, as new features and capabilities\nare added to the SDK, your taps and targets can always take advantage of the latest\ncapabilities and bug fixes, simply by updating your SDK dependency to the latest version.\n\n## Meltano\n\n*Not familiar with Meltano?*  [Meltano](https://docs.meltano.com/getting-started/meltano-at-a-glance) is your CLI for ELT+ that:\n\n- **Starts simple**: Meltano is pip-installable and comes in a prepackaged docker container, you can have your first ELT pipeline running within minutes.\n- **Has DataOps out-of-the-box**: Meltano provides tools that make DataOps best practices easy to use in every project.\n- **Integrates with everything**: 300+ natively supported data sources & targets, as well as additional plugins like great expectations or dbt are natively available.\n- **Is easily customizable**: Meltano isn't just extensible, it's built to be extended! The Singer SDK (for Connectors) & EDK (for Meltano Components) are easy to use. Meltano Hub helps you find all of the connectors and components created across the data community.\n- **Is a mature system**: Developed since 2018, runs in production at large companies like GitLab, and currently powers over a million pipeline runs monthly.\n- **Has first class ELT tooling built-in**: Extract data from any data source, load into any target, use inline maps to transform on data on the fly, and test the incoming data, all in one package.\n\nIf you want to get started with Meltano, we suggest you:\n- head over to the [Installation](https://docs.meltano.com/getting-started/installation)\n- or if you have it installed, go through the [Meltano Tutorial](https://docs.meltano.com/getting-started/part1).\n\n## Documentation\n\n- See our [online documentation](https://sdk.meltano.com) for instructions on how\nto get started with the SDK.\n\n## Contributing back to the SDK\n\n- For more information on how to contribute, see our [Contributors Guide](https://sdk.meltano.com/en/latest/CONTRIBUTING.html).\n\n## Making a new release of the SDK\n\n1. Trigger a version bump [using the GitHub web UI](https://github.com/edgarrmondragon/sdk/actions/workflows/version_bump.yml) or the cli:\n\n   ```console\n   $ gh workflow run\n   ```\n\n   The `increment: auto` option will figure out the most appropriate bump based on commit history.\n\n1. Follow the checklist in the PR description.\n\n1. Publish a new release [using the GitHub web UI](https://github.com/meltano/sdk/releases/new).\n",
    'author': 'Meltano Team and Contributors',
    'author_email': 'None',
    'maintainer': 'Meltano Team and Contributors',
    'maintainer_email': 'None',
    'url': 'https://sdk.meltano.com/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
