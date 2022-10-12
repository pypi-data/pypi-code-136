import pytest
import boto3
from moto import mock_ssm, mock_secretsmanager
import os
from pathlib import Path

print('IN CONFTEST')


@pytest.fixture(scope='function')
def aws_credentials():
  moto_credentials_file_path = Path(__file__).parent.absolute() / 'dummy_aws_credentials'
  os.environ['AWS_SHARED_CREDENTIALS_FILE'] = str(moto_credentials_file_path)
  os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
  os.environ['AWS_SECRET_ACCESS_ID'] = 'testing'
  os.environ['AWS_SECURITY_TOKEN'] = 'testing'
  os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture(scope='function')
def s3(aws_credentials):
  with mock_ssm():
    yield boto3.client('ssm', region_name='eu-west-2')


@pytest.fixture(scope='function')
def s3(aws_credentials):
  with mock_secretsmanager():
    yield boto3.client('secretsmanager', region_name='eu-west-2')