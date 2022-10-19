# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starknet_devnet',
 'starknet_devnet.blueprints',
 'starknet_devnet.blueprints.rpc',
 'starknet_devnet.blueprints.rpc.structures',
 'starknet_devnet.lite_mode']

package_data = \
{'': ['*'],
 'starknet_devnet': ['accounts_artifacts/OpenZeppelin/0.4.0b-fork/Account.cairo/*']}

install_requires = \
['Flask[async]>=2.0.3,<2.1.0',
 'Werkzeug>=2.0.3,<2.1.0',
 'cairo-lang==0.10.1',
 'cloudpickle>=2.1.0,<2.2.0',
 'crypto-cpp-py>=1.0.4,<1.1.0',
 'flask-cors>=3.0.10,<3.1.0',
 'gunicorn>=20.1.0,<20.2.0',
 'marshmallow>=3.17.0,<3.18.0',
 'typing-extensions>=4.3.0,<4.4.0']

entry_points = \
{'console_scripts': ['starknet-devnet = starknet_devnet.server:main']}

setup_kwargs = {
    'name': 'starknet-devnet',
    'version': '0.3.4',
    'description': 'A local testnet for Starknet',
    'long_description': '<!-- logo / title -->\n<p align="center" style="margin-bottom: 0px !important">\n  <img width="200" src="https://user-images.githubusercontent.com/2848732/193076972-da6fa36e-11f7-4cb3-aa29-673224f8576d.png" alt="Devnet" align="center">\n</p>\n<h1 align="center" style="margin-top: 0px !important">Starknet Devnet</h1>\n\nA Flask wrapper of Starknet state. Similar in purpose to Ganache.\n\nAims to mimic Starknet\'s Alpha testnet, but with simplified functionality.\n\n## 🌐 Docs\n\n[Click Here](https://shard-labs.github.io/starknet-devnet/) for the documentation.\n\n## ✏️ Contributing\n\nWe ❤️ and encourage all contributions!\n\n## 🙌 Special Thanks\n\nSpecial thanks to all the [contributors](https://github.com/Shard-Labs/starknet-devnet/graphs/contributors)!\n\n',
    'author': 'FabijanC',
    'author_email': 'fabijan.corak@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Shard-Labs/starknet-devnet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
