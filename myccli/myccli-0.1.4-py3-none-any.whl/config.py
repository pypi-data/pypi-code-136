import configparser
import logging
import os
import os.path
import boto3
from dataclasses import dataclass
from typing import Optional


LOGGER_NAME = 'myccli'

DEFAULT_DIST_DIR = './.mycelium'
PRIVATE_NS_DOMAIN = 'app.net'


def _get_default_aws_account_id(verbose) -> Optional[str]:
    var = os.environ.get('AWS_ACCOUNT_ID')
    if var is not None:
        return var

    if verbose:
        logging.warning(
            'Performing request to determine AWS account id.\n'
            'Please consider setting AWS_ACCOUNT_ID environment variable to skip this request.'
        )
    return boto3.client('sts').get_caller_identity().get('Account')


def _get_default_aws_region() -> Optional[str]:
    # read from environment
    var = os.environ.get('AWS_DEFAULT_REGION')
    if var is not None:
        return var

    # read from ~/.aws/config
    conf = configparser.ConfigParser()
    conf_path = os.path.join(os.path.expanduser('~'), '.aws/config')
    if os.path.exists(conf_path):
        conf.read(conf_path)
        if 'default' in conf and 'region' in conf['default']:
            return conf['default']['region']

    return None


@dataclass
class MyceliumConfiguration:
    aws_account_id: Optional[str]
    aws_region: Optional[str]
    verbose: bool = False

    @staticmethod
    def default(verbose=False):
        """
        Creates a default configuration based on environment variables and other system settings.
        """
        return MyceliumConfiguration(
            aws_account_id=_get_default_aws_account_id(verbose),
            aws_region=_get_default_aws_region(),
            verbose=verbose,
        )
