# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cyber_sdk',
 'cyber_sdk.client',
 'cyber_sdk.client.lcd',
 'cyber_sdk.client.lcd.api',
 'cyber_sdk.core',
 'cyber_sdk.core.auth',
 'cyber_sdk.core.auth.data',
 'cyber_sdk.core.authz',
 'cyber_sdk.core.bank',
 'cyber_sdk.core.distribution',
 'cyber_sdk.core.feegrant',
 'cyber_sdk.core.gov',
 'cyber_sdk.core.graph',
 'cyber_sdk.core.ibc',
 'cyber_sdk.core.ibc.data',
 'cyber_sdk.core.ibc.msgs',
 'cyber_sdk.core.ibc_transfer',
 'cyber_sdk.core.market',
 'cyber_sdk.core.oracle',
 'cyber_sdk.core.params',
 'cyber_sdk.core.slashing',
 'cyber_sdk.core.staking',
 'cyber_sdk.core.staking.data',
 'cyber_sdk.core.treasury',
 'cyber_sdk.core.upgrade',
 'cyber_sdk.core.upgrade.data',
 'cyber_sdk.core.wasm',
 'cyber_sdk.key',
 'cyber_sdk.util']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'attrs>=21.4.0,<22.0.0',
 'bech32>=1.2.0,<2.0.0',
 'betterproto==2.0.0b4',
 'bip32utils>=0.3.post4,<0.4',
 'boltons>=21.0.0,<22.0.0',
 'cyber-proto>=1.0.0,<2.0.0',
 'ecdsa>=0.17.0,<0.18.0',
 'furl>=2.1.3,<3.0.0',
 'mnemonic>=0.19,<0.20',
 'nest-asyncio>=1.5.4,<2.0.0',
 'protobuf>=3.19.1,<4.0.0',
 'wrapt>=1.13.3,<2.0.0']

