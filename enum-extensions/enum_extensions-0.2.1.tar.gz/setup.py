# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['enum_extensions']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.3.0']

setup_kwargs = {
    'name': 'enum-extensions',
    'version': '0.2.1',
    'description': 'Enhanced enumerations for Python.',
    'long_description': '# `enum-extensions`\n\n[![License][License Badge]][License]\n[![Version][Version Badge]][Package]\n[![Downloads][Downloads Badge]][Package]\n[![Discord][Discord Badge]][Discord]\n\n[![Documentation][Documentation Badge]][Documentation]\n[![Check][Check Badge]][Actions]\n[![Test][Test Badge]][Actions]\n[![Coverage][Coverage Badge]][Coverage]\n\n> *Enhanced enumerations for Python.*\n\n## Installing\n\n**Python 3.7 or above is required.**\n\n### pip\n\nInstalling the library with `pip` is quite simple:\n\n```console\n$ pip install enum-extensions\n```\n\nAlternatively, the library can be installed from source:\n\n```console\n$ git clone https://github.com/nekitdev/enum-extensions.git\n$ cd enum-extensions\n$ python -m pip install .\n```\n\n### poetry\n\nYou can add `enum-extensions` as a dependency with the following command:\n\n```console\n$ poetry add enum-extensions\n```\n\nOr by directly specifying it in the configuration like so:\n\n```toml\n[tool.poetry.dependencies]\nenum-extensions = "^0.2.0"\n```\n\nAlternatively, you can add it directly from the source:\n\n```toml\n[tool.poetry.dependencies.enum-extensions]\ngit = "https://github.com/nekitdev/enum-extensions.git"\n```\n\n## Examples\n\nCreating a simple enumeration:\n\n```python\nfrom enum_extensions import Enum\n\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n```\n\nAccessing members by name or by value:\n\n```python\nred = Color.RED  # <Color.RED: 1>\ngreen = Color["GREEN"]  # <Color.GREEN: 2>\nblue = Color(3)  # <Color.BLUE: 3>\n```\n\n## Documentation\n\nYou can find the documentation [here][Documentation].\n\n## Support\n\nIf you need support with the library, you can send an [email][Email]\nor refer to the official [Discord server][Discord].\n\n## Changelog\n\nYou can find the changelog [here][Changelog].\n\n## Security Policy\n\nYou can find the Security Policy of `enum-extensions` [here][Security].\n\n## Contributing\n\nIf you are interested in contributing to `enum-extensions`, make sure to take a look at the\n[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].\n\n## License\n\n`enum-extensions` is licensed under the MIT License terms. See [License][License] for details.\n\n[Email]: mailto:support@nekit.dev\n\n[Discord]: https://nekit.dev/discord\n\n[Actions]: https://github.com/nekitdev/enum-extensions/actions\n\n[Changelog]: https://github.com/nekitdev/enum-extensions/blob/main/CHANGELOG.md\n[Code of Conduct]: https://github.com/nekitdev/enum-extensions/blob/main/CODE_OF_CONDUCT.md\n[Contributing Guide]: https://github.com/nekitdev/enum-extensions/blob/main/CONTRIBUTING.md\n[Security]: https://github.com/nekitdev/enum-extensions/blob/main/SECURITY.md\n\n[License]: https://github.com/nekitdev/enum-extensions/blob/main/LICENSE\n\n[Package]: https://pypi.org/project/enum-extensions\n[Coverage]: https://codecov.io/gh/nekitdev/enum-extensions\n[Documentation]: https://nekitdev.github.io/enum-extensions\n\n[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2\n[License Badge]: https://img.shields.io/pypi/l/enum-extensions\n[Version Badge]: https://img.shields.io/pypi/v/enum-extensions\n[Downloads Badge]: https://img.shields.io/pypi/dm/enum-extensions\n\n[Documentation Badge]: https://github.com/nekitdev/enum-extensions/workflows/docs/badge.svg\n[Check Badge]: https://github.com/nekitdev/enum-extensions/workflows/check/badge.svg\n[Test Badge]: https://github.com/nekitdev/enum-extensions/workflows/test/badge.svg\n[Coverage Badge]: https://codecov.io/gh/nekitdev/enum-extensions/branch/main/graph/badge.svg\n',
    'author': 'nekitdev',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nekitdev/enum-extensions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
