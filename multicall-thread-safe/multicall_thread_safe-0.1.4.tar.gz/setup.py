# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multicall_thread_safe']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.8,<23.0',
 'flake8>=5.0,<6.0',
 'joblib>=1.2,<2.0',
 'pytest>=7.1,<8.0']

setup_kwargs = {
    'name': 'multicall-thread-safe',
    'version': '0.1.4',
    'description': 'Thread Safe Multicall for execution in containerised environments, tweaked from https://github.com/banteg/multicall.py',
    'long_description': "# multicall.py\npython interface for makerdao's [multicall](https://github.com/makerdao/multicall) and a port of [multicall.js](https://github.com/makerdao/multicall.js).\n\nThis fork supports multithreading/processing in dockerized env which breaks with original module, by disabling Async execution of w3 requests. \n\nTo enable threaded/parallel execution with docker set env variable ASYNC_W3=0.\n\n## installation\n\n```\npip install multicall\n```\n\n## example\n\n```python\nfrom multicall import Call, Multicall\n\n# assuming you are on kovan\nMKR_TOKEN = '0xaaf64bfcc32d0f15873a02163e7e500671a4ffcd'\nMKR_WHALE = '0xdb33dfd3d61308c33c63209845dad3e6bfb2c674'\nMKR_FISH = '0x2dfcedcb401557354d0cf174876ab17bfd6f4efd'\n\ndef from_wei(value):\n    return value / 1e18\n\nmulti = Multicall([\n    Call(MKR_TOKEN, ['balanceOf(address)(uint256)', MKR_WHALE], [['whale', from_wei]]),\n    Call(MKR_TOKEN, ['balanceOf(address)(uint256)', MKR_FISH], [['fish', from_wei]]),\n    Call(MKR_TOKEN, 'totalSupply()(uint256)', [['supply', from_wei]]),\n])\n\nmulti()  # {'whale': 566437.0921992733, 'fish': 7005.0, 'supply': 1000003.1220798912}\n\n# seth-style calls\nCall(MKR_TOKEN, ['balanceOf(address)(uint256)', MKR_WHALE])()\nCall(MKR_TOKEN, 'balanceOf(address)(uint256)')(MKR_WHALE)\n# return values processing\nCall(MKR_TOKEN, 'totalSupply()(uint256)', [['supply', from_wei]])()\n```\n\nfor a full example, see implementation of [daistats](https://github.com/banteg/multicall.py/blob/master/examples/daistats.py).\noriginal [daistats.com](https://daistats.com) made by [nanexcool](https://github.com/nanexcool/daistats).\n\n## api\n\n### `Signature(signature)`\n\n- `signature` is a seth-style function signature of `function_name(input,types)(output,types)`. it also supports structs which need to be broken down to basic parts, e.g. `(address,bytes)[]`.\n\nuse `encode_data(args)` with input args to get the calldata. use `decode_data(output)` with the output to decode the result.\n\n### `Call(target, function, returns)`\n\n- `target` is the `to` address which is supplied to `eth_call`.\n- `function` can be either seth-style signature of `method(input,types)(output,types)` or a list of `[signature, *args]`.\n- `returns` is a list of `[name, handler]` for return values. if `returns` argument is omitted, you get a tuple, otherwise you get a dict. to skip processing of a value, pass `None` as a handler.\n\nuse `Call(...)()` with predefined args or `Call(...)(args)` to reuse a prepared call with different args.\n\nuse `decode_output(output)` with to decode the output and process it with `returns` handlers.\n\n### `Multicall(calls)`\n\n- `calls` is a list of calls with prepared values.\n\nuse `Multicall(...)()` to get the result of a prepared multicall.\n\n### Environment Variables\n\n- GAS_LIMIT: sets overridable default gas limit for Multicall to prevent out of gas errors. Default: 50,000,000\n- MULTICALL_DEBUG: if set, sets logging level for all library loggers to logging.DEBUG\n- MULTICALL_PROCESSES: pass an integer > 1 to use multiprocessing for encoding args and decoding results. Default: 1, which executes all code in the main process.\n- AIOHTTP_TIMEOUT: sets aiohttp timeout period in seconds for async calls to node. Default: 30\n- ASYNC_W3: enables/disables web3 async execution, 0 = Disable, 1 = Enable.\n",
    'author': 'cbhondwe',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cbsystango/multicall-thread-safe/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
