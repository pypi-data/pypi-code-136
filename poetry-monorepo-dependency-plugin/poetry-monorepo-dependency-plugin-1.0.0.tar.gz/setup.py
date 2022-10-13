# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_monorepo_dependency_plugin']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2,<2.0']

entry_points = \
{'poetry.application.plugin': ['poetry-monorepo-dependency-plugin = '
                               'poetry_monorepo_dependency_plugin.plugin:MonorepoDependencyPlugin']}

setup_kwargs = {
    'name': 'poetry-monorepo-dependency-plugin',
    'version': '1.0.0',
    'description': 'Poetry plugin that generates more easily consumable archives for projects in a monorepo structure with path dependencies on other Poetry projects',
    'long_description': '# Poetry Monorepo Dependency Plugin\n\n[![PyPI](https://img.shields.io/pypi/v/krausening)](https://pypi.org/project/poetry-monorepo-dependency-plugin/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry-monorepo-dependency-plugin)\n![PyPI - Wheel](https://img.shields.io/pypi/wheel/poetry-monorepo-dependency-plugin)\n[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/mit)\n\nForked and inspired by the [poetry-stickywheel-plugin](https://github.com/artisanofcode/poetry-stickywheel-plugin), this\nPoetry[poetry] plugin facilitates the usage of more complex monorepo project structures by pinning version dependencies when \nbuilding and publishing archives with local path dependencies to other Poetry projects within the same monorepo.\n\n## Installation\n\n```\npoetry self add poetry-monorepo-dependency-plugin\n```\n\nIf you want to activate `poetry-monorepo-dependency-plugin` for all [build][poetry-build] and\n[publish][poetry-publish] command invocations, add the following to your project\'s `pyproject.toml`\nthat has path dependencies to other Poetry projects:\n\n```toml\n[tool.poetry-monorepo-dependency-plugin]\nenable = true\n```\n\n## Usage\n\nDuring archive building or publishing, this plugin will rewrite [path dependencies](https://python-poetry.org/docs/dependency-specification/#path-dependencies) \nto other Poetry projects using the corresponding pinned version dependency extracted from the referenced project\'s `pyproject.toml`.\nThe extracted dependency version will be applied to the generated archive using the strategy specified in the `version-pinning-strategy`\nconfiguration.  By referencing pinned version dependencies in published archive files, package consumers may more easily depend on\nand install packages that are built within complex monorepos, without needing to replicate the exact folder structure utilized within\nthe monorepo for that project\'s dependencies.\n\nFor example, assume that `spam` and `ham` Poetry projects exist within the same monorepo and use the following `pyproject.toml`\nconfigurations.\n\n`spam/pyproject.toml`:\n```toml\n[tool.poetry]\nname = "spam"\nversion = "0.1.0"\n\n[tool.poetry.dependencies]\nham = {path = "../ham", develop = true}\n```\n\n`ham/pyproject.toml`:\n```\n[tool.poetry]\nname = "ham"\nversion = "1.2.3"\n```\nWhen generating `wheel` or `sdist` archives for the `spam` project through Poetry\'s [build][poetry-build] or \n[publish][poetry-publish] commands, the corresponding `spam` package will be constructed as if its dependency on the\n`ham` project were declared as `ham = "1.2.3"`.  As a result, package metadata in archives for `spam` will shift from\n`Requires-Dist: ham @ ../ham` to `Requires-Dist: ham (==1.2.3)`\n\n### Command line mode\n\nIf you need greater control over when `poetry-monorepo-dependency-plugin` is activated, this plugin exposes new `build-rewrite-path-deps`\nand `publish-rewrite-path-deps` Poetry commands for on-demand execution.  For example, it may be desirable to only use this\nplugin during CI to support a monorepo\'s artifact deployment and/or release process.  When these custom Poetry commands are invoked, \nany configuration defined in the project\'s `pyproject.toml` `[tool.poetry-monorepo-dependency-plugin]` section is ignored and all options\n(other than `enable`) are exposed as command line options.  For example:\n```commandline\npoetry build-rewrite-path-deps --version-pinning-strategy=semver\n```\n\n### Configuration\n\nThe following configuration options are supported within your project\'s `pyproject.toml` configuration:\n\n* `[tool.poetry-monorepo-dependency-plugin]`: Parent-level container for plugin\n  * `enable` (`boolean`, default: `false`): Since Poetry plugins are globally installed, this configuration allows projects\nto opt-in to this plugin\'s modifications of the archives built and/or published Poetry\n  * `version-pinning-strategy` (`string`, default: `mixed`, options: `mixed`, `semver`, `exact`): Strategy by which path \ndependencies to other Poetry projects will be versioned in generated archives. Given a path dependency to a Poetry project \nwith version `1.2.3`, the version of the dependency referenced in the generated archive is `^1.2.3` for \n`semver` and `=1.2.3` for `exact`.  `mixed` mode switches versioning strategies based on whether the dependency\nPoetry project version is an in-flight development version or a release - if a development version (i.e. `1.2.3.dev456`),\n`semver` is applied (i.e. `^1.2.3dev`), and if a release version (i.e. `1.2.3`), `exact` is applied (i.e. `=1.2.3`).\n  \n## Licence\n\n`poetry-monorepo-dependency-plugin` is available under the [MIT licence][mit_licence].\n\n## Releasing to PyPI\n\nReleasing `poetry-monorepo-dependency-plugin` relies on the [maven-release-plugin](https://maven.apache.org/maven-release/maven-release-plugin/)\nto automate manual release activities and [Habushu](https://bitbucket.org/cpointe/habushu/) to automate the execution of a\nPoetry-based DevOps workflow via a custom Maven lifecycle.  During Maven\'s `deploy` phase, the appropriate plugin packages\nwill be published to PyPI.  \n\nA [PyPI account](https://pypi.org/account/register/) with access to the [poetry-monorepo-dependency-plugin](https://pypi.org/project/poetry-monorepo-dependency-plugin/) \nproject is required. PyPI account credentials should be specified in your `settings.xml` under the `<id>pypi</id>` `<server>` entry:\n\n```xml\n<settings>\n  <servers>\n    <server>\n      <id>pypi</id>\n      <username>pypi-username</username>\n      <password>{encrypted-pypi-password}</password>\n    </server>\n  </servers>\n</settings>\n```\nExecute `mvn release:clean release:prepare`, answer the prompts for the versions and tags, and execute `mvn release:perform` to publish\nthe package to PyPI. \n\n[poetry]: https://python-poetry.org/\n[poetry-build]: https://python-poetry.org/docs/cli/#build\n[poetry-publish]: https://python-poetry.org/docs/cli/#publish\n[mit_licence]: http://dan.mit-license.org/',
    'author': 'Eric Konieczny',
    'author_email': 'ekonieczny@cpointe-inc.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://bitbucket.org/cpointe/poetry-monorepo-dependency-plugin',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
