# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['token_throttler', 'token_throttler.storage', 'token_throttler.storage.redis']

package_data = \
{'': ['*']}

extras_require = \
{'aioredis': ['aioredis>=2.0.1,<3.0.0'], 'redis': ['redis>=4.3.4,<5.0.0']}

setup_kwargs = {
    'name': 'token-throttler',
    'version': '1.2.0',
    'description': 'Token throttler is an extendable rate-limiting library somewhat based on a token bucket algorithm',
    'long_description': '# Token throttler\n\n![Coverage](https://img.shields.io/gitlab/coverage/vojko.pribudic/token-throttler/main?job_name=tests)\n![Version](https://img.shields.io/pypi/pyversions/token-throttler)\n![Downloads](https://pepy.tech/badge/token-throttler)\n![Formatter](https://img.shields.io/badge/code%20style-black-black)\n![License](https://img.shields.io/pypi/l/token-throttler)\n\n**Token throttler** is an extendable rate-limiting library somewhat based on a [token bucket algorithm](https://en.wikipedia.org/wiki/Token_bucket).\n\n## Table of contents\n\n1. [ Installation ](#installation)\n2. [ Features ](#features)\n3. [ Usage ](#usage)\n    1. [ Manual usage example ](#usage-manual)\n    2. [ Decorator usage example ](#usage-decorator)\n4. [ Storage ](#storage)\n5. [ Configuration ](#configuration)\n   1. [ Configuration usage ](#configuration-usage)\n\n<a name="installation"></a>\n## 1. Installation\n\nToken throttler is available on PyPI:\n```console \n$ python -m pip install token-throttler\n```\nToken throttler officially supports Python >= 3.7.\n\n*NOTE*: Depending on the storage engine you pick, you can install token throttler with extras:\n```console \n$ python -m pip install token-throttler[redis]\n$ python -m pip install token-throttler[aioredis]\n```\n\n<a name="features"></a>\n## 2. Features\n\n- Blocking (TokenThrottler) and non-blocking (TokenThrottlerAsync)\n- Global throttler(s) configuration\n- Configurable token throttler cost and identifier\n- Multiple buckets per throttler per identifier\n- Buckets can be added/removed manually or by a `dict` configuration\n- Manual usage or usage via decorator\n- Decorator usage supports async code too\n- Custom decorator can be written\n- Extendable storage engine (eg. Redis)\n\n<a name="usage"></a>\n## 3. Usage\n\nToken throttler supports both manual usage and via decorator.\n\nDecorator usage supports both async and sync.\n\n<a name="usage-manual"></a>\n### 1) Manual usage example:\n\n```python\nfrom token_throttler import TokenBucket, TokenThrottler\nfrom token_throttler.storage import RuntimeStorage\n\nthrottler: TokenThrottler = TokenThrottler(cost=1, storage=RuntimeStorage())\nthrottler.add_bucket(identifier="hello_world", bucket=TokenBucket(replenish_time=10, max_tokens=10))\nthrottler.add_bucket(identifier="hello_world", bucket=TokenBucket(replenish_time=30, max_tokens=20))\n\n\ndef hello_world() -> None:\n    print("Hello World")\n\n\nfor i in range(10):\n    throttler.consume(identifier="hello_world")\n    hello_world()\n\nif throttler.consume(identifier="hello_world"):\n    hello_world()\nelse:\n    print("bucket_one ran out of tokens")\n```\n\n<a name="usage-decorator"></a>\n### 2) Decorator usage example:\n\n```python\nfrom token_throttler import TokenBucket, TokenThrottler, TokenThrottlerException\nfrom token_throttler.storage import RuntimeStorage\n\nthrottler: TokenThrottler = TokenThrottler(1, RuntimeStorage())\nthrottler.add_bucket("hello_world", TokenBucket(10, 10))\nthrottler.add_bucket("hello_world", TokenBucket(30, 20))\n\n\n@throttler.enable("hello_world")\ndef hello_world() -> None:\n    print("Hello World")\n\n\nfor i in range(10):\n    hello_world()\n\ntry:\n    hello_world()\nexcept TokenThrottlerException:\n    print("bucket_one ran out of tokens")\n```\n\nFor other examples see [**examples**](https://gitlab.com/vojko.pribudic/token-throttler/-/tree/main/examples) directory.\n\n<a name="storage"></a>\n## 4. Storage\n\n`TokenThrottler` supports `RuntimeStorage` and `RedisStorage`.\n`TokenThrottlerAsync` supports `RedisStorageAsync`\n\nIf you want your own storage engine, feel free to extend the `token_throttler.storage.BucketStorage` or `token_throttler.storage.BucketStorageAsync` classes.\n\nFor storage examples see [**examples**](https://gitlab.com/vojko.pribudic/token-throttler/-/tree/main/examples) directory.\n\n<a name="configuration"></a>\n## 5. Configuration\n\nToken throttler supports global configuration by making use of `ThrottlerConfig` class.\n\nConfiguration params:\n- `IDENTIFIER_FAIL_SAFE` - if invalid identifier is given as a param for the `consume` method and `IDENTIFIER_FAIL_SAFE`\nis set to `True`, no `KeyError` exception will be raised and `consume` will act like a limitless bucket is being consumed.\n- `ENABLE_THREAD_LOCK` - if set to `True`, throttler will acquire a thread lock upon calling `consume` method and release\nthe lock once the `consume` is finished. This avoids various race conditions at a slight performance cost.\n\n<a name="configuration-usage"></a>\n### Configuration usage\n\n```python\nfrom token_throttler import ThrottlerConfig, TokenBucket, TokenThrottler\nfrom token_throttler.storage import RuntimeStorage\n\nThrottlerConfig.set({\n   "ENABLE_THREAD_LOCK": False,\n   "IDENTIFIER_FAIL_SAFE": True,\n})\nthrottler: TokenThrottler = TokenThrottler(1, RuntimeStorage())\nthrottler.add_bucket("hello_world", TokenBucket(10, 10))\nthrottler.add_bucket("hello_world", TokenBucket(30, 20))\n...\n```\n',
    'author': 'Vojko Pribudić',
    'author_email': 'dmanthing@gmail.com',
    'maintainer': 'Vojko Pribudić',
    'maintainer_email': 'dmanthing@gmail.com',
    'url': 'https://gitlab.com/vojko.pribudic/token-throttler',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
