import json

import boto3
from botocore.exceptions import ClientError

from bigeye_sdk.log import get_logger

log = get_logger(__file__)


def run_glue_crawler(region_name: str, crawler_name: str):
    session = boto3.session.Session()
    client = session.client(
        service_name='glue',
        region_name=region_name
    )

    try:
        client.start_cralwer(Name=crawler_name)
    except ClientError as e:
        log.error(e)


def get_secret(region_name: str, secret_name: str) -> dict:
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        else:
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            return json.loads(get_secret_value_response['SecretString'])
        else:
            raise Exception('Binary Secrets not supported.')
            # decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])


def set_other_secret_type(region_name: str, configs: dict):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        client.create_secret(**configs)
        log.info(f'Created secret {configs["Name"]}')
    except ClientError as e:
        log.error(e)
        raise


def validate_aws_account():
    log.info('Validating AWS Credentials')
    if boto3.client('sts').get_caller_identity().get('Account') is None:
        raise Exception('Not authenticated with AWS.')
