# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iam_builder']

package_data = \
{'': ['*'], 'iam_builder': ['schemas/*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'jsonschema>=4.10.0,<5.0.0', 'parameterized>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['iam_builder = iam_builder.command_line:main']}

setup_kwargs = {
    'name': 'iam-builder',
    'version': '4.1.2',
    'description': 'A lil python package to generate iam policies',
    'long_description': '# IAM Builder\n\n[![Actions Status](https://github.com/moj-analytical-services/iam_builder/workflows/IAM%20Builder/badge.svg)](https://github.com/moj-analytical-services/iam_builder/actions)\n\nA python script to generate an IAM policy based on a yaml or json configuration.\n\nTo install:\n\n```\n# Most stable\npip install iam-builder\n\n# OR directly from github\npip install git+git://github.com/moj-analytical-services/iam_builder.git#egg=iam_builder\n```\n\nTo use the command line interface:\n\n```\niam_builder -c examples/iam_config.yaml -o examples/iam_policy.json\n```\n\n- `-c` is the path to your iam configuration (either a yaml or json file).\n- `-o` is the path to your output iam policy (needs to be a json file).\n\nOr to do the same thing in python:\n\n```python\nimport yaml\nimport json\nfrom iam_builder.iam_builder import build_iam_policy\n\nwith open(\'examples/iam_config.yaml\') as f:\n  config = yaml.load(f, Loader=yaml.FullLoader)\n\niam_policy = build_iam_policy(config)\n\nwith open(\'examples/iam_policy.json\', "w+") as f:\n  json.dump(iam_policy, f, indent=4, separators=(\',\', \': \'))\n```\n\nBoth scripts will create the output iam_policy seen in the [examples](examples/) folder. You can also see [more example configs](tests/test_config/) by looking in the unit tests.\n\nYour config file can be either a yaml or json file.\n\nThe example yaml (`iam_config.yaml`) looks this:\n\n```yaml\niam_role_name: iam_role_name\n\nathena:\n  write: false\n\nglue_job: true\n\nsecrets: true\n\ns3: \n  read_only:\n    - test_bucket_read_only/*\n\n  write_only:\n    - test_bucket_write_only/*\n    - test_bucket_read_only/write_only_folder/*\n\n  read_write:\n    - test_bucket_read_write/*\n    - test_bucket_read_only/write_folder/*\n```\n\nWhilst the example json (`iam_config.json`) looks like this:\n\n```json\n{\n  "iam_role_name": "iam_role_name",\n  "athena": {\n    "write": false\n  },\n  "glue_job": true,\n  "secrets": true,\n  "s3": {\n    "read_only": [\n      "test_bucket_read_only/*"\n    ],\n    "write_only": [\n      "test_bucket_write_only/*",\n      "test_bucket_read_only/write_only_folder/*"\n    ],\n    "read_write": [\n      "test_bucket_read_write/*",\n      "test_bucket_read_only/write_folder/*"\n    ]\n  }\n}\n```\n- **iam_role_name:** The role name of your airflow job; required if you want to run glue jobs or access secrets.\n\n- **athena:** Can have two keys. \n  - **write**: Either `true` or `false`. If `false` then only read access to Athena (cannot create, delete or alter tables, databases and partitions). If `true` then the role will also have the ability to do stuff like CTAS queries, `DROP TABLE`, `CREATE DATABASE`, etc.\n  - **dump_bucket**: The location in S3 (either an S3 path or a list of S3 paths) for temporarily storing the results of queries. This defaults to `mojap-athena-query-dump` and should not normally need changing.\n\n- **glue_job:** Boolean; must be set to `true` to allow role to run glue jobs. If `false` or absent role will not be able to run glue jobs.\n\n- **secrets:** Boolean; must be set to `true` to allow role to access secrets from AWS Parameter Store. If `false` or absent role will not be able to access secrets.\n\n- **s3:** Can have up to 3 keys: `read_only`, `write_only` and `read_write`. Each key describes the level of access you want your iam policy to have with each s3 path. More details below:\n  \n  - **read_only:** A list of s3 paths that the iam_role should be able to access (read only). Each item in the list should either be a path to a object or finish with `/*` to denote that it can access everything within that directory. _Note the S3 paths don\'t start with `s3://` in the config._\n\n  - **write_only:** A list of s3 paths that the iam_role should be able to access (write only). Each item in the list should either be a path to a object or finish with `/*` to denote that it can access everything within that directory. _Note the S3 paths don\'t start with `s3://` in the config._\n\n  - **read_write:** A list of s3 paths that the iam_role should be able to access (read and write). Each item in the list should either be a path to a object or finish with `/*` to denote that it can access everything within that directory. _Note the S3 paths don\'t start with `s3://` in the config._\n\n## How to update\n\nWhen updating IAM builder, make sure to change the version number in `pyproject.toml` and describe the change in `CHANGELOG.md`.\n\nIf you have changed any dependencies in `pyproject.yaml`, run `poetry update` to update `poetry.lock`.\n\nOnce you have created a release in GitHub, to publish the latest version to PyPI, run:\n\n```\npoetry build\npoetry publish -u <username>\n```\n\nHere, you should substitute `<username>` for your PyPI username. In order to publish to PyPI, you must be an owner of the project.\n',
    'author': 'Karik Isichei',
    'author_email': 'karik.isichei@digital.justice.gov.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
