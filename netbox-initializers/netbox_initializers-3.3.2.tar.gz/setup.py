# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['netbox_initializers',
 'netbox_initializers.initializers',
 'netbox_initializers.management',
 'netbox_initializers.management.commands']

package_data = \
{'': ['*'], 'netbox_initializers.initializers': ['yaml/*']}

install_requires = \
['ruamel.yaml==0.17.21']

setup_kwargs = {
    'name': 'netbox-initializers',
    'version': '3.3.2',
    'description': 'Load initial data into Netbox',
    'long_description': '# Netbox Initializers Plugin\n\nLoad data from YAML files into Netbox\n\n## Installation\n\nFirst activate your virtual environment where Netbox is installed, the install the plugin version correspondig to your Netbox version.\n```bash\npip install "netbox-initializers==3.3.*"\n```\nThen you need to add the plugin to the `PLUGINS` array in the Netbox configuration.\n```python\nPLUGINS = [\n    \'netbox_initializers\',\n]\n```\n\n## Getting started\n\nAt first you need to start with writing the YAML files that contain the initial data. To make that easier the plugin includes example files for all supported initializers. To access those examples you can copy them into a directory of your choosing and edit them there. To copy the files run the following command (in your Netbox directory):\n\n```bash\n./manage.py copy_initializers_examples --path /path/for/example/files\n```\n\nAfter you filled in the data you want to import, the import can be started with this command:\n\n```bash\n./manage.py load_initializer_data --path /path/for/example/files\n```\n\n\n## Netbox Docker image\n\nThe initializers where a part of the Docker image and where then extracted into a Netbox plugin. This was done to split the release cycle of the initializers and the image.\nTo use the new plugin in a the Netbox Docker image, it musst be installad into the image. To this, the following example can be used as a starting point:\n\n```dockerfile\nFROM netboxcommunity/netbox:v3.3\nRUN /opt/netbox/venv/bin/pip install "netbox-initializers==3.3.*"\n```\n',
    'author': 'Tobias Genannt',
    'author_email': 'tobias.genannt@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tobiasge/netbox-initializers',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
