# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lndgrpc', 'lndgrpc.aio', 'lndgrpc.compiled']

package_data = \
{'': ['*']}

install_requires = \
['aiogrpc>=1.8,<2.0',
 'click>=8.1.3,<9.0.0',
 'googleapis-common-protos>=1.53.0,<2.0.0',
 'grpcio-tools>=1.37.0,<2.0.0',
 'grpcio>=1.37.0,<2.0.0',
 'protobuf3-to-dict>=0.1.5,<0.2.0',
 'protobuf>=3.15.8,<4.0.0',
 'ptpython>=3.0.20,<4.0.0',
 'yachalk>=0.1.5,<0.2.0']

entry_points = \
{'console_scripts': ['lndgrpcclient_cli = lndgrpc.cli:cli']}

setup_kwargs = {
    'name': 'lnd-grpc-client',
    'version': '0.5.3',
    'description': 'An rpc client for LND (lightning network deamon)',
    'long_description': '# lnd-grpc-client\nA python grpc client for LND (Lightning Network Daemon) ⚡⚡⚡\n\nThis is a wrapper around the default grpc interface that handles setting up credentials (including macaroons). An async client is also available to do fun async stuff like listening for invoices in the background. \n\n## Dependencies\n- Python 3.6+\n- Working LND lightning node, take note of its ip address.\n- Copy your admin.macaroon and tls.cert files from your node to a directory on your machine. \n\n\n## Installation\n```bash\npip install lnd-grpc-client\n```\n\n### CLI Usage\nThis package adds a CLI command to your PATH once installed:\n\n```bash\nlndgrpcclient_cli\n```\n\n### Setup\n\n```\n$ lndgrpcclient_cli environment\n\nSaving credentials!\nEnter your node\'s IP Address [127.0.0.1]: 86.75.309.69\n86.75.309.69\nEnter your node\'s Port [10009]: \n10009\nEnter your node\'s Alias [default-node-alias]: my-cool-node\nmy-cool-node\nWhere do you want keep your node credentials? Macaroons and tls.cert? [/home/kornpow/Documents/lnd-creds/my-cool-node]: \nEnter your macaroon filename [admin.macaroon]: \nBuild directory structure and save `node-env` file at location: /home/kornpow/Documents/lnd-creds/my-cool-node [True]: 1\nThis environment file must be loaded to access your node!\n\nexport LND_CRED_PATH=/home/kornpow/Documents/lnd-creds/my-cool-node\nexport LND_NODE_IP=86.75.309.69\nexport LND_NODE_PORT=10009\nexport LND_MACAROON=admin.macaroon\nWriting file....\nWrote environment file to location: /home/kornpow/Documents/lnd-creds/my-cool-node/node-env\nEnable it by running: source /home/kornpow/Documents/lnd-creds/my-cool-node/node-env\n```\n\n```\n$ lndgrpcclient_cli credentials --input_format hex --credential_type macaroon\n\nSaving credentials to: /home/kornpow/Documents/lnd-creds/my-cool-node\nEnter your node\'s macaroon []: abcdef123456\nEnter your macaroon name: [admin]: readonly\nEnable this macaroon by running:\n export LND_MACAROON=readonly.macaroon\nWrote file: /home/kornpow/Documents/lnd-creds/my-cool-node/readonly.macaroon\n```\n\n```\n$ lndgrpcclient_cli credentials --input_format hex --credential_type tls\n\nSaving credentials to: /home/kornpow/Documents/lnd-creds/my-cool-node\nEnter your node\'s tls []: abcdef1234\nWrote file: /home/kornpow/Documents/lnd-creds/my-cool-node/tls.cert\n```\n\n\n### Usage\n```\n$ lndgrpcclient_cli shell\n\n>>> lnd.get_info().block_hash\n\'0000000000000000000873876975b2443cfcb93cd9b66c58ed6da922fe5f40b3\'\n\n>>> lnd.get_node_info("0360a41eb8c3fe09782ef6c984acbb003b0e1ebc4fe10ae01bab0e80d76618c8f4").node.alias\n\'kungmeow\'\n\n>>> lnd.get_network_info()\ngraph_diameter: 13\navg_out_degree: 5.528722661077973\nmax_out_degree: 417\nnum_nodes: 18609\nnum_channels: 51442\ntotal_network_capacity: 2873600\navg_channel_size: 55.86096963570623\nmax_channel_size: 1000000\nnum_zombie_chans: 165176\n```\n\n## Advanced Usage\nGo in the `examples` folder for some advanced examples including:\n- Open channel using PSBT: `openchannel-external.py`\n- Open Batch of Channels using PSBT: `batchopenchannel-external.py`\n- Keysend Payments: `send-keysend.py`\n- Reconnect to your peers: `reconnect-peers.py`\n- Channel Acceptor API w/ a custom failure message: `channel-acceptor.py`\n\n### Async\n\n```python\nimport asyncio\nfrom lndgrpc import AsyncLNDClient\n\nasync_lnd = AsyncLNDClient()\n\nasync def subscribe_invoices():\n    print(\'Listening for invoices...\')\n    async for invoice in async_lnd.subscribe_invoices():\n        print(invoice)\n\nasync def get_info():\n    while True:\n        info = await async_lnd.get_info()\n        print(info)\n        await asyncio.sleep(5)\n\nasync def run():\n    coros = [subscribe_invoices(), get_info()]\n    await asyncio.gather(*coros)\n\nloop = asyncio.get_event_loop()\nloop.run_until_complete(run())\n```\n\n### Specifying Macaroon/Cert files\nBy default the client will attempt to lookup the `readonly.macaron` and `tls.cert` files in the mainnet directory. \nHowever if you want to specify a different macaroon or different path you can pass in the filepath explicitly.\n\n```python\nlnd = LNDClient(\n    macaroon_filepath=\'~/.lnd/invoice.macaroon\', \n    cert_filepath=\'path/to/tls.cert\'\n)\n```\n\n## Generating LND Proto Files\n```\nmkvirtualenv gen_rpc_protos\n# or \nworkon gen_rpc_protos\n# then\n\npip install grpcio grpcio-tools googleapis-common-protos sh\n\ncd lndgrpc\ngit clone --depth 1 https://github.com/googleapis/googleapis.git\ncd ..\n```\n\n\nSet environment variables\n```\nexport APP_DIR=$HOME/Documents/lightning/lnd\nexport CLIENT_DIR=$HOME/Documents/lightning/lnd-grpc-client\npython3 rebuild_protos.py\n```\n\n## Deploy to Test-PyPi\n```bash\npoetry build\ntwine check dist/*\ntwine upload --repository-url https://test.pypi.org/legacy/ dist/*\n```',
    'author': 'Kornpow',
    'author_email': 'test@email.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kornpow/lnd-grpc-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
