# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['open_rarity',
 'open_rarity.data',
 'open_rarity.models',
 'open_rarity.models.utils',
 'open_rarity.resolver',
 'open_rarity.resolver.models',
 'open_rarity.resolver.rarity_providers',
 'open_rarity.scoring',
 'open_rarity.scoring.handlers']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'scipy>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'open-rarity',
    'version': '0.7.0b0',
    'description': 'Open-Rarity library is an open standard that provides an easy, explanable and reproducible computation for NFT rarity',
    'long_description': '![OpenRarity](img/OR_Github_banner.jpg)\n\n[![Version][version-badge]][version-link]\n[![Test CI][ci-badge]][ci-link]\n[![License][license-badge]][license-link]\n\n\n# OpenRarity\n\nWe’re excited to announce OpenRarity(Beta), a new rarity protocol we’re building for the NFT community. Our objective is to provide a transparent rarity calculation that is entirely open-source, objective, and reproducible.\n\nWith the explosion of new collections, marketplaces and tooling in the NFT ecosystem, we realized that rarity ranks often differed across platforms which could lead to confusion for buyers, sellers and creators. We believe it’s important to find a way to provide a unified and consistent set of rarity rankings across all platforms to help build more trust and transparency in the industry.\n\nWe are releasing the OpenRarity library in a Beta preview to crowdsource feedback from the community and incorporate it into the library evolution.\n\nSee the full announcement in the [blog post](https://mirror.xyz/openrarity.eth/LUoJnybWuNYedIQHD6RRdX1SS9MiowdI6a69X-lefGM).\n\n# Developer documentation\n\nRead [developer documentation](https://openrarity.gitbook.io/developers/) on how to integrate with OpenRarity.\n\n# Setup and run tests locally\n\n```\npoetry install # install dependencies locally\npoetry run pytest # run tests\n```\n\nSome tests are skipped by default due to it being more integration/slow tests.\nTo run resolver tests:\n```\npoetry run pytest -k test_testset_resolver --run-resolvers\n```\n\n# Library usage\nYou can install open rarity as a [python package](https://pypi.org/project/open-rarity/) to use OpenRarity in your project:\n```\npip install open-rarity\n```\nPlease refer to the [scripts/](/scripts/) folder for an example of how to use the library.\n\nIf you have downloaded the repo, you can use OpenRarity shell tool to generate json or csv outputs of OpenRarity scoring and ranks for any collections:\n```\npython -m scripts.score_real_collections boredapeyachtclub proof-moonbirds\n```\nRead [developer documentation](https://openrarity.gitbook.io/developers/) for advanced library usage\n\n\n\n# Contributions guide and governance\n\nOpenRarity is a community effort to improve rarity computation for NFTs (Non-Fungible Tokens). The core collaboration group consists of four primary contributors: [Curio](https://curio.tools), [icy.tools](https://icy.tools), [OpenSea](https://opensea.io) and [Proof](https://www.proof.xyz/)\n\nOpenRarity is an open-source project and all contributions are welcome. Consider following steps when you request/propose contribution:\n\n- Have a question? Submit it on OpenRarity GitHub  [discussions](https://github.com/ProjectOpenSea/open-rarity/discussions) page\n- Create GitHub issue/bug with description of the problem [link](https://github.com/ProjectOpenSea/open-rarity/issues/new?assignees=impreso&labels=bug&template=bug_report.md&title=)\n- Submit Pull Request with proposed changes\n- To merge the change in the `main` branch you required to get at least 2 approvals from the project maintainer list\n- Always add a unit test with your changes\n\nWe use git-precommit hooks in OpenRarity repo. Install it with the following command\n```\npoetry run pre-commit install\n```\n\n# Project Setup and Core technologies\n\nWe used the following core technologies in OpenRarity:\n\n- Python ≥ 3.10.x\n- Poetry for dependency management\n- Numpy ≥1.23.1\n- PyTest for unit tests\n\n# License\n\nApache 2.0 , OpenSea, ICY, Curio, PROOF\n\n\n\n[license-badge]: https://img.shields.io/github/license/ProjectOpenSea/open-rarity\n[license-link]: https://github.com/ProjectOpenSea/open-rarity/blob/main/LICENSE\n[ci-badge]: https://github.com/ProjectOpenSea/open-rarity/actions/workflows/tests.yaml/badge.svg\n[ci-link]: https://github.com/ProjectOpenSea/open-rarity/actions/workflows/tests.yaml\n[version-badge]: https://img.shields.io/github/v/release/ProjectOpenSea/open-rarity\n[version-link]: https://github.com/ProjectOpenSea/open-rarity/releases?display_name=tag\n',
    'author': 'Dan Meshkov',
    'author_email': 'daniil.meshkov@opensea.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
