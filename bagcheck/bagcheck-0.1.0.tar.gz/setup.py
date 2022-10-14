# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bagcheck', 'bagcheck.concourse']

package_data = \
{'': ['*']}

install_requires = \
['jsonpath-ng>=1.5.3,<2.0.0', 'pyyaml>=6.0,<7.0', 'rich-click>=1.5.2,<2.0.0']

entry_points = \
{'console_scripts': ['bagcheck = bagcheck.bagcheck:cli']}

setup_kwargs = {
    'name': 'bagcheck',
    'version': '0.1.0',
    'description': 'A concourse pipeline validation tool',
    'long_description': '# BagCheck\n\n## About\n\n`bagcheck` is a relatively simply command line utility developed to make validating Concourse pipelines simpler. To accomplish this, `bagcheck` has the following functionality:\n\n## Checking a pipeline\n\nTo check your pipeline, simply run:\n\n```bash\nbagcheck check -f /path/to/your/concourse/pipeline.yaml\n```\n\nat which point `bagcheck` will proceed to check for the following conditions:\n\n- All git resources are pointed at the `main` branch\n- All PR resource puts in the same job have the same context\n- All PR statuses are accounted for in a job (success, failure, error, pending)\n- All jobs have a timeout set\n\n### Disabling Specific Checks\n\nSometimes you want to skip a check across the board (e.g. you don\'t want timeouts in a specific pipeline) or you only want to disable a check for a specific job/resource. To do this, you\'ll use a `.bagcheck` file. \n\nAn example file looks something like this:\n\n```yaml\ndisable:\n  global:\n    - check-main-branch\n    - ...\n  local:\n    - path: \'$.jobs[?(@.name = "job-name-1")]\'\n      tests:\n        - check-pr-statuses\n        - ...\n    - path: \'$.jobs[?(@.name = "job-name-2")]\'\n      tests:\n        - check-timeout\n        - ...\n    - ...\n```\n\nwith any check listed under the `disable.global` key being completely disabled and the tests under each path being disabled when the job meets that JSONPath criteria (the ellipsis denote that you can include as many as you want in each section).\n\nCurrently the following tests are run and as a consequence can be disabled:\n\n- `check-main-branch`\n- `check-timeout`\n- `check-pr-statuses`\n- `check-pr-contexts`\n\nOne thing to note is that `bagcheck` will first attempt to read a file located at `~/.bagcheck` and then will attempt to read one at the current working directory, combining the values with whatever is located in your `~/.bagcheck` file.\n\n## Summarizing a pipeline\n\nHaving to read through a 1000+ line YAML file can make it hard to understand what the pipeline is doing on a conceptual level as well as how everything ties together. To help with this, you can run:\n\n```bash\nbagcheck summary -f /path/to/your/concourse/pipeline.yaml\n```\n\nat which point `bagcheck` will print out a summarized version of your pipeline which attempts to:\n\n- List in plain English what each step of a job does\n- Describe what resource changes will cause the job to trigger\n- Describe which jobs will be triggered as a result\n',
    'author': 'John Carter',
    'author_email': 'jfcarter2358@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jfcarter2358/bagcheck',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
