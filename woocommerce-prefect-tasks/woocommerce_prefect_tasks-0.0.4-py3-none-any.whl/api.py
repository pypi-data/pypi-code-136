import json
import os
from time import time

from configparser import ConfigParser
from .aws import SecretsManagerStorage, SecretsManagerClient

from woocommerce import API

from prefect import *

from typing import Any


class Api:
    _instance = None

    def __new__(cls, aws_secret_name: str = None, aws_secret_region: str = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, aws_secret_name: str = None, aws_secret_region: str = None):
        try:
            if os.getenv('AWS_CONFIG_FILE'):
                self.aws_config = read_config(os.getenv('AWS_CONFIG_FILE'))

            self.aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
            self.aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

            if aws_secret_name:
                self.aws_secretsmanager_secret_name = aws_secret_name
            else:
                self.aws_secretsmanager_secret_name = os.getenv('AWS_SM_WOOCOMMERCE_SECRET_NAME')

            if aws_secret_region:
                self.aws_secretsmanager_region = aws_secret_region
            else:
                self.aws_secretsmanager_region = os.getenv('AWS_SM_REGION')

            self.secretsmanager_client = SecretsManagerClient.get_instance(
                self.aws_access_key, self.aws_secret_key,
                region_name=self.aws_secretsmanager_region,
            )

            self.secretsmanager_client.name = self.aws_secretsmanager_secret_name

            self.storage = SecretsManagerStorage(secretsmanager_client=self.secretsmanager_client,
                                                 name=self.secretsmanager_client.name)

            self.storage.read_config()

            self.url = self.storage.get('woocommerce', 'url')
            self.consumer_key = self.storage.get('woocommerce', 'consumer_key')
            self.consumer_secret = self.storage.get('woocommerce', 'consumer_secret')

            kw = dict(self.storage.items('woocommerce'))
            kw.pop('url', None)
            kw.pop('consumer_key', None)
            kw.pop('consumer_secret', None)

            self.api_client = API(url=self.url, consumer_key=self.consumer_key, consumer_secret=self.consumer_secret, **kw)

        except Exception as e:
            print(e)
            raise e


def read_config(filepath):
    """Read AWS configuration file"""
    config = ConfigParser()
    config.read(filepath)
    return {s: dict(config.items(s)) for s in config.sections()}
