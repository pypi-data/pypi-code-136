# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ghgql']

package_data = \
{'': ['*']}

install_requires = \
['fnc>=0.5.3,<0.6.0', 'requests>=2.28.1']

setup_kwargs = {
    'name': 'ghgql',
    'version': '1.0.2',
    'description': 'Thin wrapper for interacting with the Github GraphQL API',
    'long_description': '# ghgql\n\nThin wrapper for interacting with the [Github GraphQL API](https://docs.github.com/en/graphql).\n\n## Status\n\n[![Documentation Status](https://readthedocs.org/projects/ghgql/badge/?version=latest)](https://ghgql.readthedocs.io/en/latest/?badge=latest)\n[![CodeQL](https://github.com/kwk/ghgql/actions/workflows/codeql.yml/badge.svg)](https://github.com/kwk/ghgql/actions/workflows/codeql.yml)\n[![ci-cd](https://github.com/kwk/ghgql/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/kwk/ghgql/actions/workflows/ci-cd.yml)\n[![codecov](https://codecov.io/gh/kwk/ghgql/branch/main/graph/badge.svg?token=ASSPTOL3JU)](https://codecov.io/gh/kwk/ghgql)\n[![release](https://img.shields.io/github/release/kwk/ghgql.svg)](https://github.com/kwk/ghgql/releases)\n\n## Documentation\n\nPlease find the documentation and usage examples here: https://ghgql.readthedocs.io/en/latest/\n\n## Installation\n\n```bash\n$ pip install ghgql\n```\n\n## Usage\n\nFor a more in-depth example, take a look at [the example in the documentation](https://ghgql.readthedocs.io/en/latest/example.html). Here\'s a basic example.\n\n```python\nimport os\nimport fnc\nimport ghgql\n\nquery = """\nquery ($searchQuery: String!) {\n  search(query: $searchQuery, type: ISSUE, first: 1) {\n    edges {\n      node {\n        ... on Issue {\n          id\n          number\n          title\n          url\n        }\n      }\n    }\n  }\n}\n"""\n\nwith ghgql.GithubGraphQL(token=os.getenv("GITHUB_TOKEN")) as ghapi:\n    result = ghapi.query(query=query, variables={"searchQuery": "llvm/llvm-project"})\n    print(fnc.get("search.edges", result))\n```\n\nShould output something like this:\n\n```yaml\n[{\'node\': {\'id\': \'I_kwDOHicqdc5RG-tC\',\n   \'number\': 16,\n   \'title\': \'llvm/llvm-project\',\n   \'url\': \'https://github.com/KhushP786/open-sauced-goals/issues/16\'}}]\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n### Commit message conventions and semantic versioniong (semver)\n\nWe use semantic versioning and [these commit message conventions](https://www.conventionalcommits.org/en/v1.0.0/)\ncan be used to automatically bump the version number and generate the changelog.\n\n## License\n\n`ghgql` was created by Konrad Kleine. It is licensed under the terms of the MIT license.\n\n## Credits\n\nThis project was created with the help of [this python packaging documentation](https://py-pkgs.org/01-introduction).\n\n`ghgql` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Konrad Kleine',
    'author_email': 'None',
    'maintainer': 'Konrad Kleine',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/ghgql/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
