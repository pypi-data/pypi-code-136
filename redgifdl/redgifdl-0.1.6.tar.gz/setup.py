# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redgifdl']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'redgifdl',
    'version': '0.1.6',
    'description': '',
    'long_description': '# redgifdl\n\nDownload from redgif by sending in URL and output file\n\n\n## Usage\n\n```\nfrom redgifdl import download\n\n\ndownload.url_file(redgifs_url="URL", filename="foo.mp4")\n\n```',
    'author': 'jorg-j',
    'author_email': 'jorgensen.server@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