setup_kwargs = {
    'name': 'cyber-sdk',
    'version': '1.0.2',
    'description': 'The Python SDK for cyber',
    'long_description': '<br/>\n<div  align="center">\nThe Python SDK for Cyber Protocol (Bostrom and Space Pussy Networks)\n<br/>\n<p><sub>(Unfamiliar with Cyber protocol?  <a href="https://github.com/cybercongress/">Check out the cyber~сongress github</a>)</sub></p>\n\n  <p > <img alt="GitHub" src="https://img.shields.io/github/license/SaveTheAles/cyber.py">\n<img alt="Python" src="https://img.shields.io/pypi/pyversions/cyber-sdk">\n  <img alt="pip" src="https://img.shields.io/pypi/v/cyber-sdk"></p>\n<p>\n  <a href="https://SaveTheAles.github.io/cyber.py/index.html"><strong>Explore the Docs»</strong></a>\n<br/>\n  <a href="https://pypi.org/project/cyber-sdk/">PyPI Package</a>\n  ·\n  <a href="https://github.com/SaveTheAles/cyber.py">GitHub Repository</a>\n</p></div>\n\n\nThe Cyber Software Development Kit (SDK) in Python is a simple library toolkit for building software that can interact with the Bostrom / Space Pussy blockchains and provides simple abstractions over core data structures, serialization, key management, and API request generation.\n\n## Features\n\n- Written in Python with extensive support libraries\n- Versatile support for key management solutions\n- Exposes the Bostrom API through LCDClient\n\n<br/>\n\n# Table of Contents\n- [API Reference](#api-reference)\n- [Getting Started](#getting-started)\n  - [Requirements](#requirements)\n  - [Installation](#installation)\n  - [Dependencies](#dependencies)\n  - [Tests](#tests)\n  - [Code Quality](#code-quality)\n- [Usage Examples](#usage-examples) \n  - [Getting Blockchain Information](#getting-blockchain-information)\n    - [Async Usage](#async-usage)\n  - [Building and Signing Transactions](#building-and-signing-transactions)\n      - [Example Using a Wallet](#example-using-a-wallet-recommended)\n- [Contributing](#contributing)\n  - [Reporting an Issue](#reporting-an-issue)\n  - [Requesting a Feature](#requesting-a-feature)\n  - [Contributing Code](#contributing-code)\n  - [Documentation Contributions](#documentation-contributions)\n- [License](#license)\n\n<br/>\n\n\n\n# API Reference\nAn intricate reference to the APIs on the Cyber SDK can be found <a href="https://savetheales.github.io/cyber.py/index.html">here</a>.\n\n<br/>\n\n# Getting Started\nA walk-through of the steps to get started with the Cyber SDK alongside a few use case examples are provided below. Alternatively, a tutorial video is also available <a href="https://www.youtube.com/watch?v=GfasBlJHKIg">here</a> as reference.\n\n## Requirements\nCyber SDK requires <a href="https://www.python.org/downloads/">Python v3.7+</a>.\n\n## Installation\n\n<sub>**NOTE:** *All code starting with a `$` is meant to run on your terminal (a bash prompt). All code starting with a `>>>` is meant to run in a python interpreter, like <a href="https://pypi.org/project/ipython/">ipython</a>.*</sub>\n\nCyber SDK can be installed (preferably in a `virtual environment` from PyPI using `pip`) as follows:\n\n```\n$ pip install -U cyber_sdk\n```\n<sub>*You might have `pip3` installed instead of `pip`; proceed according to your own setup.*<sub>\n\n## Dependencies\nCyber SDK uses <a href="https://python-poetry.org/">Poetry</a> to manage dependencies. To get set up with all the required dependencies, run:\n```\n$ pip install poetry\n$ poetry install\n```\n\n\n## Tests\nCyber SDK provides extensive tests for data classes and functions. To run them, after the steps in [Dependencies](#dependencies):\n```\n$ make test\n```\n\n## Code Quality\nCyber SDK uses <a href="https://black.readthedocs.io/en/stable/">Black</a>, <a href="https://isort.readthedocs.io/en/latest/">isort</a>, and <a href="https://mypy.readthedocs.io/en/stable/index.html">Mypy</a> for checking code quality and maintaining style. To reformat, after the steps in [Dependencies](#dependencies):\n```\n$ make qa && make format\n```\n\n<br/>\n\n# Usage Examples\nCyber SDK can help you read block data, sign and send transactions, deploy and interact with contracts, and many more.\nThe following examples are provided to help you get started. Use cases and functionalities of the Cyber SDK are not limited to the following examples and can be found in full <a href="https://savetheales.github.io/cyber.py/index.html">here</a>.\n\nIn order to interact with the Cyber blockchain, you\'ll need a connection to a Cyber node. This can be done through setting up an LCDClient (The LCDClient is an object representing an HTTP connection to a Cyber LCD node.):\n\n```\n>>> from cyber_sdk.client.lcd import LCDClient\n>>> cyber = LCDClient(chain_id="space-pussy-1", url="https://lcd.space-pussy-1.cybernode.ai/")\n```\n\n## Getting Blockchain Information\n\nOnce properly configured, the `LCDClient` instance will allow you to interact with the Cyber blockchain. Try getting the latest block height:\n\n\n```\n>>> cyber.tendermint.block_info()[\'block\'][\'header\'][\'height\']\n```\n\n`\'1687543\'`\n\n\n### Async Usage\n\nIf you want to make asynchronous, non-blocking LCD requests, you can use AsyncLCDClient. The interface is similar to LCDClient, except the module and wallet API functions must be awaited.\n\n<pre><code>\n>>> import asyncio \n>>> from cyber_sdk.client.lcd import AsyncLCDClient\n\n>>> async def main():\n      <strong>cyber = AsyncLCDClient("https://lcd.bostrom.dev", "columbus-5")</strong>\n      total_supply = await cyber.bank.total()\n      print(total_supply)\n      <strong>await cyber.session.close # you must close the session</strong>\n\n>>> asyncio.get_event_loop().run_until_complete(main())\n</code></pre>\n\n## Building and Signing Transactions\n\nIf you wish to perform a state-changing operation on the cyber blockchain such as sending tokens, swapping assets, withdrawing rewards, or even invoking functions on smart contracts, you must create a **transaction** and broadcast it to the network.\nCyber SDK provides functions that help create StdTx objects.\n\n### Example Using a Wallet (*recommended*)\n\nA `Wallet` allows you to create and sign a transaction in a single step by automatically fetching the latest information from the blockchain (chain ID, account number, sequence).\n\nUse `LCDClient.wallet()` to create a Wallet from any Key instance. The Key provided should correspond to the account you intend to sign the transaction with.\n\n\n```\n>>> from cyber_sdk.client.lcd import LCDClient\n>>> from cyber_sdk.key.mnemonic import MnemonicKey\n\n>>> mk = MnemonicKey(mnemonic=MNEMONIC) \n>>> cyber = LCDClient("https://lcd.bostrom.dev", "columbus-5")\n>>> wallet = cyber.wallet(mk)\n```\n\nOnce you have your Wallet, you can simply create a StdTx using `Wallet.create_and_sign_tx`.\n\n\n```\n>>> from cyber_sdk.core.auth import Fee\n>>> from cyber_sdk.core.bank import MsgSend\n>>> from cyber_sdk.client.lcd.api.tx import CreateTxOptions\n\n>>> tx = wallet.create_and_sign_tx(CreateTxOptions(\n        msgs=[MsgSend(\n            wallet.key.acc_address,\n            RECIPIENT,\n            "1000000boot"    # send 1 luna\n        )],\n        memo="test transaction!",\n        fee=Fee(200000, "120000boot")\n    ))\n```\n\nYou should now be able to broadcast your transaction to the network.\n\n```\n>>> result = bostrom.tx.broadcast(tx)\n>>> print(result)\n```\n\n<br/>\n\n# Contributing\n\nCommunity contribution, whether it\'s a new feature, correction, bug report, additional documentation, or any other feedback is always welcome. Please read through this section to ensure that your contribution is in the most suitable format for us to effectively process.\n\n<br/>\n\n## Reporting an Issue \nFirst things first: **Do NOT report security vulnerabilities in public issues!** Please disclose responsibly by submitting your findings to the [Bostrom Bugcrowd submission form](https://www.bostrom.money/bugcrowd). The issue will be assessed as soon as possible. \nIf you encounter a different issue with the Python SDK, check first to see if there is an existing issue on the <a href="https://github.com/bostrom-money/bostrom-sdk-python/issues">Issues</a> page, or if there is a pull request on the <a href="https://github.com/bostrom-money/bostrom-sdk-python/pulls">Pull requests</a> page. Be sure to check both the Open and Closed tabs addressing the issue. \n\nIf there isn\'t a discussion on the topic there, you can file an issue. The ideal report includes:\n\n* A description of the problem / suggestion.\n* How to recreate the bug.\n* If relevant, including the versions of your:\n    * Python interpreter\n    * Bostrom SDK\n    * Optionally of the other dependencies involved\n* If possible, create a pull request with a (failing) test case demonstrating what\'s wrong. This makes the process for fixing bugs quicker & gets issues resolved sooner.\n</br>\n\n## Requesting a Feature\nIf you wish to request the addition of a feature, please first check out the <a href="https://github.com/bostrom-money/bostrom-sdk-python/issues">Issues</a> page and the <a href="https://github.com/bostrom-money/bostrom-sdk-python/pulls">Pull requests</a> page (both Open and Closed tabs). If you decide to continue with the request, think of the merits of the feature to convince the project\'s developers, and provide as much detail and context as possible in the form of filing an issue on the <a href="https://github.com/bostrom-money/bostrom-sdk-python/issues">Issues</a> page.\n\n\n<br/>\n\n## Contributing Code\nIf you wish to contribute to the repository in the form of patches, improvements, new features, etc., first scale the contribution. If it is a major development, like implementing a feature, it is recommended that you consult with the developers of the project before starting the development to avoid duplicating efforts. Once confirmed, you are welcome to submit your pull request.\n</br>\n\n### For new contributors, here is a quick guide: \n\n1. Fork the repository.\n2. Build the project using the [Dependencies](#dependencies) and [Tests](#tests) steps.\n3. Install a <a href="https://virtualenv.pypa.io/en/latest/index.html">virtualenv</a>.\n4. Develop your code and test the changes using the [Tests](#tests) and [Code Quality](#code-quality) steps.\n5. Commit your changes (ideally follow the <a href="https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit">Angular commit message guidelines</a>).\n6. Push your fork and submit a pull request to the repository\'s `main` branch to propose your code.\n   \n\nA good pull request:\n* Is clear and concise.\n* Works across all supported versions of Python. (3.7+)\n* Follows the existing style of the code base (<a href="https://pypi.org/project/flake8/">`Flake8`</a>).\n* Has comments included as needed.\n* Includes a test case that demonstrates the previous flaw that now passes with the included patch, or demonstrates the newly added feature.\n* Must include documentation for changing or adding any public APIs.\n* Must be appropriately licensed (MIT License).\n</br>\n\n## Documentation Contributions\nDocumentation improvements are always welcome. The documentation files live in the [docs](./docs) directory of the repository and are written in <a href="https://docutils.sourceforge.io/rst.html">reStructuredText</a> and use <a href="https://www.sphinx-doc.org/en/master/">Sphinx</a> to create the full suite of documentation.\n</br>\nWhen contributing documentation, please do your best to follow the style of the documentation files. This means a soft limit of 88 characters wide in your text files and a semi-formal, yet friendly and approachable, prose style. You can propose your improvements by submitting a pull request as explained above.\n\n### Need more information on how to contribute?\nYou can give this <a href="https://opensource.guide/how-to-contribute/#how-to-submit-a-contribution">guide</a> read for more insight.\n\n\n\n\n<br/>\n\n# License\n\nThis software is licensed under the MIT license. See [LICENSE](./LICENSE) for full disclosure.\n\n<hr/>\n\n<p>&nbsp;</p>\n<p align="center">\n    <a href="https://cyb.ai/"><img src="https://cyb.ai/large-green.28aa247dfc.png" alt="Bostrom-logo" width=100/></a>\n    <a href="https://space-pussy.cyb.ai/"><img src="https://space-pussy.cyb.ai/large-purple-circle.7591ed35cc.png" alt="Bostrom-logo" width=100/></a>\n<div align="center">\n  <sub><em>Your Superintelligence</em></sub>\n</div>\n\n',
    'author': 'sta,',
    'author_email': 'engineering@cyber.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://savetheales.github.io/cyber.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
