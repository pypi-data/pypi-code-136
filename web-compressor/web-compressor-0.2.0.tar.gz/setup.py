# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['web_compressor', 'web_compressor.handlers']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4,<5']

extras_require = \
{'images': ['Pillow>=9.2,<10.0', 'pillow-avif-plugin>=1.2,<2.0'],
 'minify': ['tdewolff-minify>=2,<3']}

setup_kwargs = {
    'name': 'web-compressor',
    'version': '0.2.0',
    'description': 'Supercharges HTML files & web assets',
    'long_description': "# WebCompressor\n\nSupercharge HTML files & web assets - ideal for improving 'static site generator' output\n\n## Getting started\n\n## Configuration\n\n## Roadmap\n\n- [ ] Update `README.md`\n- [x] Add tests\n- [ ] Add more tests\n",
    'author': 'Digitalbüro',
    'author_email': 'post@digitalbuero.eu',
    'maintainer': 'Martin Folkers',
    'maintainer_email': 'hello@twobrain.io',
    'url': 'https://digitalbuero.eu',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
