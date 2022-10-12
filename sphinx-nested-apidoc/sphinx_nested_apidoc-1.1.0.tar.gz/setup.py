# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sphinx_nested_apidoc']

package_data = \
{'': ['*']}

install_requires = \
['Sphinx>=5.0.0,<6.0.0']

entry_points = \
{'console_scripts': ['sphinx-nested-apidoc = '
                     'sphinx_nested_apidoc.__main__:main']}

setup_kwargs = {
    'name': 'sphinx-nested-apidoc',
    'version': '1.1.0',
    'description': 'sphinx-nested-apidoc: When flattened is not enough',
    'long_description': "# sphinx-nested-apidoc\n\n[![CI](https://github.com/arunanshub/sphinx-nested-apidoc/actions/workflows/ci.yml/badge.svg)](https://github.com/arunanshub/sphinx-nested-apidoc/actions/workflows/ci.yml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[![Python Versions](https://img.shields.io/pypi/pyversions/sphinx-nested-apidoc)](https://pypi.org/project/sphinx-nested-apidoc)\n\nWhen flattened is not enough.\n\n## Installation\n\nUse `pip` or `pip3` to install `sphinx-nested-apidoc`\n\n```bash\npip install sphinx-nested-apidoc\n```\n\nor\n\n```bash\npip3 install sphinx-nested-apidoc\n```\n\n## Introduction\n\n`sphinx-apidoc` is a great tool for generating documentation, but it does not\nreplicate the directory structure of your package. `sphinx-nested-apidoc` aims\nto solve that problem.\n\n## Usage Overview\n\nLet's say we have the following directory structure of our package:\n\n```\nmymodule/\n├── fruits/\n│   ├── __init__.py\n│   ├── apple.py\n│   ├── pear.py\n│   ├── guava.py\n│   └── mango.py\n├── animals/\n│   ├── special/\n│   │   ├── __init__.py\n│   │   ├── doggo.py\n│   │   └── catto.py\n│   ├── __init__.py\n│   ├── bear.py\n│   ├── giraffe.py\n│   ├── monke.py\n│   └── chimp.py\n├── __init__.py\n├── base.py\n├── exceptions.py\n└── secret.py\n```\n\nAnd we want to generate documentation for this package in some directory `docs/`.\n\n### A short comparison\n\nLet's see the difference.\n\n#### Using `sphinx-apidoc` we get\n\nWe use the following command:\n\n```bash\nsphinx-apidoc -o docs/ mymodule/ -e\n```\n\nIt generates:\n\n```\ndocs/\n├── modules.rst\n├── mymodule.animals.bear.rst\n├── mymodule.animals.chimp.rst\n├── mymodule.animals.giraffe.rst\n├── mymodule.animals.monke.rst\n├── mymodule.animals.rst\n├── mymodule.animals.special.catto.rst\n├── mymodule.animals.special.doggo.rst\n├── mymodule.animals.special.rst\n├── mymodule.base.rst\n├── mymodule.exceptions.rst\n├── mymodule.fruits.apple.rst\n├── mymodule.fruits.guava.rst\n├── mymodule.fruits.mango.rst\n├── mymodule.fruits.pear.rst\n├── mymodule.fruits.rst\n├── mymodule.rst\n└── mymodule.secret.rst\n```\n\nThis is not very clean, obviously.\n\n#### Using `sphinx-nested-apidoc` we get\n\nWe use the following command:\n\n```bash\nsphinx-nested-apidoc -o docs/ mymodule/\n```\n\nIt generates:\n\n```\ndocs/\n├── modules.rst\n└── mymodule\n    ├── animals\n    │   ├── bear.rst\n    │   ├── chimp.rst\n    │   ├── giraffe.rst\n    │   ├── index.rst\n    │   ├── monke.rst\n    │   └── special\n    │       ├── catto.rst\n    │       ├── doggo.rst\n    │       └── index.rst\n    ├── base.rst\n    ├── exceptions.rst\n    ├── fruits\n    │   ├── apple.rst\n    │   ├── guava.rst\n    │   ├── index.rst\n    │   ├── mango.rst\n    │   └── pear.rst\n    ├── index.rst\n    └── secret.rst\n```\n\nLooks clean!\n\n## Usage Details\n\n```\nusage: sphinx-nested-apidoc [-h] [-v | -q] [--version] [-f] [-n] -o DESTDIR\n                            [-s SUFFIX] [--implicit-namespaces]\n                            module_path ...\n\nGenerates nested directory from sphinx-apidoc's flattened files. It is simply\na wrapper over sphinx-apidoc and you can pass additional arguments to it for\nextended configuration.\n\npositional arguments:\n  module_path           Path to package to document.\n\noptions:\n  -h, --help            show this help message and exit\n  -v, --verbose         Increase application verbosity. This option is\n                        repeatable and will increase verbosity each time it is\n                        repeated. This option cannot be used when -q/--quiet\n                        is used. (default: 3)\n  -q, --quiet           Disable logging. This option cannot be used when\n                        -v/--verbose is used. (default: False)\n  --version             show program's version number and exit\n  -f, --force           Replace existing files. (default: False)\n  -n, --dry-run         Run the script without creating files (default: False)\n  -o DESTDIR, --output-dir DESTDIR\n                        directory to place all output (default: None)\n\nsphinx-apidoc options:\n  -s SUFFIX, --suffix SUFFIX\n                        file suffix (default: rst)\n  --implicit-namespaces\n                        interpret module paths according to PEP-0420 implicit\n                        namespaces specification (default: False)\n  ...                   Commands and flags to supply to sphinx-apidoc. Note\n                        that some arguments like `--dry-run` are ignored.\n\nsphinx-nested-apidoc is licensed under MIT license. Visit\n<https://github.com/arunanshub/sphinx-nested-apidoc> for more info.\n```\n\n## Some additional details\n\n### What it does\n\n- As you saw earlier, it generates a nested directory from a flattened one.\n- Under the hood, it uses `sphinx-apidoc`. More on this below.\n\nAs stated above, `sphinx-nested-apidoc` uses `sphinx-apidoc` internally. This means,\nyou can configure `sphinx-apidoc` from `sphinx-nested-apidoc`. For example:\n\n```bash\n# You can pass arguments like this:\nsphinx-nested-apidoc -o docs/ mymodule/ -- -M -F --ext-githubpages\n# or you can simply omit the '--'.\n```\n\nEverything after the required positional argument of `sphinx-nested-apidoc` is\npassed to `sphinx-apidoc`.\n\n### What it does not do\n\n- It does not modify the contents of the file. It just renames (or moves) them.\n- It is not a standalone tool. It requires `sphinx-apidoc` for its work.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n",
    'author': 'Arunanshu Biswas',
    'author_email': 'mydellpc07@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/arunanshub/sphinx-nested-apidoc',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
