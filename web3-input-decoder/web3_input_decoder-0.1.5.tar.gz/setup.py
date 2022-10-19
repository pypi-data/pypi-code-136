# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['web3_input_decoder']

package_data = \
{'': ['*']}

install_requires = \
['eth-abi>=3.0.0,<4.0.0',
 'eth-utils>=2.0.0,<3.0.0',
 'pycryptodome>=3.15.0,<4.0.0']

setup_kwargs = {
    'name': 'web3-input-decoder',
    'version': '0.1.5',
    'description': 'A simple offline web3 transaction input decoder for functions and constructors',
    'long_description': '# web3-input-decoder\n\n[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6f10d5104ef4464797ee94b17c7b9371)](https://www.codacy.com/gh/kigawas/web3-input-decoder/dashboard)\n[![CI](https://img.shields.io/github/workflow/status/kigawas/web3-input-decoder/Build)](https://github.com/kigawas/web3-input-decoder/actions)\n[![Codecov](https://img.shields.io/codecov/c/github/kigawas/web3-input-decoder.svg)](https://codecov.io/gh/kigawas/web3-input-decoder)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/web3-input-decoder.svg)](https://pypi.org/project/web3-input-decoder/)\n[![PyPI](https://img.shields.io/pypi/v/web3-input-decoder.svg)](https://pypi.org/project/web3-input-decoder/)\n[![License](https://img.shields.io/github/license/kigawas/web3-input-decoder.svg)](https://github.com/kigawas/web3-input-decoder)\n\nA simple offline web3 transaction input decoder for functions and constructors.\n\n## Install\n\n```bash\npip install web3-input-decoder\n```\n\n## Quick start\n\nLet\'s take a [USDT transfer transaction](https://etherscan.io/tx/0x0331fdfa070ee26b1fc7b01b246ef5e58593cbe9f4a02f7f09bf4a2aa640cf35) and the [USDT contract creator transaction](https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7#code) as an example:\n\n```python\n>>> import json\n>>> import urllib.request\n>>> from web3_input_decoder import decode_constructor, decode_function\n>>> f = urllib.request.urlopen("https://api.etherscan.io/api?module=contract&action=getabi&address=0xdac17f958d2ee523a2206206994597c13d831ec7")\n>>> TETHER_ABI = json.loads(json.load(f)["result"])\n>>> decode_function(\n        TETHER_ABI, "0xa9059cbb000000000000000000000000f050227be1a7ce587aa83d5013f900dbc3be0611000000000000000000000000000000000000000000000000000000000ecdd350",\n    )\n[(\'address\', \'_to\', \'0xf050227be1a7ce587aa83d5013f900dbc3be0611\'),\n (\'uint256\', \'_value\', 248370000)]\n>>> decode_constructor(\n        TETHER_ABI, "000000000000000000000000000000000000000000000000000000174876e800000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000a546574686572205553440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000045553445400000000000000000000000000000000000000000000000000000000"\n    )\n[(\'uint256\', \'_initialSupply\', 100000000000),\n (\'string\', \'_name\', \'Tether USD\'),\n (\'string\', \'_symbol\', \'USDT\'),\n (\'uint256\', \'_decimals\', 6)]\n```\n\nYou can also play with it [here](https://replit.com/@kigawas/Web3-input-decoder-quick-start).\n\n### Performance enhancement\n\nIf you have lots of inputs in the same contract to decode, consider using [`InputDecoder`](web3_input_decoder/decoder.py#L22).\n\n```python\n>>> from web3_input_decoder import InputDecoder\n>>> decoder = InputDecoder(TETHER_ABI)\n>>> for _ in range(10000):\n>>>    decoder.decode_function(\n          (\n            "0xa9059cbb000000000000000000000000f050227be1a7ce587aa83d5013f900dbc3b"\n            "e0611000000000000000000000000000000000000000000000000000000000ecdd350"\n          ),\n        )\n```\n\n## API\n\n- [`decode_constructor`](web3_input_decoder/__init__.py#L11)\n\n  ```python\n  def decode_constructor(\n      abi: List[dict],\n      tx_input: Union[str, bytes],\n      bytecode: Optional[Union[str, bytes]] = None,\n  ) -> List[Tuple[str, str, Any]]\n  ```\n\n  **Parameters**:\n\n  - `abi`: Contract ABI\n  - `tx_input`: Transaction input to decode, with or without deployed contract bytecode\n  - `bytecode`: Optional deployed contract bytecode. If this is set, `tx_input` should include bytecode\n\n  **Returns**:\n\n  - `List[Tuple[str, str, Any]]`: Decoded type-name-value tuples\n\n- [`decode_function`](web3_input_decoder/__init__.py#L36)\n\n  ```python\n  def decode_function(\n      abi: List[dict], tx_input: Union[str, bytes]\n  ) -> List[Tuple[str, str, Any]]\n  ```\n\n  **Parameters**:\n\n  - `abi`: Contract ABI\n  - `tx_input`: Transaction input to decode\n\n  **Returns**:\n\n  - `List[Tuple[str, str, Any]]`: Decoded type-name-value tuples\n\n## Rationale\n\nExisting solutions are not satisfying to me, e.g.:\n\n1. [web3py](https://web3py.readthedocs.io/en/stable/contracts.html#web3.contract.Contract.decode_function_input) can only decode function calls and it\'s necessary to be online to set up a provider first.\n2. [ethereum-input-decoder](https://github.com/tintinweb/ethereum-input-decoder) is not actively maintained and it contains several glitches.\n',
    'author': 'Weiliang Li',
    'author_email': 'to.be.impressive@gmail.com',
    'maintainer': 'Weiliang Li',
    'maintainer_email': 'to.be.impressive@gmail.com',
    'url': 'https://github.com/kigawas/web3-input-decoder',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
