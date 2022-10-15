# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gl_search', 'gl_search.clis']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'dynaconf>=3.1.11,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['gl-search = gl_search.cli:cli']}

setup_kwargs = {
    'name': 'gl-search',
    'version': '0.1.0',
    'description': 'Script to help search code in self-hosted gitlab',
    'long_description': '# gl-search\n\nThis is a lib that use gitlab api to search code.\nThis code is based in the lib [gitlab-search](https://github.com/phillipj/gitlab-search).\n\n## About\n\nIt is a lib to search code at gitlab.\nThis search can be parameterized with params groups, extension, filename, path, max-workers and visibility.\n\n## How install?\n\n```bash\npip install gl_search\n```\n\n## How it works?\n\nThe lib use gitlab token (GITLAB_PRIVATE_TOKEN) to search.\n\n## How to setup the token?\n\nGet your token at gitlab and then execute following command to save at home user at the .gl-settings.toml file.\n\n```bash\ngl-search setup-token <token>\n```\n\n## Can I change gitlab official to self hosted?\n\nYes you can. Use following command to setup the gitlab-address\n\n```bash\ngl-search setup-gitlab-address <self-hosted-gitlab-address>\n```\n\n## Where I get gitlab token?\n\nYou can get on following link [gitlab-token](https://gitlab.com/-/profile/personal_access_tokens)\n\n## Why this lib was built?\n\nI had problem with repo visibility using a mentioned lib above so I built this script to resolve my problem.\n\n## How to use\n\n```bash\ngl-search search test\n```\n\nThis options is show up below.\n\n```bash\n➜  gl_search git:(main) ✗ gl-search search --help\nUsage: gl-search search [OPTIONS] SEARCH_CODE_INPUT\n\n  Search command.\n\nOptions:\n  -p, --path TEXT                 search by Path\n  -fn, --filename TEXT            search by filename\n  -ext, --extension TEXT          code filename extension :: py,js,cs\n  -g, --groups TEXT               search by gitlab group\n  -mw, --max-workers INTEGER      number of parallel requests\n  -v, --visibility [internal|public|private]\n                                  repositories visibility\n  --help                          Show this message and exit.\n```\n\n## How was made the lib?\n\nThe lib was built using click, rich, request, ThreadPoolExecutor.\n',
    'author': 'Bernardo Gomes',
    'author_email': 'bgomesdeabreu@gmail.com',
    'maintainer': 'Bernardo Gomes',
    'maintainer_email': 'bgomesdeabreu@gmail.com',
    'url': 'https://github.com/Bernardoow/gl_search',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
