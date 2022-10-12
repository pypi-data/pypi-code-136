from omito_config_core import BasePlugin
from boto3.session import Session
import json

ssm_client = Session().client('ssm')
secretsmanager_client = Session().client('secretsmanager')


class SSMPlugin(BasePlugin):

  def protocol(self) -> str:
    return 'ssm'

  def get_value(self, key: str):

    value = ssm_client.get_parameter(Name=key, WithDecryption=True)
    return value['Parameter']['Value']


class AWSPlugin(BasePlugin):

  def protocol(self) -> str:
    return 'aws'

  def get_value(self, key: str):

    secret_id = key.split('/')[0]
    json_key = key.split('/')[1]
    value = secretsmanager_client.get_secret_value(SecretId=secret_id)
    if not json_key:
      return value['SecretString']
    else:
      return json.loads(value['SecretString'])[json_key]
