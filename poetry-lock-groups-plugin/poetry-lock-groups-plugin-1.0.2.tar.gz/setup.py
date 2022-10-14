# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_lock_groups']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.8.0,<23.0.0', 'poetry>=1.2.1,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['lock-groups-plugin = '
                               'poetry_lock_groups.plugin:LockGroupsPlugin']}

setup_kwargs = {
    'name': 'poetry-lock-groups-plugin',
    'version': '1.0.2',
    'description': 'Poetry extension enabling group dependency application at the lock stage',
    'long_description': '[![PyPI](https://img.shields.io/pypi/v/poetry-lock-groups-plugin)](https://pypi.org/project/poetry-lock-group-plugin/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry-lock-groups-plugin)\n![PyPI - Wheel](https://img.shields.io/pypi/wheel/poetry-lock-groups-plugin)\n[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/mit)\n\n# DEPRECATION NOTICE\n\n**Warning** - this plugin has been **deprecated**.  Developers should instead consider using the [poetry-monorepo-dependency-plugin](https://bitbucket.org/cpointe/poetry-monorepo-dependency-plugin/) \nto support deploying and releasing Poetry projects with path-based dependencies on other Poetry projects within a monorepo.\n\n## Overview\n\n`poetry-lock-groups-plugin` is a lightweight plugin which enables Poetry\'s [dependency group](https://python-poetry.org/docs/managing-dependencies/#dependency-groups) options \n(`--with`, `--without`, `--only`) when executing the `lock` command.  Broadly, this plugin helps enable a solution pattern that developers may use when working with and releasing \npackages within a more complex Python monorepo environment that relies on path-based dependencies.\n\n## Installation\n\nExecute the following command:\n```shell\npoetry self add poetry-lock-groups-plugin\n```\n\n## Use Case\n\nWhen working within a Python monorepo project structure with [local path dependencies](https://python-poetry.org/docs/dependency-specification/#path-dependencies), a frequently encountered challenge involves publishing these packages to a PyPI index in a way that can be easily utilized by downstream consumers.  Specifically, while editable path dependencies work well to support normal development activities, publishing a package with local path dependencies into a usable `sdist` or `wheel` archive typically involves replacing those path dependencies with references to packages that are resolvable within a PyPI repository.\n\nIn order to support this scenario, rather than maintaining two distinct versions of `pyproject.toml` (one with local path dependencies and the other with PyPI resolvable dependencies), developers may leverage dependency groups. Vanilla Poetry recognizes dependency groups only at the `install` phase - by advancing that recognition to the `lock` stage, we enable predictable, flexible patterns to support monorepo development.\n\n## Example\n\nGiven the following `pyproject.toml` where `my-poetry-project` depends on `common-library` within the same monorepo project structure:\n```toml\n[tool.poetry]\nname = "my-poetry-project"\nversion = "0.1.0.dev"\ndescription = ""\n\n[tool.poetry.dependencies]\npython = "^3.9"\n\n[tool.poetry.plugins."poetry.application.plugin"]\nlock-groups-plugin = "poetry_lock_groups.plugin:LockGroupsPlugin"\n\n[tool.poetry.group.remote.dependencies]\ncommon-library = "^1.2.6"\n\n[tool.poetry.group.local.dependencies]\ncommon-library = {path = "../../common-library/"}\n\n[build-system]\nrequires = ["poetry-core>=1.2"]\nbuild-backend = "poetry.core.masonry.api"\n```\n\nBy running the following command:\n\n```shell\npoetry lock --with remote --without local\n```\n\nThis will generate a `poetry.lock` file that includes the dependency definitions within the `remote` group, but without those in the `local` group.  Note that if we included both groups, or simply refrained from specifying group usages, we would see behavior \nidentical to that in vanilla Poetry, which is, in this case, undefined. \n\nDevelopers will typically execute the following commands as a part of their development workflow while building/testing functionality:\n```shell\npoetry lock --with local --without remote\npoetry install --with local --without remote\n```\nHowever, when performing releases, developers will execute the following to ensure that local path dependencies are removed from archives that are published to the configured PyPI repository:\n```shell\npoetry lock --with remote --without local\npoetry install --with remote --without local\n```\n\nConsider using [Habushu](https://bitbucket.org/cpointe/habushu/) to codify and automate this workflow!\n\n### Usage Considerations \n\nNote that the following sequence of commands may fail:\n```shell\npoetry lock --without local\npoetry install --with local\n```\nThis is because the `poetry install` command searches `poetry.lock` to install dependencies. By building the lock file without the `local` group, any dependencies that exist only within that group will have no known sources, rendering them unresolvable.\n\n`poetry-lock-groups-plugin` **only** modifies lock operations initiated via the `lock` command.  It makes no attempt to modify behavior resulting from an implied lock, such as when running `poetry install` without having already created a lock file.\n\n### Alternative Approaches\n\nInstead of using dependency groups as described above to capture local path dependencies in a monorepo project, developers may consider using the [poetry-stickywheel-plugin](https://pypi.org/project/poetry-stickywheel-plugin/) or other similar approach to dynamically re-write `pyproject.toml` on archive deployment with local path dependency declarations appropriately replaced. \n\n## Releasing to PyPI\n\nReleasing `poetry-lock-groups-plugin` leverages the `maven-release-plugin` to automate release preparation and delegates to the [habushu-maven-plugin](https://bitbucket.org/cpointe/habushu) to publish the package to PyPI during the `deploy` phase.  A [PyPI account](https://pypi.org/account/register/) with access to the [poetry-lock-groups-plugin](https://pypi.org/project/poetry-lock-groups-plugin/) project is required. PyPI account credentials should be specified in your `settings.xml` under the `<id>pypi</id>` `<server>` entry:\n\n```xml\n<settings>\n  <servers>\n    <server>\n      <id>pypi</id>\n      <username>pypi-username</username>\n      <password>pypi-password</password>\n    </server>\n  </servers>\n</settings>\n```\n',
    'author': 'Peter Jablonski',
    'author_email': 'jablonski_peter@bah.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://bitbucket.org/cpointe/poetry-lock-groups-plugin',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
