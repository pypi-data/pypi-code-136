# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncipfscluster']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8,<4.0']

setup_kwargs = {
    'name': 'asyncipfscluster',
    'version': '0.1.2',
    'description': 'Async IPFS Cluster HTTP API',
    'long_description': '# Async IPFS API\n\n## Install\n\n```bash\npip install asyncipfscluster\n```\n\n## Usage\n\n```python\nimport asyncio\nfrom asyncipfscluster import IPFSClient\n\nclient = IPFSClient("http://127.0.0.1:9094")\n\nasync def main():\n    async with client as session:\n        cid = await client.add_bytes(b"Hello from cofob!", "text/plain")\n        print(cid)\n\nasyncio.run(main())\n```\n',
    'author': 'Egor Ternovoy',
    'author_email': 'cofob@riseup.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://git.frsqr.xyz/cofob/asyncipfscluster',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
