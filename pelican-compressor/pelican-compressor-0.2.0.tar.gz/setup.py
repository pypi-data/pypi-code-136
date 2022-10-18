# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.compressor']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.5,<5.0', 'web-compressor>=0.3,<0.4']

extras_require = \
{'images': ['Pillow>=9.2,<10.0', 'pillow-avif-plugin>=1.2,<2.0'],
 'minify': ['tdewolff-minify>=2,<3']}

setup_kwargs = {
    'name': 'pelican-compressor',
    'version': '0.2.0',
    'description': "Pelican plugin wrapper for 'web-compressor'",
    'long_description': '# Pelican plugin for `web-compressor`\n\n## Getting started\n\n## Configuration\n\n## Roadmap\n\n- [ ] Update `README.md`\n- [ ] Add tests\n',
    'author': 'Digitalbüro',
    'author_email': 'post@digitalbuero.eu',
    'maintainer': 'Martin Folkers',
    'maintainer_email': 'hello@twobrain.io',
    'url': 'https://digitalbuero.eu',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
