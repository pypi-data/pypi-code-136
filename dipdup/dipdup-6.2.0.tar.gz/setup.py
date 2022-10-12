# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dipdup',
 'dipdup.datasources',
 'dipdup.datasources.coinbase',
 'dipdup.datasources.ipfs',
 'dipdup.datasources.metadata',
 'dipdup.datasources.tzkt',
 'dipdup.utils']

package_data = \
{'': ['*'],
 'dipdup': ['configs/*',
            'projects/base/*',
            'projects/base/src/{{cookiecutter.package}}/*',
            'projects/base/tests/test_{{cookiecutter.package}}/*',
            'projects/blank/*',
            'projects/demo_domains/*',
            'projects/demo_domains/src/{{cookiecutter.package}}/*',
            'projects/demo_domains/src/{{cookiecutter.package}}/handlers/*',
            'projects/demo_domains_big_map/*',
            'projects/demo_domains_big_map/src/{{cookiecutter.package}}/*',
            'projects/demo_domains_big_map/src/{{cookiecutter.package}}/handlers/*',
            'projects/demo_events/*',
            'projects/demo_head/*',
            'projects/demo_hic_et_nunc/*',
            'projects/demo_hic_et_nunc/src/{{cookiecutter.package}}/*',
            'projects/demo_hic_et_nunc/src/{{cookiecutter.package}}/handlers/*',
            'projects/demo_quipuswap/*',
            'projects/demo_quipuswap/src/{{cookiecutter.package}}/*',
            'projects/demo_quipuswap/src/{{cookiecutter.package}}/handlers/*',
            'projects/demo_registrydao/*',
            'projects/demo_registrydao/src/{{cookiecutter.package}}/*',
            'projects/demo_registrydao/src/{{cookiecutter.package}}/handlers/*',
            'projects/demo_registrydao/src/{{cookiecutter.package}}/types/*',
            'projects/demo_registrydao/src/{{cookiecutter.package}}/types/registry/*',
            'projects/demo_registrydao/src/{{cookiecutter.package}}/types/registry/parameter/*',
            'projects/demo_tzbtc/*',
            'projects/demo_tzbtc/src/{{cookiecutter.package}}/*',
            'projects/demo_tzbtc/src/{{cookiecutter.package}}/handlers/*',
            'projects/demo_tzbtc_transfers/*',
            'projects/demo_tzbtc_transfers/src/{{cookiecutter.package}}/*',
            'projects/demo_tzbtc_transfers/src/{{cookiecutter.package}}/handlers/*',
            'projects/demo_tzcolors/*',
            'projects/demo_tzcolors/src/{{cookiecutter.package}}/*',
            'projects/demo_tzcolors/src/{{cookiecutter.package}}/handlers/*',
            'projects/linters_advanced/*',
            'projects/linters_default/*',
            'projects/linters_none/*',
            'sql/on_reindex/*',
            'templates/*']}

install_requires = \
['APScheduler>=3.8.0,<4.0.0',
 'aiohttp>=3.8.1,<4.0.0',
 'aiolimiter>=1.0.0-beta.1,<2.0.0',
 'anyio>=3.3.2,<4.0.0',
 'asyncclick>=8.0.1,<9.0.0',
 'asyncpg==0.26.0',
 'datamodel-code-generator==0.13.1',
 'orjson>=3.6.6,<4.0.0',
 'prometheus-client>=0.14.1,<0.15.0',
 'pydantic==1.9.2',
 'pyhumps>=3.0.2,<4.0.0',
 'pysignalr==0.1.2',
 'python-dotenv>=0.19.0,<0.20.0',
 'ruamel.yaml>=0.17.2,<0.18.0',
 'sentry-sdk>=1.4.3,<2.0.0',
 'sqlparse>=0.4.2,<0.5.0',
 'tabulate>=0.8.9,<0.9.0',
 'tortoise-orm==0.19.2']

extras_require = \
{'pytezos': ['pytezos==3.7.0']}

entry_points = \
{'console_scripts': ['dipdup = dipdup.cli:cli',
                     'dipdup-install = dipdup.install:cli']}

setup_kwargs = {
    'name': 'dipdup',
    'version': '6.2.0',
    'description': 'Python SDK for developing indexers of Tezos smart contracts inspired by The Graph',
    'long_description': '[![GitHub stars](https://img.shields.io/github/stars/dipdup-net/dipdup?color=2c2c2c)](https://github.com/dipdup-net/dipdup)\n[![Latest stable release](https://img.shields.io/github/v/release/dipdup-net/dipdup?label=stable%20release&color=2c2c2c)](https://github.com/dipdup-net/dipdup/releases)\n[![Latest pre-release)](https://img.shields.io/github/v/release/dipdup-net/dipdup?include_prereleases&label=latest%20release&color=2c2c2c)](https://github.com/dipdup-net/dipdup/releases)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dipdup?color=2c2c2c)](https://www.python.org)\n[![License: MIT](https://img.shields.io/github/license/dipdup-net/dipdup?color=2c2c2c)](https://github.com/dipdup-net/dipdup/blob/master/LICENSE)\n<br>\n[![PyPI monthly downloads](https://img.shields.io/pypi/dm/dipdup?color=2c2c2c)](https://pypi.org/project/dipdup/)\n[![GitHub issues](https://img.shields.io/github/issues/dipdup-net/dipdup?color=2c2c2c)](https://github.com/dipdup-net/dipdup/issues)\n[![GitHub pull requests](https://img.shields.io/github/issues-pr/dipdup-net/dipdup?color=2c2c2c)](https://github.com/dipdup-net/dipdup/pulls)\n[![GitHub Discussions](https://img.shields.io/github/discussions/dipdup-net/dipdup?color=2c2c2c)](https://github.com/dipdup-net/dipdup/discussions)\n\n```text\n        ____   _         ____              \n       / __ \\ (_)____   / __ \\ __  __ ____ \n      / / / // // __ \\ / / / // / / // __ \\\n     / /_/ // // /_/ // /_/ // /_/ // /_/ /\n    /_____//_// .___//_____/ \\__,_// .___/ \n             /_/                  /_/      \n```\n\nDipDup is a Python framework for building smart contract indexers. It helps developers focus on business logic instead of writing a boilerplate to store and serve data. DipDup-based indexers are selective, which means only required data is requested. This approach allows to achieve faster indexing times and decreased load on underlying APIs.\n\n* **Ready to build your first indexer?** Head to [Quickstart](https://docs.dipdup.io/quickstart).\n\n* **Looking for examples?** Check out [Demo Projects](https://docs.dipdup.io/examples/demo-projects) and [Built with DipDup](https://docs.dipdup.io/examples/built-with-dipdup) pages.\n\n* **Want to participate?** Vote for [open issues](https://github.com/dipdup-net/dipdup/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc), join [discussions](https://github.com/dipdup-net/dipdup/discussions) or [become a sponsor](https://github.com/sponsors/dipdup-net).\n\n* **Have a question?** Contact us on [Discord](https://discord.com/invite/RcPGSdcVSx), [Telegram](https://t.me/baking_bad_chat), or [Slack](https://tezos-dev.slack.com/archives/CV5NX7F2L)!\n\nThis project is maintained by the [Baking Bad](https://bakingbad.dev/) team.\n<br>\nDevelopment is supported by [Tezos Foundation](https://tezos.foundation/).\n',
    'author': 'Lev Gorodetskiy',
    'author_email': 'github@droserasprout.space',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://dipdup.io/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
