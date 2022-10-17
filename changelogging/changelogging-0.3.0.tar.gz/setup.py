# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['changelogging']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.1.0',
 'click>=8.1.3',
 'entrypoint>=1.3.0',
 'toml>=0.10.2',
 'typing-extensions>=4.3.0',
 'versions>=1.2.1',
 'wraps>=0.2.0',
 'yarl>=1.8.1']

entry_points = \
{'console_scripts': ['changelogging = changelogging.main:changelogging']}

setup_kwargs = {
    'name': 'changelogging',
    'version': '0.3.0',
    'description': 'Building changelogs from fragments.',
    'long_description': '# `changelogging`\n\n[![License][License Badge]][License]\n[![Version][Version Badge]][Package]\n[![Downloads][Downloads Badge]][Package]\n[![Discord][Discord Badge]][Discord]\n\n[![Documentation][Documentation Badge]][Documentation]\n[![Check][Check Badge]][Actions]\n[![Test][Test Badge]][Actions]\n[![Coverage][Coverage Badge]][Coverage]\n\n> *Building changelogs from fragments.*\n\n## Installing\n\n**Python 3.7 or above is required.**\n\n### pip\n\nInstalling the library with `pip` is quite simple:\n\n```console\n$ pip install changelogging\n```\n\nAlternatively, the library can be installed from source:\n\n```console\n$ git clone https://github.com/nekitdev/changelogging.git\n$ cd changelogging\n$ python -m pip install .\n```\n\n### poetry\n\nYou can add `changelogging` as a dependency with the following command:\n\n```console\n$ poetry add changelogging\n```\n\nOr by directly specifying it in the configuration like so:\n\n```toml\n[tool.poetry.dependencies]\nchangelogging = "^0.3.0"\n```\n\nAlternatively, you can add it directly from the source:\n\n```toml\n[tool.poetry.dependencies.changelogging]\ngit = "https://github.com/nekitdev/changelogging.git"\n```\n\n## Documentation\n\nYou can find the documentation [here][Documentation].\n\n## Support\n\nIf you need support with the library, you can send an [email][Email]\nor refer to the official [Discord server][Discord].\n\n## Changelog\n\nYou can find the changelog [here][Changelog].\n\n## Security Policy\n\nYou can find the Security Policy of `changelogging` [here][Security].\n\n## Contributing\n\nIf you are interested in contributing to `changelogging`, make sure to take a look at the\n[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].\n\n## License\n\n`changelogging` is licensed under the MIT License terms. See [License][License] for details.\n\n[Email]: mailto:support@nekit.dev\n\n[Discord]: https://nekit.dev/discord\n\n[Actions]: https://github.com/nekitdev/changelogging/actions\n\n[Changelog]: https://github.com/nekitdev/changelogging/blob/main/CHANGELOG.md\n[Code of Conduct]: https://github.com/nekitdev/changelogging/blob/main/CODE_OF_CONDUCT.md\n[Contributing Guide]: https://github.com/nekitdev/changelogging/blob/main/CONTRIBUTING.md\n[Security]: https://github.com/nekitdev/changelogging/blob/main/SECURITY.md\n\n[License]: https://github.com/nekitdev/changelogging/blob/main/LICENSE\n\n[Package]: https://pypi.org/project/changelogging\n[Coverage]: https://codecov.io/gh/nekitdev/changelogging\n[Documentation]: https://nekitdev.github.io/changelogging\n\n[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2\n[License Badge]: https://img.shields.io/pypi/l/changelogging\n[Version Badge]: https://img.shields.io/pypi/v/changelogging\n[Downloads Badge]: https://img.shields.io/pypi/dm/changelogging\n\n[Documentation Badge]: https://github.com/nekitdev/changelogging/workflows/docs/badge.svg\n[Check Badge]: https://github.com/nekitdev/changelogging/workflows/check/badge.svg\n[Test Badge]: https://github.com/nekitdev/changelogging/workflows/test/badge.svg\n[Coverage Badge]: https://codecov.io/gh/nekitdev/changelogging/branch/main/graph/badge.svg\n',
    'author': 'nekitdev',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nekitdev/changelogging',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
