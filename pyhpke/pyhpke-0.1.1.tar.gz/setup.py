# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyhpke']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=3.4.7,<39']

setup_kwargs = {
    'name': 'pyhpke',
    'version': '0.1.1',
    'description': 'HPKE implementation',
    'long_description': 'Forked from [ctz/hpke-py](https://github.com/ctz/hpke-py).\n\n**This package is only for an experimental [COSE-HPKE](https://datatracker.ietf.org/doc/html/draft-ietf-cose-hpke-02) implementation on [dajiaji/python-cwt](https://github.com/dajiaji/python-cwt). DO NOT INSTALL IT.**\n\n# pyhpke\n\nThis is an implementation of [RFC9180](https://datatracker.ietf.org/doc/rfc9180/) in python3, using\n[cryptography.io](https://cryptography.io) for the underlying cryptography.\n\n## Features\n\n - Modes\n   - [x] mode_base\n   - [ ] mode_psk\n   - [x] mode_auth\n   - [ ] mode_auth_psk\n - AEADs\n   - [x] AES-128-GCM\n   - [x] AES-256-GCM\n   - [x] ChaCha20Poly1305\n   - [x] Export only\n - KEMs\n   - [x] DHKEM(P-256, HKDF-SHA256)\n   - [ ] DHKEM(P-384, HKDF-SHA384)\n   - [x] DHKEM(P-521, HKDF-SHA512)\n   - [ ] DHKEM(X25519, HKDF-SHA256)\n   - [ ] DHKEM(X448, HKDF-SHA512)\n - KDFs\n   - [x] HKDF-SHA256\n   - [x] HKDF-SHA384\n   - [x] HKDF-SHA512\n\n## Original Author\nJoseph Birr-Pixton <jpixton@gmail.com>\n\n## License\npyhpke is licensed under the Apache License, Version 2.0. See\n[LICENSE](LICENSE) for the full license text.\n',
    'author': 'Ajitomi Daisuke',
    'author_email': 'dajiaji@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dajiaji/pyhpke',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
