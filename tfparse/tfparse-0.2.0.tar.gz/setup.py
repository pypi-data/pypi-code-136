# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tfparse']

package_data = \
{'': ['*']}

install_requires = \
['cffi>=1.0.0']

setup_kwargs = {
    'name': 'tfparse',
    'version': '0.2.0',
    'description': 'Python HCL/Terraform parser via extension for AquaSecurity defsec',
    'long_description': "\n# What\n\nA python extension for parsing and evaluating terraform using defsec.\n\nWhile terraform uses HCL as its configuration format, it requires numerous\nforms of variable interpolation, function and expression evaluation, which\nis beyond the typical usage of an hcl parser. To achieve compatiblity\nwith the myriad real world usages of terraform, this library uses the\ncanonical implementation from terraform, along with the interpolation and evaluation\nfrom defsec to offer a high level interface to parsing terraform modules.\n\n# Installation\n\n```\npip install tfparse\n```\n\nWe currently distribute binaries for MacOS (x86_64, arm64) and Linux (x86_64, aarch64).\n\n\n# Usage\n\nA terraform module root, with `terraform init` having been performed to resolve module references.\n\n```\nfrom tfparse import load_from_path\nparsed = load_from_path('path_to_terraform_root')\nprint(parsed.keys())\n```\n\n# Developing\n\n- requires Go >= 1.18\n- requires Python >= 3.10\n\nThis project uses [Poetry][poetry_website] for package management, if you do not already have Poetry installed you can do so by running the following command:\n\n    curl -sSL https://install.python-poetry.org | python3 -\n\n\n\n## Installing from source\n\nInstalling will build the module and install the local copy of tfparse in to the current Python environment.\n\n```shell\npoetry install\npython\n>>> from tfparse import load_from_path\n>>> parsed = load_from_path('<path_to_terraform>')\n>>> print(parsed.keys())\n```\n\n## Building from source\n\nBuilding will produce a wheel and a source artifact for distribution or upload to package repositories.\n\n```shell\npoetry build\nls -l dist/\n```\n\n## Running the tests\n\nThis project uses pytest\n\n```shell\npoetry run pytest\n```\n\n# Credits\n\naquasecurity/defsec - golang module for parsing and evaluating terraform hcl\n\nScalr/pygohcl - python bindings for terraform hcl via golang extension\n\n\n[poetry_website]: https://python-poetry.org/",
    'author': 'Wayne Witzel III',
    'author_email': 'wayne@stacklet.io',
    'maintainer': 'Cloud Custodian Project',
    'maintainer_email': 'cloud-custodian@googlegroups.com',
    'url': 'https://github.com/cloud-custodian/tfparse',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
