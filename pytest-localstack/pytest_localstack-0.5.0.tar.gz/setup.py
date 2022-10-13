# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_localstack', 'pytest_localstack.contrib']

package_data = \
{'': ['*']}

install_requires = \
['botocore>=1.4.31,<2.0.0,!=1.4.45',
 'docker>=4.0.0,<5.0.0',
 'pluggy>=0.12.0,<0.13.0',
 'pytest>=6.0.0,<7.0.0']

entry_points = \
{'pytest11': ['localstack = pytest_localstack']}

setup_kwargs = {
    'name': 'pytest-localstack',
    'version': '0.5.0',
    'description': 'Pytest plugin for AWS integration tests',
    'long_description': 'pytest-localstack\n=================\n\n.. image:: https://img.shields.io/pypi/v/pytest-localstack.svg\n    :alt: PyPI\n    :target: https://pypi.org/project/pytest-localstack/\n\n.. image:: https://img.shields.io/travis/mintel/pytest-localstack/master.svg\n    :alt: Travis-CI\n    :target: https://travis-ci.org/mintel/pytest-localstack\n\n.. image:: https://img.shields.io/codecov/c/github/mintel/pytest-localstack.svg\n    :alt: Codecov\n    :target: https://codecov.io/gh/mintel/pytest-localstack\n\n.. image:: https://img.shields.io/github/license/mintel/pytest-localstack.svg\n    :target: https://github.com/mintel/pytest-localstack/blob/master/LICENSE\n\n.. image:: https://img.shields.io/github/issues/mintel/pytest-localstack.svg\n    :target: https://github.com/mintel/pytest-localstack/issues\n\n.. image:: https://img.shields.io/github/forks/mintel/pytest-localstack.svg\n    :target: https://github.com/mintel/pytest-localstack/network\n\n.. image:: https://img.shields.io/github/stars/mintel/pytest-localstack.svg\n    :target: https://github.com/mintel/pytest-localstack/stargazers\n\npytest-localstack is a plugin for pytest_ to create AWS_ integration tests\nvia a Localstack_ Docker container.\n\n`Read The Docs`_\n\n**Requires:**\n\n- pytest >= 3.3.0\n- Docker\n\nTested against Python >= 3.6.\n\n.. _pytest: http://docs.pytest.org/\n.. _AWS: https://aws.amazon.com/\n.. _Localstack: https://github.com/localstack/localstack\n.. _Read the Docs: https://pytest-localstack.readthedocs.io/\n\n\nFeatures\n--------\n* Create `pytest fixtures`_ that start and stop a Localstack container.\n* Temporarily patch botocore to redirect botocore/boto3 API calls to Localstack container.\n* Plugin system to easily extend supports to other AWS client libraries such as aiobotocore_.\n\n.. _pytest fixtures: https://docs.pytest.org/en/stable/fixture.html\n\nExample\n-------\n.. code-block:: python\n\n    import boto3\n    import pytest_localstack\n\n    localstack = pytest_localstack.patch_fixture(\n        services=["s3"],  # Limit to the AWS services you need.\n        scope=\'module\',  # Use the same Localstack container for all tests in this module.\n        autouse=True,  # Automatically use this fixture in tests.\n    )\n\n    def test_s3_bucket_creation():\n        s3 = boto3.resource(\'s3\')  # Botocore/boto3 will be patched to use Localstack\n        assert len(list(s3.buckets.all())) == 0\n        bucket = s3.Bucket(\'foobar\')\n        bucket.create()\n        assert len(list(s3.buckets.all())) == 1\n\nServices\n--------\n* apigateway\n* cloudformation\n* cloudwatch\n* dynamodb\n* dynamodbstreams\n* ec2\n* es\n* firehose\n* iam\n* kinesis\n* lambda\n* logs\n* redshift\n* route53\n* s3\n* secretsmanager\n* ses\n* sns\n* sqs\n* ssm\n* stepfunctions\n* sts\n\nInstallation\n------------\n.. code-block:: bash\n\n    $ pip install pytest-localstack\n\n\nTODO\n----\n\n* More detailed docs.\n* Break Docker container running out of LocalstackSession.\n* Make botocore patching more comprehensible.\n* Add common test resource fixture factories i.e. S3 buckets, SQS queues, SNS topics, etc.\n* Test this works for non-localhost Docker containers.\n* Add other client libraries such as aiobotocore_.\n\n.. _aiobotocore: https://github.com/aio-libs/aiobotocore\n',
    'author': 'Mintel Group Ltd.',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mintel/pytest-localstack',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
