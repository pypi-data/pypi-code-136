# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poolgrpc', 'poolgrpc.compiled']

package_data = \
{'': ['*']}

install_requires = \
['aiogrpc>=1.8,<2.0',
 'googleapis-common-protos>=1.53.0,<2.0.0',
 'grpcio-tools>=1.37.0,<2.0.0',
 'grpcio>=1.37.0,<2.0.0',
 'protobuf3-to-dict>=0.1.5,<0.2.0',
 'protobuf>=3.15.8,<4.0.0']

entry_points = \
{'console_scripts': ['poolgrpcclient_cli = poolgrpc.client:cli']}

setup_kwargs = {
    'name': 'pool-grpc-client',
    'version': '0.1.1',
    'description': 'An rpc client for LL Pool (Rent Channels)',
    'long_description': '# pool-grpc-client\nA python grpc client for Lightning Pool (Lightning Network Daemon) ⚡⚡⚡\n\nThis is a wrapper around the default grpc interface that handles setting up credentials (including macaroons.\n\n## Dependencies\n- Python 3.6+\n- Working LND lightning node, take note of its ip address.\n- Copy your pool.macaroon and tls.cert files from `~/.pool/mainnet` to a directoy on your machine. \n\n\n## Installation\n```bash\npip install pool-grpc-client\n```\n\n\n\n\n## Basic Usage\nThe api mirrors the underlying lnd grpc api (http://api.lightning.community/) but methods will be in pep8 style. ie. `.GetInfo()` becomes `.get_info()`.\n\n```python\nfrom pathlib import Path\nimport json\nfrom poolgrpc.client import PoolClient\n\ncredential_path = Path("/home/skorn/.pool/mainnet/")\n\nmac = str(credential_path.joinpath("pool.macaroon").absolute())\ntls = str(credential_path.joinpath("tls.cert").absolute())\n\npool = PoolClient(\n\tmacaroon_filepath=mac,\n\tcert_filepath=tls\n)\n\npool.get_info()\n\npool.get_lsat_tokens()\n```\n\n### Specifying Macaroon/Cert files\nBy default the client will attempt to lookup the `readonly.macaron` and `tls.cert` files in the mainnet directory. \nHowever if you want to specify a different macaroon or different path you can pass in the filepath explicitly.\n\n```python\nlnd = LNDClient(\n    macaroon_filepath=\'~/.lnd/invoice.macaroon\', \n    cert_filepath=\'path/to/tls.cert\'\n)\n```\n\n## Compiling Proto Files\n\n\n```\nmkvirtualenv gen_rpc_protos\n# or \nworkon gen_rpc_protos\n# then\n\npip install grpcio grpcio-tools googleapis-common-protos sh\n\ncd poolgrpc\ngit clone --depth 1 https://github.com/googleapis/googleapis.git\ncd ..\n```\n\n\nSet environment variables\n```\nexport APP_DIR=$HOME/Documents/lightning/pool\nexport CLIENT_DIR=$HOME/Documents/lightning/pool-grpc-client\n```\n\n```python\npython3 rebuild_protos.py\n```\n\n## Deploy to Test-PyPi\n```bash\npoetry build\ntwine check dist/*\ntwine upload --repository-url https://test.pypi.org/legacy/ dist/*\n```',
    'author': 'Kornpow',
    'author_email': 'test@email.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>3.6',
}


setup(**setup_kwargs)
