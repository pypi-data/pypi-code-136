# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wacryptolib', 'wacryptolib._crypto_backend']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0,<9.0',
 'decorator>=5.1,<6.0',
 'jsonrpc-requests>=0.4.0,<0.5.0',
 'jsonschema>=4.1.2,<5.0.0',
 'multitimer>=0.3,<0.4',
 'psutil>=5.8.0,<6.0.0',
 'pycryptodome>=3.9.9,<4.0.0',
 'pymongo>=4.0,<5.0',
 'pytz>=2021.3',
 'schema>=0.7.2,<0.8.0',
 'uuid0>=0.2.7,<0.3.0']

extras_require = \
{':sys_platform == "linux"': ['pyudev>=0.22.0,<0.23.0'],
 ':sys_platform == "win32"': ['wmi>=1.5.1,<2.0.0', 'pywin32>=300']}

setup_kwargs = {
    'name': 'wacryptolib',
    'version': '0.10',
    'description': 'Witness Angel Cryptolib',
    'long_description': 'Witness Angel Cryptolib\n#############################\n\n.. image:: https://ci.appveyor.com/api/projects/status/y7mfa00b6c34khe0?svg=true\n    :target: https://travis-ci.com/WitnessAngel/witness-angel-cryptolib\n\n.. image:: https://readthedocs.org/projects/witness-angel-cryptolib/badge/?version=latest&style=flat\n    :target: https://witness-angel-cryptolib.readthedocs.io/en/latest/\n\n-> `Full documentation on READTHEDOCS! <https://witness-angel-cryptolib.readthedocs.io/en/latest/>`_ <-\n\n\nOverview\n+++++++++++++++++++++\n\nThe Witness Angel Cryptolib is a toolkit aimed at handling secure configuration-driven containers, called *cryptainers*.\n\nBy leveraging a flexible JSON-based format called *cryptoconf*, users can define their own hybrid cryptosystem, recursively combining symmetric cihers, asymmetric ciphers, shared secrets, and data signatures.\n\nAccess to the cyptainers is secured by a variety of actors: local device, remote server, trusted third parties...\n\nThe decryption process can involve different steps, like entering passphrases, or submitting authorization requests to third parties.\n\nOverall, the lib gathers lots of utilities to generate and store cryptographic keys, encrypt/check/decrypt cryptainers, access webservices and recorder sensors, and help testing other libraries willing to extend these tools.\n\n\nCLI interface\n+++++++++++++++++++++\n\nA command-line interface is available to play with simple cryptainers.\n\nIf you didn\'t install the library via `pip`, ensure that "src/" is in your PYTHONPATH environnement variable.\n\n::\n\n    $ python -m wacryptolib --help\n\n    $ python -m wacryptolib encrypt -i <data-file> -o <cryptainer-file>\n\n    $ python -m wacryptolib decrypt -i <cryptainer-file> -o <data-file>\n\n    $ python -m wacryptolib summarize -i <cryptoconf-or-cryptainer>\n\n\nBy default, CLI-generated cryptainers use a simple hard-coded cryptographic conf, using unprotected local keypairs, so they are insecure.\nUse a `--cryptoconf` argument during encryption, to specify a config with your own trusted third parties.\nBut note that many cases (accessing remote web gateways, entering passphrases...) are not yet supported by this CLI.\n',
    'author': 'Pascal Chambon',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://witnessangel.com/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
