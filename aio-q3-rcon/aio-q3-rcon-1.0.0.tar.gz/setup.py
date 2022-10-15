# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioq3rcon']

package_data = \
{'': ['*']}

install_requires = \
['asyncio-dgram>=2.1.2,<3.0.0']

entry_points = \
{'console_scripts': ['q3rcon = aioq3rcon.cli:rcon']}

setup_kwargs = {
    'name': 'aio-q3-rcon',
    'version': '1.0.0',
    'description': 'An async Quake 3 RCON implementation with a CLI',
    'long_description': '# aio-q3-rcon\n*An async Quake 3 RCON implementation for Python*\n\n## Installation\n```\npip install aio-q3-rcon\n```\nor with the cli extra\n```\npip install aio-q3-rcon[cli]\n```\n\n## CLI Usage\n```\nUsage: q3rcon [OPTIONS] ADDRESS PASSWORD\n\nOptions:\n  -p, --port INTEGER RANGE        [1<=x<=65535]\n  --timeout FLOAT RANGE           [x>=0.01]\n  --fragment-read-timeout, --fr-timeout FLOAT RANGE\n                                  [x>=0.01]\n  --retries INTEGER RANGE         [x>=1]\n  --debug\n  --help                          Show this message and exit.\n```\n\n## API Reference\n#### [Examples Folder](examples)\n\n#### *class* [`Client`](aioq3rcon/client.py)(`host`: *`str`*, `port`: *`int`*, `timeout`: *`float`*, `fragment_read_timeout`: *`float`*, `retries`: *`int`*, `logger`: *`Logger | None`*)\n- Parameters:\n  - `host`: *`str`* - *the host / IP / domain of the server to connect to*\n  - `port`: *`port`* - *the port of the server to connect to*\n    - default value is `27960`\n  - `timeout`: *`float`* - *the timeout for network operations*\n    - default value is `2.0`\n    - for network operations with retries, the timeout applies to the rewrite attempts as a whole, rather than being per retry\n  - `fragment_read_timeout`: *`float`* - *the timeout for waiting on potentially fragmented responses*\n    - default value is `.25`\n    - the Quake 3 server can sometimes send fragmented responses, since there is no consistent way to tell if a response is fragmented or not, the best solution is to wait for fragmented responses from the server whether they exist or not. This value is the timeout for waiting for those responses.\n  - `retries`: *`int`* - *the amount of retries per network operation*\n    - default value is `2`\n    - all network operations except for reads are wrapped in retry logic\n  - `logger`: *`Logger | None`* - *the logger instance*\n    - default value is `None`\n    - if there is no logger specified, a logger that has `disabled` set to `True` will be used instead\n    - currently only some debug information is logged\n- Methods:\n  - `connect`(`verify`: *`bool`* = `True`) -> *`None`*\n    - *connects to the server*\n    - *if `verify` is `True`, then the `heartbeat` RCON command is sent and the password is checked as well*\n    - *if `Client` is being used as a context manager, this will be called automatically upon enter*\n  - `close`() -> *`None`*\n    - *closes the connection to the server*\n    - *if `Client` is being used as a context manager, this will be called automatically upon exit*\n#### *exception* [`RCONError`](aioq3rcon/errors.py)\n- Base exception all aio-q3-rcon errors derive from\n#### *exception* [`IncorrectPasswordError`](aioq3rcon/errors.py)\n- Raised when the provided password is incorrect\n',
    'author': 'Milo Weinberg',
    'author_email': 'iapetus011@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Iapetus-11/aio-q3-rcon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
